#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 1: Reading and Viewing Data


#Lesson 1: Fixing Issues with CSV Files
#Task 1
import pandas as pd

df = pd.read_csv('/datasets/letters_colors_decimals.csv',sep='$',decimal='a',)

print(df.head())


#Lesson 2: How to Read Excel Files
#Task 1
import pandas as pd

df_categories = pd.read_excel('/datasets/product_reviews.xlsx', sheet_name='product_categories')

print(df_categories.head())


#Lesson 3: Looking at Our Data
#Task 1
import pandas as pd

column_names = [
    'country',
    'name',
    'capacity_mw',
    'latitude',
    'longitude',
    'primary_fuel',
    'owner'
]
data = pd.read_csv(
    '/datasets/gpp_modified.csv',
    sep='|',
    header=None,
    names=column_names,
    decimal=',',
)

print(data.head())
print()

print(data.sample(5, random_state=543210))


#Lesson 4: Numerical Descriptions and desbribe()
#Task 1
import pandas as pd

column_names = [
    'country',
    'name',
    'capacity_mw',
    'latitude',
    'longitude',
    'primary_fuel',
    'owner'
]
data = pd.read_csv(
    '/datasets/gpp_modified.csv',
    sep='|',
    header=None,
    names=column_names,
    decimal=',',
)

print(data['primary_fuel'].describe())


