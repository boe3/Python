#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 4: Filtering Data
#Lesson 2: Using External Data Structures to Filter DataFrames

import pandas as pd

our_list = [2, 5, 10]
df = pd.DataFrame(
    {
        'a': [2, 3, 10, 11, 12],
        'b': [5, 4, 3, 2, 1],
        'c': ['X', 'Y', 'Y', 'Y', 'Z'],
    }
)
print(df)
print()
print(our_list)
print()
print(df.query("a in @our_list"))
print(df.query("b in @our_list"))

