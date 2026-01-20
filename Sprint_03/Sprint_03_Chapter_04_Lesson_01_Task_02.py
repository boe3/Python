#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 4: Filtering Data
#Lesson 1: Indexes in DataFrames and Series

import pandas as pd

#Example 10: Changing a DataFrame index using set_index() method
states  = ['Alabama', 'Alaska', 'Arizona', 'Arkansas']
flowers = ['Camellia', 'Forget-me-not', 'Saguaro cactus blossom', 'Apple blossom']
insects = ['Monarch butterfly', 'Four-spotted skimmer dragonfly', 'Two-tailed swallowtail', 'European honey bee']
index   = ['state 1', 'state 2', 'state 3', 'state 4']

df = pd.DataFrame({'state': states, 'flower': flowers, 'insect': insects}, index=index)
df = df.set_index('state')

#Task 1
#Use loc[] to print out the flowers for Alabama, Alaska, and Arizona. The precode already creates the DataFrame for you and sets the 'state' column as the index, so make sure to use the state names as the index values in loc[].
print('Task 1')
print(df.loc[['Alabama', 'Alaska', 'Arizona'], 'flower'])
print()

#Task 2
#Now use iloc[] to index the exact same part of the DataFrame you did in the last task.
print('Task 2')
print(df.iloc[0:3, 0])
print()