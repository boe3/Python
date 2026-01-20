#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 5: Data Types
#Lesson 3: Working with Datetime Attributes and Timee Zones

import pandas as pd

#Task 1
# Add a 'month' column to the position table by using the 'timestamp' column to get the month number. Print the first five rows of the table after creating the 'month' column.
position = pd.read_csv('/datasets/position.csv')
position['timestamp'] = pd.to_datetime(position['timestamp'], format='%Y-%m-%dT%H:%M:%S')
position['month'] = position['timestamp'].dt.month
print(position.head())


#Task 2
#Using the 'timestamp' column, create a new column called 'ts_toronto' that contains all of the datetimes localized to the 'America/Toronto' time zone. Print the first 5 rows of your result.
#Don't change the precode that converts 'timestamp' to datetime.
position = pd.read_csv('/datasets/position.csv')
position['timestamp'] = pd.to_datetime(position['timestamp'], format='%Y-%m-%dT%H:%M:%S')
position['ts_toronto'] = position['timestamp'].dt.tz_localize('America/Toronto').dt.tz_convert('America/Toronto')
print(position.head())
