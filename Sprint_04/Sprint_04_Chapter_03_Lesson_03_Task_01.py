# Sprint 4: Statisttical Data Analysis
# Chapter 3: Testing Hypotheses
# Lesson 3: Formulating One-Tailed Hypotheses


from scipy import stats as st
import numpy as np
import pandas as pd

revenue = pd.Series([727, 678, 685, 669, 661, 705, 701, 717, 
                     655,643, 660, 709, 701, 681, 716, 655, 
                     716, 695, 684, 687, 669,647, 721, 681, 
                     674, 641, 704, 717, 656, 725, 684, 665])

# how much did Robby Tobbinson promise?
interested_value = 800

# indicate the statistical significance level
alpha = 0.05

# use the method st.ttest_1samp
results = st.ttest_1samp(revenue, interested_value) 

# print the p-value for a one-sided test
print("Task 1")
print('p-value:', results.pvalue / 2)

# compare the value you get and the critical statistical significance level
# and check to see if the sample mean is on the correct side of interested_value
if (results.pvalue < alpha) and (revenue.mean() < interested_value): 
    print("We reject the null hypothesis: revenue was significantly lower than 800 dollars") 
else: 
    print("We can't reject the null hypothesis: revenue wasn't significantly lower")
print()