#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 5: Data Types
#Lesson 3: Working with Dates and Times

import pandas as pd

#We've received a new dataset from our colleagues. The data is stored in a file called position.csv and it contains data on search engine rankings for the past three months. Read the CSV file and store it in a variable called position. Print the first fifteen rows.
position = pd.read_csv('/datasets/position.csv')
print(position.head(15))

