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
print(df)
print()

df = df.set_index('state')

print('Example 10: Changing a DataFrame index using set_index() method')
print(df)
print()
print(df.index)
print()

print('Example 11: Changing a DataFrame index using set_index() method')
df.index.name = None
print(df)
print()
print(df.index)
print()