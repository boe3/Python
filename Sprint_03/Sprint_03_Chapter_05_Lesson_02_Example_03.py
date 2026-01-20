#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 5: Data Types
#Lesson 2: Working with Numeric and String Data Types

import pandas as pd

d = {'col1': ['1.0', '2.0'], 'col2': ['3', '4']}
df = pd.DataFrame(data=d)

print('Example 1:')
# convert col2 to int
df['col2'] = df['col2'].astype(int)
df['col1'] = pd.to_numeric(df['col1'])
print(df.dtypes)
print()



