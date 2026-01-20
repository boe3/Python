#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 4: Filtering Data
#Lesson 1: Indexes in DataFrames and Series


import pandas as pd

states  = ['Alabama', 'Alaska', 'Arizona', 'Arkansas']
flowers = ['Camellia', 'Forget-me-not', 'Saguaro cactus blossom', 'Apple blossom']
insects = ['Monarch butterfly', 'Four-spotted skimmer dragonfly', 'Two-tailed swallowtail', 'European honey bee']
index   = ['state 1', 'state 2', 'state 3', 'state 4']

df = pd.DataFrame({'state': states, 'flower': flowers, 'insect': insects}, index=index)

#Task 1
#Practice using loc[] in this way to get only the 'flower' and 'insect' columns for Alabama and Arizona. Your code should return another DataFrame. Print the result.
print('Task 1')
print(df.loc[['state 1', 'state 3'], ['flower', 'insect']])
print()

#Task 2
#This time, use loc[] to get just the 'insect' column for all states except Alabama. Your code should return a Series. Print the result.
print('Task 2')
print(df.loc[['state 2', 'state 3', 'state 4'], 'insect'])
print()

#Reference
print('Reference')
print(df)
print()

print('One cell')
print(df.loc['state 3', 'flower'])
print()

print('One column')
print(df.loc[:, 'state'])
print()

print('Multiple columns')
print(df.loc[:, ['flower', 'insect']])
print()

print('Multiple consecutive columns (slice)')
print(df.loc[:, 'state': 'insect'])
print()

print('One row')
print(df.loc['state 1'])
print()

print('All rows, starting with the given row')
print(df.loc['state 2':])
print()

print('All rows, up to the given row')
print(df.loc[:'state 3'])
print()

print('Multiple consecutive rows (slice)')
print(df.loc['state 2': 'state 4'])
print()
