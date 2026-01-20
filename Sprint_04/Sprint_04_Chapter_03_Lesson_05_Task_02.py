# Sprint 4: Statisttical Data Analysis
# Chapter 3: Testing Hypotheses
# Lesson 4: Hypothesis on the Equality of Two Population Means


from scipy import stats as st
import numpy as np
import pandas as pd

bullets_before = [821, 1164, 598, 854, 455, 1220, 161, 1400, 479, 215, 
          564, 159, 920, 173, 276, 444, 273, 711, 291, 880, 
          892, 712, 16, 476, 498, 9, 1251, 938, 389, 513]

bullets_after = [904, 220, 676, 459, 299, 659, 1698, 1120, 514, 1086, 1499, 
         1262, 829, 476, 1149, 996, 1247, 1117, 1324, 532, 1458, 898, 
         1837, 455, 1667, 898, 474, 558, 639, 1012]

print("Task 2")
print('mean before:', pd.Series(bullets_before).mean())
print('mean after:', pd.Series(bullets_after).mean())

alpha = 0.05 # your code: set a critical statistical significance level

results = st.ttest_rel(bullets_before, bullets_after)

# your code: print the p-value you get
print('p-value:', results.pvalue / 2)

if results.pvalue < alpha:
    print("We reject the null hypothesis")
else:
    print("We can't reject the null hypothesis")
print()