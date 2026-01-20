#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 7: Data Transformations
#Lesson 4: Processing Grouped data with agg()

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales']

grp = df.groupby('genre')

# It's time we take a detailed look at the video game sales for each genre!
# The precode creates a 'total_sales' column like you’ve done previously and groups df by the 'genre' column, assigning the grouped object to the grp variable.
# Use grp and agg() to calculate for each genre:
# Total sales
# Average NA sales
# Average EU sales
# Average JP sales
# Use strings for the aggregate function names in your dictionary, and assign the dictionary to a variable called agg_dict.
# Assign the result of agg() to a variable called genre. Then print genre.
# write your code here
agg_dict = {
    'total_sales': 'sum',
    'na_sales': 'mean',
    'eu_sales': 'mean',
    'jp_sales': 'mean'
}
genre = grp.agg(agg_dict)
print(genre)
    