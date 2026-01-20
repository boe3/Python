# Sprint 4: Statisttical Data Analysis
# Chapter 3: Testing Hypotheses
# Lesson 4: Hypothesis on the Equality of the Means of Paired Samples


from scipy import stats as st
import numpy as np

time_before = [1732, 1301, 1540, 2247, 1632, 1550, 754, 1946, 1889, 
          2748, 1349, 1648, 1665, 2416, 1470, 1681, 1868, 1629, 
          1271, 1633, 2131, 942, 1599, 1127, 2200, 661, 1207, 
          1737, 2410, 1486]

time_after = [955, 2577, 360, 139, 1618, 990, 644, 1796, 1487, 949, 472, 
         1906, 1758, 1258, 2554, 612, 309, 1864, 1294, 1487, 1164, 1559, 
         491, 2286, 1270, 2069, 1553, 1629, 1704, 1623]

# your code: set a critical statistical significance level
alpha = 0.05

# your code: conduct the test and calculate the p-value
results = st.ttest_rel(time_before, time_after)

# your code: print the p-value you get
print("Task 1")
print('p-value:', results.pvalue)

# your code: compare the p-value to the statistical significance level
if results.pvalue < alpha:
    print("We reject the null hypothesis")
else:
    print("We can't reject the null hypothesis")
print()