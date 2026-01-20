#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 6: Feature Engineering
#Lesson 3: Creating Categories with Row Functions

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')
df.dropna(inplace=True)

# Task 2
# Now it’s time to test your new function. Create three custom rows with the following variable names and values:
# row_1 — critic score of 66 and user score of 3.6
# row_2 — critic score of 72 and user score of 8.1
# row_3 — critic score of 99 and user score of 9.4
# Each of the row variables must be a Series object with index values 'critic_score' and 'user_score' so that avg_score_group() can extract the correct values.
# The precode defines the avg_score_group() function from the last task, although it may look different from your solution. Your task here is to print the result of calling avg_score_group() with each of the three inputs above.

def avg_score_group(row):
    critic_score = row['critic_score']
    user_score = row['user_score']
    
    avg_score = (critic_score + user_score * 10) / 2
    
    if avg_score < 60:
        return 'low'
    if avg_score < 80:
        return 'medium'
    if avg_score >= 80:
        return 'high'

# create the test input rows here
row_1 = pd.Series({'critic_score': 66, 'user_score': 3.6})
row_2 = pd.Series({'critic_score': 72, 'user_score': 8.1})
row_3 = pd.Series({'critic_score': 99, 'user_score': 9.4}) 

# print results of calling the function with the test inputs in order
print(avg_score_group(row_1))
print(avg_score_group(row_2))  
print(avg_score_group(row_3))

