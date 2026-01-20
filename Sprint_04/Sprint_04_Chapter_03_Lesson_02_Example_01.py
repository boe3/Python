# Sprint 4: Statisttical Data Analysis
# Chapter 3: Testing Hypotheses
# Lesson 1: Formulating Two-Tailed Hypotheses


from scipy import stats as st
import numpy as np
import pandas as pd

time_on_site = pd.read_csv('datasets/user_time.csv')

interested_value = 120

alpha = 0.05  # critical statistical significance

results = st.ttest_1samp(time_on_site, interested_value)
print("Example 1")
print('p-value: ', results.pvalue)

if results.pvalue < alpha:
    print('We reject the null hypothesis')
else:
    print("We can't reject the null hypothesis")

print()