#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 6: Feature Engineering
#Lesson 1: Creating New Columns Based on Values in Other Columns

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')

# View the first five rows of the DataFrame
print(df.head())

# create a 'total_sales' column, we have to generate it from the other columns
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales']
print(df['total_sales'].head())

# to get the share of total sales that are from the EU all we have to do is
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales']

df['eu_sales_share'] = df['eu_sales'] / df['total_sales']
print(df['eu_sales_share'].head())

# create a column that checks if the publisher is Nintendo
df['is_nintendo'] = df['publisher'] == 'Nintendo'
print(df['is_nintendo'].head())

# Ensure that we're comparing lower cases
print(df['platform'].str.lower().isin(['gb', 'wii']).head())

# unique values in the 'platform' column
print(df['platform'].unique())

# convert 'platform' from a string column to a categorical column using the astype() method
df['platform'] = df['platform'].astype('category')
print(df['platform'].head())

# Your task is to take the average of the 'critic_score' and  'user_score' columns and store it in a new column called 'average_score', then print the first five values in the new column.
# Note that user score and critic score are not on the same scale! We want the average score to be a floating-point value representing a score between 0 and 100, so you’ll need to rescale the user score accordingly before taking the average. Convert the 'user_score' column to a float, and then divide by 10 to rescale it.
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')
df['average_score'] = (df['critic_score'] + df['user_score'] * 10) / 2
print(df['average_score'].head())

