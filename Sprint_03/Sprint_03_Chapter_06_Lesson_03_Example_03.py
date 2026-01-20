#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 6: Feature Engineering
#Lesson 3: Creating Categories with Row Functions

import pandas as pd

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


cols = ['year_of_release', 'na_sales', 'eu_sales', 'jp_sales']

row_1 = pd.Series([1989, 0, 0, 0.6], index=cols) # expect 'retro'
row_2 = pd.Series([1989, 1, 2, 0], index=cols)   # expect 'classic'
row_3 = pd.Series([2006, 0.3, 0, 0], index=cols) # expect 'modern'
row_4 = pd.Series([2020, 0, 0.4, 0], index=cols) # expect 'recent'
row_5 = pd.Series([2020, 1, 1, 1], index=cols)   # expect 'big hit'

print(row_1, row_2, row_3, row_4, row_5, sep='\n\n')
print()

rows = [row_1, row_2, row_3, row_4, row_5]

for row in rows:
    print(era_sales_group(row))



