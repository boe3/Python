#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 5: Data Types
#Lesson 3: Working with Dates and Times

import pandas as pd

#Task 1
#We've received a new dataset from our colleagues. The data is stored in a file called position.csv and it contains data on search engine rankings for the past three months. Read the CSV file and store it in a variable called position. Print the first fifteen rows.
position = pd.read_csv('/datasets/position.csv')
print(position.head(15))

#Task 2
#Take a look at the data's general information by calling the info() method on position.
position.info()

#Task 3
#Process the time data in the 'timestamp' column by converting it from string to datetime. Then, print the first five rows in the position table.
position['timestamp'] = pd.to_datetime(position['timestamp'], format='%Y-%m-%dT%H:%M:%S')
print(position.head())