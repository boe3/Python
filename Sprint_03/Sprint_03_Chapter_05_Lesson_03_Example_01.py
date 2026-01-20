#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 5: Data Types
#Lesson 3: Working with Dates and Times

import pandas as pd

string_date = '2010-12-17T12:38:00Z'
datetime_date = pd.to_datetime(string_date, format='%Y-%m-%dT%H:%M:%SZ')

print('Formatting datetme values')
print(type(string_date))
print(type(datetime_date))
print(datetime_date)
print()


