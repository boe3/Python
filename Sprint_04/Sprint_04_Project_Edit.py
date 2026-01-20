# Loading all the libraries

import pandas as pd
import numpy as np
from scipy import stats as st
import matplotlib.pyplot as plt

# plt.style.use('ggplot')


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


# Fix obvious issues with the data given the initial observations.

# Standardize plan names (lowercase, no spaces)
plans['plan_name'] = plans['plan_name'].str.lower().str.strip()

# Drop exact duplicates if any
plans = plans.drop_duplicates().reset_index(drop=True)


# Add additional factors to the data if you believe they might be useful.

# For convenience, compute GB included (integer) from MB included
plans['gb_included'] = (plans['mb_per_month_included'] / 1024).astype(int)
plans


# Print the general/summary information about the users' DataFrame

users.info()


# Print a sample of data for users

users.head()


# Fix obvious issues with the data given the initial observations.

# Convert date columns to datetime
users['reg_date'] = pd.to_datetime(users['reg_date'])
users['churn_date'] = pd.to_datetime(users['churn_date'])

# Standardize plan names and city formatting
users['plan'] = users['plan'].str.lower().str.strip()
users['city'] = users['city'].str.strip()

# Drop duplicate user records if any
users = users.drop_duplicates(subset='user_id')


# Add additional factors to the data if you believe they might be useful.

# Registration month
users['reg_month'] = users['reg_date'].dt.to_period('M')

# Flag users in NY-NJ area (assuming city names contain 'NY-NJ')
users['is_ny_nj'] = users['city'].str.contains('NY-NJ', case=False, na=False)

users.head()


# Print the general/summary information about the messages' DataFrame

messages.info()


# Print a sample of data for messages

messages.head()


# Fix obvious issues with the data given the initial observations.

# Convert message_date to datetime
messages['message_date'] = pd.to_datetime(messages['message_date'])

# Drop duplicates if any
messages = messages.drop_duplicates()


# Add additional factors to the data if you believe they might be useful.

# Extract year-month as a period for grouping
messages['month'] = messages['message_date'].dt.to_period('M')

messages.head()


# Print the general/summary information about the internet DataFrame

internet.info()


# Print a sample of data for the internet traffic

internet.head()


# Fix obvious issues with the data given the initial observations.

# Convert session_date to datetime
internet['session_date'] = pd.to_datetime(internet['session_date'])

# Remove negative mb_used values if present
internet = internet[internet['mb_used'] >= 0]

# Drop duplicates if any
internet = internet.drop_duplicates()


# Add additional factors to the data if you believe they might be useful.

# Extract year-month as a period for grouping
internet['month'] = internet['session_date'].dt.to_period('M')

internet.head()


# Print general/summary information about the calls DataFrame

calls.info()


# Print a sample of data for calls

calls.head()


# Fix obvious issues with the data given the initial observations.

# Convert call_date to datetime
calls['call_date'] = pd.to_datetime(calls['call_date'])

# Remove negative durations if any
calls = calls[calls['duration'] >= 0]

# Drop duplicates if any
calls = calls.drop_duplicates()


# Add additional factors to the data if you believe they might be useful.

# Extract year-month as a period for grouping
calls['month'] = calls['call_date'].dt.to_period('M')

# Round each call up to the next full minute
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

# Build a base of all user-month combinations present in any activity
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

# Merge metrics
user_month = user_month.merge(calls_per_month, on=['user_id', 'month'], how='left')
user_month = user_month.merge(minutes_per_month, on=['user_id', 'month'], how='left')
user_month = user_month.merge(messages_per_month, on=['user_id', 'month'], how='left')
user_month = user_month.merge(internet_per_month, on=['user_id', 'month'], how='left')

# Replace NaNs with zeros (no activity in that month)
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
    revenue = row['usd_monthly_pay']
    
    # Extra minutes
    extra_minutes = max(0, row['total_minutes'] - row['minutes_included'])
    revenue += extra_minutes * row['usd_per_minute']
    
    # Extra messages
    extra_messages = max(0, row['messages_count'] - row['messages_included'])
    revenue += extra_messages * row['usd_per_message']
    
    # Extra data (MB) converted to GB, with month total rounded up
    extra_mb = max(0, row['mb_used'] - row['mb_per_month_included'])
    if extra_mb > 0:
        extra_gb = int(np.ceil(extra_mb / 1024))
    else:
        extra_gb = 0
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

# Convert month to string for plotting
calls_stats['month'] = calls_stats['month'].astype(str)

months = sorted(calls_stats['month'].unique())
plans_list = calls_stats['plan'].unique()

x = np.arange(len(months))
width = 0.35

plt.figure(figsize=(12, 6))

for i, p in enumerate(plans_list):
    subset = calls_stats[calls_stats['plan'] == p]
    plt.bar(x + i*width, subset['mean_minutes'], width=width, label=p.capitalize())

plt.xticks(x + width / 2, months, rotation=45)
plt.xlabel('Month')
plt.ylabel('Average minutes per user')
plt.title('Average monthly call minutes per user by plan')
plt.legend()
plt.tight_layout()
plt.show()


# Compare the number of minutes users of each plan require each month. Plot a histogram.

plt.figure(figsize=(12, 5))

plans_list = user_month['plan'].unique()

for i, p in enumerate(plans_list, 1):
    plt.subplot(1, 2, i)
    subset = user_month[user_month['plan'] == p]['total_minutes']
    plt.hist(subset, bins=20, alpha=0.7, color='steelblue', edgecolor='black')
    plt.title(f'Monthly minutes distribution: {p.capitalize()}')
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

data_to_plot = [
    user_month[user_month['plan'] == p]['total_minutes']
    for p in plans_list
]

plt.figure(figsize=(8, 6))
plt.boxplot(data_to_plot, labels=[p.capitalize() for p in plans_list])
plt.title('Monthly call minutes per user by plan')
plt.xlabel('Plan')
plt.ylabel('Total minutes per month')
plt.show()


# Compare the number of messages users of each plan tend to send each month

plt.figure(figsize=(12, 5))

for i, p in enumerate(plans_list, 1):
    plt.subplot(1, 2, i)
    subset = user_month[user_month['plan'] == p]['messages_count']
    plt.hist(subset, bins=20, alpha=0.7, color='darkorange', edgecolor='black')
    plt.title(f'Monthly messages distribution: {p.capitalize()}')
    plt.xlabel('Messages')
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()


# Compare the amount of internet traffic consumed by users per plan
plt.figure(figsize=(12, 5))

plans_list = user_month['plan'].unique() 

for i, p in enumerate(plans_list, 1): 
    plt.subplot(1, 2, i) 
    subset = user_month[user_month['plan'] == p]['mb_used'] 
    plt.hist(subset, bins=20, alpha=0.7, color='purple', edgecolor='black') 
    plt.title(f'Internet Traffic Distribution: {p.capitalize()}') 
    plt.xlabel('MB Used') 
    plt.ylabel('Frequency') 
    
plt.tight_layout() 
plt.show()



# Test the hypotheses: average revenue from users of Ultimate and Surf calling plans differs.

surf_revenue = user_month[user_month['plan'] == 'surf']['revenue']
ultimate_revenue = user_month[user_month['plan'] == 'ultimate']['revenue']

alpha = 0.05  # you can adjust this if you want

results_plans = st.ttest_ind(
    surf_revenue,
    ultimate_revenue,
    equal_var=False  # Welch's t-test (safer if variances differ)
)

print('T-statistic:', results_plans.statistic)
print('p-value:', results_plans.pvalue)

if results_plans.pvalue < alpha:
    print("We reject the null hypothesis: average revenue differs between Surf and Ultimate.")
else:
    print("We can't reject the null hypothesis: no significant difference detected.")


# Test the hypotheses: average revenue from users in NY-NJ area is different from other regions.

ny_nj_revenue = user_month[user_month['is_ny_nj'] == True]['revenue']
other_revenue = user_month[user_month['is_ny_nj'] == False]['revenue']

alpha = 0.05  # same or different alpha, your choice

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



'''
What to say in your analysis section
You can write something like:
“Ultimate users consumed significantly more internet traffic on average than Surf users. The histogram shows a wider and higher‑usage distribution for Ultimate, while Surf users cluster closer to the 15 GB included limit. The boxplot confirms that Ultimate users have a higher median and greater variability in data usage.”'''

