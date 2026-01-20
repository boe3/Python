#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 4: Filtering Data
#Lesson 2: Using External Data Structures to Filter DataFrames

import pandas as pd
#Filter df so that you only get games that were released in the 1980s. Assign the result to a variable called df_filtered and then print the first 5 rows.
df = pd.read_csv('/datasets/vg_sales.csv')
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')

df_filtered = df[(df['year_of_release'] >= 1980) & (df['year_of_release'] < 1990)]
print(df_filtered.head())