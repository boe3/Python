#Sprint 4: Statistical Data Analysis (SDA)
#Chapter 4: SDA Project


# Loading all the libraries
import pandas as pd
import numpy as np
from scipy import stats as st
import matplotlib.pyplot as plt
##import seaborn as sns

##plt.style.use('seaborn-v0_8')


# Load the data files into different DataFrames
calls = pd.read_csv('datasets/megaline_calls.csv')
internet = pd.read_csv('datasets/megaline_internet.csv')
messages = pd.read_csv('datasets/megaline_messages.csv')
plans = pd.read_csv('datasets/megaline_plans.csv')
users = pd.read_csv('datasets/megaline_users.csv')


# Print the general/summary information about the plans' DataFrame
plans.info()

# Print a sample of data for plans
plans.head()


#Fix obvious issues with the data given the initial observations.
# (Usually: make sure column names are consistent, types are proper, etc.)
# Standardize plan_name column to lowercase if needed
plans['plan_name'] = plans['plan_name'].str.lower()

# Check for duplicates
plans = plans.drop_duplicates().reset_index(drop=True)


#Add additional factors to the data if you believe they might be useful.
# For convenience, precompute included GB from MB
plans['gb_included'] = (plans['mb_per_month_included'] / 1024).astype(int)
plans


# Print the general/summary information about the users' DataFrame
users.info()


# Print a sample of data for users
users.head()


#Fix obvious issues with the data given the initial observations.
# Convert dates to datetime
users['reg_date'] = pd.to_datetime(users['reg_date'], format='%Y-%m-%d')
users['churn_date'] = pd.to_datetime(users['churn_date'], format='%Y-%m-%d')

# Standardize city and plan names
users['city'] = users['city'].str.strip()
users['plan'] = users['plan'].str.lower().str.strip()

# Drop exact duplicates if any
users = users.drop_duplicates(subset='user_id')


#Add additional factors to the data if you believe they might be useful.
# Extract registration month and year if needed
users['reg_month'] = users['reg_date'].dt.to_period('M')

# Create a NY-NJ flag for later hypothesis test
users['is_ny_nj'] = users['city'].str.contains('NY-NJ', case=False, na=False)
users.head()


# Print the general/summary information about the messages' DataFrame
messages.info()


# Print a sample of data for messages
messages.head()


#Fix obvious issues with the data given the initial observations.
# Convert dates to datetime
messages['message_date'] = pd.to_datetime(messages['message_date'], format='%Y-%m-%d')

# Drop duplicates if any
messages = messages.drop_duplicates()


#Add additional factors to the data if you believe they might be useful.
# Extract year-month for aggregation
messages['month'] = messages['message_date'].dt.to_period('M')
messages.head()


# Print the general/summary information about the internet DataFrame
internet.info()


# Print a sample of data for the internet traffic
internet.head()


#Fix obvious issues with the data given the initial observations.
# Convert dates to datetime
internet['session_date'] = pd.to_datetime(internet['session_date'], format='%Y-%m-%d')

# Replace obviously wrong mb_used (like negative) with NaN and drop
internet = internet[internet['mb_used'] >= 0]

# Drop duplicates
internet = internet.drop_duplicates()


#Add additional factors to the data if you believe they might be useful.
# Extract year-month
internet['month'] = internet['session_date'].dt.to_period('M')
internet.head()


#???

# Print the general/summary information about the calls DataFrame
calls.info()


# Print a sample of data for calls
calls.head()


# Fix obvious issues with the data given the initial observations.
# Convert dates to datetime
calls['call_date'] = pd.to_datetime(calls['call_date'], format='%Y-%m-%d')

# Replace negative durations with NaN and drop them if any
calls = calls[calls['duration'] >= 0]

# Drop duplicates
calls = calls.drop_duplicates()


# Add additional factors to the data if you believe they might be useful.
# Extract month
calls['month'] = calls['call_date'].dt.to_period('M')

# According to the condition: Megaline rounds seconds up to minutes.
# Here duration is already given in minutes, but may not be integer.
# Round each individual call up to the next whole minute.
calls['minutes_rounded'] = np.ceil(calls['duration']).astype(int)
calls.head()


# Print out the plan conditions and make sure they are clear for you
plans


# Calculate the number of calls made by each user per month. Save the result.
calls_per_month = (
    calls
    .groupby(['user_id', 'month'])
    .agg(calls_count=('id', 'count'))
    .reset_index()
)
calls_per_month.head()


# Calculate the amount of minutes spent by each user per month. Save the result.
minutes_per_month = (
    calls
    .groupby(['user_id', 'month'])
    .agg(total_minutes=('minutes_rounded', 'sum'))
    .reset_index()
)
minutes_per_month.head()


# Calculate the number of messages sent by each user per month. Save the result.
messages_per_month = (
    messages
    .groupby(['user_id', 'month'])
    .agg(messages_count=('id', 'count'))
    .reset_index()
)
messages_per_month.head()


# Calculate the volume of internet traffic used by each user per month. Save the result.
internet_per_month = (
    internet
    .groupby(['user_id', 'month'])
    .agg(mb_used=('mb_used', 'sum'))
    .reset_index()
)
internet_per_month.head()


# Merge the data for calls, minutes, messages, internet based on user_id and month

# Start with users × months present in any activity
data = users[['user_id', 'city', 'plan', 'is_ny_nj']].copy()

# We'll merge all per-month info into one table
# First, create a base frame of all user-months moving from each activity table

user_month = pd.concat([
    calls_per_month[['user_id', 'month']],
    minutes_per_month[['user_id', 'month']],
    messages_per_month[['user_id', 'month']],
    internet_per_month[['user_id', 'month']]
]).drop_duplicates().reset_index(drop=True)

# Merge user info
user_month = user_month.merge(
    users[['user_id', 'city', 'plan', 'is_ny_nj']],
    on='user_id',
    how='left'
)

# Merge aggregates
user_month = user_month.merge(calls_per_month, on=['user_id', 'month'], how='left')
user_month = user_month.merge(minutes_per_month, on=['user_id', 'month'], how='left')
user_month = user_month.merge(messages_per_month, on=['user_id', 'month'], how='left')
user_month = user_month.merge(internet_per_month, on=['user_id', 'month'], how='left')

# Fill NaNs (no activity) with zeros
for col in ['calls_count', 'total_minutes', 'messages_count', 'mb_used']:
    user_month[col] = user_month[col].fillna(0)

user_month.head()


# Add the plan information
user_month = user_month.merge(
    plans,
    left_on='plan',
    right_on='plan_name',
    how='left'
)

user_month.head()


# Calculate the monthly revenue for each user
def compute_revenue(row):
    # Base monthly fee
    revenue = row['usd_monthly_fee']
    
    # Extra minutes
    extra_minutes = max(0, row['total_minutes'] - row['minutes_included'])
    revenue += extra_minutes * row['usd_per_minute']
    
    # Extra messages
    extra_messages = max(0, row['messages_count'] - row['messages_included'])
    revenue += extra_messages * row['usd_per_message']
    
    # Extra data: MB -> GB, rounding up the total per month
    extra_mb = max(0, row['mb_used'] - row['mb_per_month_included'])
    extra_gb = int(np.ceil(extra_mb / 1024)) if extra_mb > 0 else 0
    revenue += extra_gb * row['usd_per_gb']
    
    return revenue

user_month['revenue'] = user_month.apply(compute_revenue, axis=1)

user_month[['user_id', 'month', 'plan', 'total_minutes', 'messages_count', 'mb_used', 'revenue']].head()


# Compare average duration of calls per each plan per each distinct month. Plot a bar plot to visualize it.
calls_stats = (
    user_month
    .groupby(['plan', 'month'])
    .agg(mean_minutes=('total_minutes', 'mean'))
    .reset_index()
)

plt.figure(figsize=(12, 6))
sns.barplot(
    data=calls_stats,
    x='month',
    y='mean_minutes',
    hue='plan'
)
plt.title('Average monthly call minutes per user by plan')
plt.xlabel('Month')
plt.ylabel('Average minutes')
plt.xticks(rotation=45)
plt.legend(title='Plan')
plt.tight_layout()
plt.show()


# Compare the number of minutes users of each plan require each month. Plot a histogram.
plt.figure(figsize=(12, 5))

for i, plan_name in enumerate(user_month['plan'].unique(), 1):
    plt.subplot(1, 2, i)
    subset = user_month[user_month['plan'] == plan_name]
    plt.hist(subset['total_minutes'], bins=20, alpha=0.7)
    plt.title(f'Monthly minutes distribution: {plan_name}')
    plt.xlabel('Minutes')
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()


# Calculate the mean and the variance of the monthly call duration
call_stats_plan = (
    user_month
    .groupby('plan')['total_minutes']
    .agg(['mean', 'var', 'std'])
    .reset_index()
)

call_stats_plan


# Plot a boxplot to visualize the distribution of the monthly call duration
plt.figure(figsize=(8, 6))
sns.boxplot(
    data=user_month,
    x='plan',
    y='total_minutes'
)
plt.title('Monthly call minutes per user by plan')
plt.xlabel('Plan')
plt.ylabel('Total minutes per month')
plt.show()


# Compare the number of messages users of each plan tend to send each month
plt.figure(figsize=(12, 5))

for i, plan_name in enumerate(user_month['plan'].unique(), 1):
    plt.subplot(1, 2, i)
    subset = user_month[user_month['plan'] == plan_name]
    plt.hist(subset['messages_count'], bins=20, alpha=0.7)
    plt.title(f'Monthly messages distribution: {plan_name}')
    plt.xlabel('Messages')
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()


# Test the hypothesis: average revenue from Ultimate and Surf calling plans differs.
surf_revenue = user_month[user_month['plan'] == 'surf']['revenue']
ultimate_revenue = user_month[user_month['plan'] == 'ultimate']['revenue']

alpha = 0.05

results_plans = st.ttest_ind(
    surf_revenue,
    ultimate_revenue,
    equal_var=False  # Welch's t-test
)

print('T-statistic:', results_plans.statistic)
print('p-value:', results_plans.pvalue)

if results_plans.pvalue < alpha:
    print("We reject the null hypothesis: average revenue differs between Surf and Ultimate.")
else:
    print("We can't reject the null hypothesis: no significant difference detected.")


# Test the hypothesis: average revenue from users in NY-NJ area differs from other regions.
ny_nj_revenue = user_month[user_month['is_ny_nj'] == True]['revenue']
other_revenue = user_month[user_month['is_ny_nj'] == False]['revenue']

alpha = 0.05

results_region = st.ttest_ind(
    ny_nj_revenue,
    other_revenue,
    equal_var=False
)

print('T-statistic:', results_region.statistic)
print('p-value:', results_region.pvalue)

if results_region.pvalue < alpha:
    print("We reject the null hypothesis: average revenue differs between NY-NJ and other regions.")
else:
    print("We can't reject the null hypothesis: no significant difference detected.")





# Print out the plan conditions and make sure they are clear for you


# Calculate the number of calls made by each user per month. Save the result.


# Calculate the amount of minutes spent by each user per month. Save the result.


# Calculate the number of messages sent by each user per month. Save the result.


# Calculate the volume of internet traffic used by each user per month. Save the result.


# Merge the data for calls, minutes, messages, internet based on user_id and month


# Add the plan information


# Calculate the monthly revenue for each user


# Compare average duration of calls per each plan per each distinct month. Plot a bar plat to visualize it.


# Compare the number of minutes users of each plan require each month. Plot a histogram.


# Calculate the mean and the variance of the monthly call duration


# Plot a boxplot to visualize the distribution of the monthly call duration


# Compare the number of messages users of each plan tend to send each month


# Test the hypotheses


# Test the hypotheses




#WITHOUT SEABORN Library:
## Bar plot — average monthly call minutes per plan per month
# Average monthly call minutes per plan per month
calls_stats = (
    user_month
    .groupby(['plan', 'month'])
    .agg(mean_minutes=('total_minutes', 'mean'))
    .reset_index()
)

# Convert month to string for plotting
calls_stats['month'] = calls_stats['month'].astype(str)

# Get unique months and plans
months = sorted(calls_stats['month'].unique())
plans_list = calls_stats['plan'].unique()

# Prepare bar positions
x = np.arange(len(months))
width = 0.35

plt.figure(figsize=(12, 6))

for i, plan_name in enumerate(plans_list):
    subset = calls_stats[calls_stats['plan'] == plan_name]
    plt.bar(
        x + i*width,
        subset['mean_minutes'],
        width=width,
        label=plan_name.capitalize()
    )

plt.xticks(x + width/2, months, rotation=45)
plt.ylabel("Average Minutes")
plt.title("Average Monthly Call Minutes per User by Plan")
plt.legend()
plt.tight_layout()
plt.show()


## Histogram — monthly minutes per plan
plt.figure(figsize=(12, 5))

plans_list = user_month['plan'].unique()

for i, plan_name in enumerate(plans_list, 1):
    plt.subplot(1, 2, i)
    subset = user_month[user_month['plan'] == plan_name]['total_minutes']
    plt.hist(subset, bins=20, alpha=0.7, color='steelblue', edgecolor='black')
    plt.title(f"Monthly Minutes Distribution: {plan_name.capitalize()}")
    plt.xlabel("Minutes")
    plt.ylabel("Frequency")

plt.tight_layout()
plt.show()


## Boxplot — monthly call minutes
# Prepare data for boxplot
data_to_plot = [
    user_month[user_month['plan'] == plan]['total_minutes']
    for plan in plans_list
]

plt.figure(figsize=(8, 6))
plt.boxplot(data_to_plot, labels=[p.capitalize() for p in plans_list])
plt.title("Monthly Call Minutes per User by Plan")
plt.xlabel("Plan")
plt.ylabel("Total Minutes per Month")
plt.show()


## Histogram — monthly messages per plan
plt.figure(figsize=(12, 5))

for i, plan_name in enumerate(plans_list, 1):
    plt.subplot(1, 2, i)
    subset = user_month[user_month['plan'] == plan_name]['messages_count']
    plt.hist(subset, bins=20, alpha=0.7, color='darkorange', edgecolor='black')
    plt.title(f"Monthly Messages Distribution: {plan_name.capitalize()}")
    plt.xlabel("Messages")
    plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
