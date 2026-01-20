#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 4: Filtering Data
#Lesson 1: Indexes in DataFrames and Series

import pandas as pd

oceans = pd.Series(['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic'])

print('Example 1: The index attribute')
print(oceans)
print()

print('Example 2: The index attribute')
print(oceans.index)
print(type(oceans.index))
print()

print('Example 3: The index attribute')
oceans.index = [1, 2, 3, 4, 5]
print(oceans.index)
print(type(oceans.index))
print()
