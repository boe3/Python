#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 4: Filtering Data
#Lesson 1: Indexes in DataFrames and Series

import pandas as pd

#Example 4: The index attribute
oceans = pd.Series(['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic'], index=[1, 2, 3, 4, 5])

print('Example 4: The index attribute')
print(oceans.index)
print(type(oceans.index))
print()


#Example 5: The index attribute
continents = pd.Series(['North America', 'South America', 'Europe', 'Asia', 'Africa'], index=['NA', 'SA', 'EU', 'AS', 'AF'])

print('Example 5: The index attribute')
print(continents)
print()
print(continents.index)
print(type(continents.index))
print()


#Example 6: Indexing using loc[]
states  = ['Alabama', 'Alaska', 'Arizona', 'Arkansas']
flowers = ['Camellia', 'Forget-me-not', 'Saguaro cactus blossom', 'Apple blossom']
insects = ['Monarch butterfly', 'Four-spotted skimmer dragonfly', 'Two-tailed swallowtail', 'European honey bee']
index   = ['state 1', 'state 2', 'state 3', 'state 4']

df = pd.DataFrame({'state': states, 'flower': flowers, 'insect': insects}, index=index)

print('Example 6: Indexing using loc[]')
print(df)
print()

#Example 7: Indexing using loc[]
print('Example 7: Indexing using loc[]')
print(df.loc['state 4', 'insect'])
print()

#Example 8: Indexing using iloc[]
print('Example 8: Indexing using loc[]')
print(df)
print()
print(df.iloc[3, 2])
print()

#Example 9: Indexing using iloc[]
print('Example 9: Indexing using loc[]')
print(df)
print()
print(df.iloc[[0, 2], 1:])
print()
#We can use -1 to select the last column, just like with Python lists.
print(df.iloc[1:, -1])
print()
print(df.iloc[1:4, 2])
print()
