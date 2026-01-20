#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 6: Feature Engineering
#Lesson 2: Creating Category Columns with apply()

import pandas as pd
import numpy as np

df = pd.read_csv('vg_sales.csv')

# take another look at the 'year_of_release' column from the video game dataset
print(df['year_of_release'].min(), df['year_of_release'].max())

# sort our result by the index values so that it’s in chronological order
df['year_of_release'].value_counts().sort_index()

# custom fumction to group our games into four categories of era 
def era_group(year):
    """
    The function returns the era group for games according to the year of release, using the following rules:
    —'retro'   for year < 2000
    —'modern'  for 2000 <= year < 2010
    —'recent'  for year >= 2010
    —'unknown' for missing year values (NaN)
    """

    if year < 2000:
        return 'retro'
    elif year < 2010:
        return 'modern'
    elif year >= 2010:
        return 'recent'
    else:
        return 'unknown'

print(era_group(1983))
print(era_group(2011))
print(era_group(2021))
print(era_group(np.nan))

# analyze the data on era groups with the value_counts() method
df['era_group'] = df['year_of_release'].apply(era_group)
print(df['era_group'].value_counts())


#Task 1
"""
import pandas as pd
import numpy as np

df = pd.read_csv('/datasets/vg_sales.csv')
"""
# write your function definition here
def score_group(score):
    if score < 60:
        return 'low'
    elif score < 80:
        return 'medium'
    elif score >= 80:
        return 'high'
    else:
        return 'no score'

# print results of calling the function with these inputs in order: 10, 65, 99, np.nan
print(score_group(10))
print(score_group(65))
print(score_group(99))
print(score_group(np.nan))

# Add a 'score_group' column to the df table by applying the score_group() function to the 'critic_score' column. Print the first 5 rows to make sure the new column was created correctly. 
# The precode contains the score_group() function from the last task (it may look slightly different from yours, but the functionality is the same).
df['score_group'] = df['critic_score'].apply(score_group)
print(df.head())
