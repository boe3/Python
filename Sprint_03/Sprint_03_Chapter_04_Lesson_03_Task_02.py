#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 4: Filtering Data
#Lesson 2: Using External Data Structures to Filter DataFrames

import pandas as pd

df = pd.DataFrame(
    {
        'a': [2, 3, 10, 11, 12],
        'b': [5, 4, 3, 2, 1],
        'c': ['X', 'Y', 'Y', 'Y', 'Z'],
    }
)
our_df = pd.DataFrame(
    {
        'a1': [2, 4, 6],
        'b1': [3, 2, 2],
        'c1': ['A', 'B', 'C'],
    },
    index=['Z', 'X', 'P']
)

print(df.query("a in @our_df.b1"))