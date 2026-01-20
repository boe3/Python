#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 7: Data Transformations
#Lesson 2: Pivot Tables

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')
df = df[df['year_of_release'] >= 2000]

df.user_score = pd.to_numeric(df.user_score, errors='coerce')



# Task 1
# We’ve filtered the video game dataset so that it only contains games that were released in the year 2000 or later. Create a pivot table from the filtered dataset that contains the average user score for every combination of genre and release year.
# Make the pivot table index values correspond to the genres and the columns correspond to the release year. The values you want to aggregate are the user scores, and the aggregation function you want to use is the mean.
# Assign the result to a variable called df_pivot, then print it.

# write your code here
df_pivot = pd.pivot_table(df, values='user_score', index='genre', columns='year_of_release', aggfunc='mean')
print(df_pivot)
    