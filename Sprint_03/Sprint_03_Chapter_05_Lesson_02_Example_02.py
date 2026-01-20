#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 5: Data Types
#Lesson 2: Working with Numeric and String Data Types

import numpy as np
import pandas as pd

d = {'col1': [1.0, 2.0, 3.0, 4.0], 'col2': [5.0, 6.01, 7.0, 8.0]}
df = pd.DataFrame(data=d)

#Example 1
print('Example 1:')
print(df)
print()

#Example 2
print('Example 2:')
#check if converting 'col1' is safe
#np.array_equal(df['col1'], df['col1'].astype('int'))
print(np.array_equal(df['col1'], df['col1'].astype('int'))) #Task 1
print()