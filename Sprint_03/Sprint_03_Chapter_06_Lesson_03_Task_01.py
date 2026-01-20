#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 6: Feature Engineering
#Lesson 3: Creating Categories with Row Functions

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')
df.dropna(inplace=True)

# Task 1
# Write a function called avg_score_group() that has one parameter called row. The row parameter should be a pandas Series object. The function should calculate the average rating score for each game, then return a string that places each game in one of the following categories:
# A value of 'low' for average scores below 60
# A value of 'medium' for averages scores from 60 to 79, inclusive
# A value of 'high' for scores 80 and above
# To calculate the average score, avg_score_group() should extract values from row with column names 'critic_score' and 'user_score'. Don’t forget to multiply the user score by 10 before taking the average of the two scores.
# There is no output for this task, but we’ll test your function behind the scenes to make sure it works as intended.
# write your function definition here
def avg_score_group(row):
    critic_score = row['critic_score']
    user_score = row['user_score'] * 10
    avg_score = (critic_score + user_score) / 2
    if avg_score < 60:
        return 'low'
    elif 60 <= avg_score <= 79:
        return 'medium'
    else:
        return 'high'
    
    