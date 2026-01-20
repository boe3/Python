# Sprint 4: Statisttical Data Analysis
# Chapter 2: Probability Theory
# Lesson 9: Normal Approximation to the Binomial Distribution


from scipy import stats as st
import pandas as pd

scooters = pd.Series([15, 31, 10, 21, 21, 32, 30, 25, 21,
28, 25, 32, 38, 18, 33, 24, 26, 40, 24, 37, 20, 36, 28, 38,
24, 35, 33, 21, 29, 26, 13, 25, 34, 38, 23, 37, 31, 28, 32,
24, 25, 13, 38, 34, 48, 19, 20, 22, 38, 28, 31, 18, 21, 24,
31, 21, 28, 29, 33, 40, 26, 33, 33,  6, 27, 24, 17, 28,  7,
33, 25, 25, 29, 19, 30, 29, 22, 15, 28, 36, 25, 36, 25, 29,
33, 19, 32, 32, 28, 26, 18, 48, 15, 27, 27, 27,  0, 28, 39,
27, 25, 39, 28, 22, 33, 30, 35, 19, 20, 18, 31, 44, 20, 18,
17, 28, 17, 44, 40, 33,])

# Proposed mean under H0
optimal_value = 30

# Significance level
alpha = 0.05

# Perform two-tailed one-sample t-test
results = st.ttest_1samp(scooters, optimal_value) 

print("Task 1")
print('p-value: ', results.pvalue)

# Decision rule
if results.pvalue < alpha:
    print('We reject the null hypothesis')
else:
    print("We can't reject the null hypothesis")
print()