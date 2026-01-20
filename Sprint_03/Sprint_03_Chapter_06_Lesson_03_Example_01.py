#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 6: Feature Engineering
#Lesson 3: Creating Categories with Row Functions

import pandas as pd

df = pd.read_csv('datasets/vg_sales.csv')

# discard any rows with missing values
df.dropna(inplace=True)
df.info()

def era_sales_group(row):
    """
    The function returns a category for games according to the year of release and total sales, using the following rules:
    —'retro'   for year < 2000 and total sales < $1 million
    —'modern'  for 2000 <= year < 2010 and total sales < $1 million
    —'recent'  for year >= 2010 and total sales < $1 million
    —'classic' for year < 2010 and total sales >= $1 million
    —'big hit' for year >= 2010 and total sales >= $1 million
    """

    year = row['year_of_release']
    na_sales = row['na_sales']
    eu_sales = row['eu_sales']
    jp_sales = row['jp_sales']
    
    total_sales = na_sales + eu_sales + jp_sales
    
    if year < 2000:
        if total_sales < 1:
            return 'retro'
        else:
            return 'classic'
    if year < 2010:
        if total_sales < 1:
            return 'modern'
        else:
            return 'classic'
    if year >= 2010:
        if total_sales < 1:
            return 'recent'
        else:
            return 'big hit'

row = df.iloc[0] # use the first row as example input
print(row)
print()
print(era_sales_group(row))



