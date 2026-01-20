#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 2: Working with Missing and Duplicate Values


#Lesson 1: Counting Missing Values
#[Method 1] Using the info() Method
import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')

df_logs.info()


#[Method 2] Using isna().sum()
import pandas as pd

    # Load the dataset
df_logs = pd.read_csv('/datasets/visit_log.csv')

    # Count missing values in each column
print(df_logs.isna().sum())


#[Method 3] Counting missing values with value_counts()
import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')
print(df_logs['source'].value_counts(dropna=False))


#Task 1
import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')

    #Filter the df_logs DataFrame so that it only contains rows where there is not a missing value in the 'email' column. 
df_emails = df_logs[~df_logs['email'].isna()]
print(df_emails.head(10))


#Task 2
import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')

    #Filter df_logs on the condition that both the 'email' column and the 'source' column have missing values. 
df_emails = df_logs[df_logs['email'].isna() & df_logs['source'].isna()]
print(df_emails)


#Lesson 2: Filling in Missing Categorical Values
#Quiz !: Filling Missing Values
import pandas as pd
df_logs = pd.read_csv('/datasets/visit_log.csv')

df_logs['email'] = df_logs['email'].fillna(value='')
print(df_logs.head())


#Lesson 3: Filling in Missing Categorical Values
#Dataset Overview
import pandas as pd

analysis_data = pd.read_csv('/datasets/web_analysis_data.csv')
print(analysis_data.head(10))


#Wy the median?
import pandas as pd

    # Example DataFrame
data = {'Salary': [30000, 30000, 30000, 30000, 900000]}
df = pd.DataFrame(data)

    # Calcuate the median
median_salary = df['Salary'].median()
print("Median Salary:", median_salary)


#Task
import pandas as pd

    # Load the dataset
analytics_data = pd.read_csv('/datasets/web_analytics_data.csv')

    # Calculate the median of the 'age' column
age_median = analytics_data['age'].median()
#print("Median age:", age_median)

analytics_data['age'] = analytics_data['age'].fillna(value=age_median)

analytics_data.info()
