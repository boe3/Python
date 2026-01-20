#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 7: Data Transformations
#Lesson 4: Processing Grouped data with merge()

import pandas as pd

# Task 1
# read data
df_members = pd.read_csv('/datasets/new_members.csv')
df_orders = pd.read_csv('/datasets/recent_orders.csv')

# display data
print(df_members)
print()
print(df_orders)

# Task 2
# Each row of the df_orders table represents one service order. Notice how that table has a 'user_id' column that records which customer placed each order. Your task is to merge the two tables so that you only end up with customers who’ve actually placed an order.
# Think about what type of merge you need to do this. Use df_members as your left DataFrame and df_orders as your right DataFrame. The column you need to merge on from df_members is 'id', and from df_orders you need to merge on 'user_id'. Also, include the suffixes '_member' (left) and '_order' (right) in your merged DataFrame.
# Assign the merge to a variable called df_merged, then print it. Don’t drop any columns for now.
df_merged = df_members.merge(df_orders, left_on='id', right_on='user_id', suffixes=['_member', '_order'])
print(df_merged)

# Task 3
# Clean things up a bit by by dropping the duplicate 'user_id' column from the merged DataFrame using the drop() method. Assign the result back to df_merged, then print it.
df_merged = df_merged.drop('user_id', axis='columns')
print(df_merged)













#