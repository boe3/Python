#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 4: Filtering Data
#Lesson 4

import pandas as pd

#We’ve provided you a list of companies in the developers variable. Filter df however you choose so that you only get games that meet the following conditions:

#Sold in all 3 regions (North America, Europe, and Japan)
#The Japanese sales were greater than the combined sales from North America and Europe
#The game developer is one of the companies in the developers list
#There is no column that explicitly says whether a game was sold in each region, but you can infer that a game was not sold in a region if its sales are 0 for that region.

#Use the cols variable to select only the 'name', 'developer', 'na_sales', 'eu_sales', and 'jp_sales' columns from the filtered DataFrame, and assign the result to a variable called df_filtered. Print the whole DataFrame.

df = pd.read_csv('/datasets/vg_sales.csv')
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')

developers = ['SquareSoft', 'Enix Corporation', 'Square Enix']
cols = ['name', 'developer', 'na_sales', 'eu_sales', 'jp_sales']
df_filtered = df[(df['na_sales'] > 0) & (df['eu_sales'] > 0) & (df['jp_sales'] > 0) & (df['jp_sales'] > df['na_sales'] + df['eu_sales']) & (df['developer'].isin(developers))][cols]
print(df_filtered)
