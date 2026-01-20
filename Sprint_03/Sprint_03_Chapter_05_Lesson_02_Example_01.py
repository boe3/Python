#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 5: Data Types
#Lesson 2: Working with Numeric and String Data Types

import pandas as pd

d = {'col1': [1.0, 2.0], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

#Example 1
print('Example 1:')
print(df)
print()
print('Output of df.info():')
df.info()
print()


# Example 2
print('Example 2:')
df_str_dtype = df.astype(str)
print(df_str_dtype)
df_str_dtype.info()
print()

# Example 3
print('Example 3:')
df['col1'] = df['col1'].astype('int')
print(df)
df.info()
print()
print(df.dtypes)
print()

