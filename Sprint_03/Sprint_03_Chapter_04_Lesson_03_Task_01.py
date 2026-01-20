#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 4: Filtering Data
#Lesson 2: Using External Data Structures to Filter DataFrames

import pandas as pd

our_series = pd.Series([10, 11, 12], index=['X', 'Y', 'T'])
df = pd.DataFrame(
    {
        'a': [2, 3, 10, 11, 12],
        'b': [5, 4, 3, 2, 1],
        'c': ['X', 'Y', 'Y', 'Y', 'Z'],
    }
)

print(df.query("c in @our_series.index"))