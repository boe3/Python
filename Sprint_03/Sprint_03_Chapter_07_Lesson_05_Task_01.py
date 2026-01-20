#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 7: Data Transformations
#Lesson 4: Processing Grouped data with agg()

import pandas as pd

# Task 1
# We’ve read in the data for you, created a 'total_sales' column, and calculated the total sales for each platform in the total_sales variable. Your task is to calculate the total number of publishers that made a game on each platform. Assign the result to a variable called num_pubs, then print it.

df = pd.read_csv('datasets/vg_sales.csv')
df['total_sales'] = df['NA_Sales'] + df['EU_Sales'] + df['JP_Sales']

total_sales = df.groupby('Platform')['total_sales'].sum()
num_pubs = df.groupby('Platform')['Publisher'].nunique()
print(num_pubs)

# Task 2
# Combine total_sales and num_pubs column-wise into one DataFrame called platforms using concat(). Change the column names in platforms to 'total_sales' and 'num_publishers', then print platforms
platforms = pd.concat([total_sales, num_pubs], axis=1)
platforms.columns = ['total_sales', 'num_publishers']
print(platforms)




