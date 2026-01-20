# Sprint 4: Statisttical Data Analysis
# Chapter 3: Testing Hypotheses
# Lesson 4: Hypothesis on the Equality of the Means of Paired Samples


from scipy import stats as st
import numpy as np

before = [157, 114, 152, 355, 155, 513, 299, 268, 164, 320, 
                    192, 262, 506, 240, 364, 179, 246, 427, 187, 431, 
                    320, 193, 313, 347, 312, 92, 177, 225, 242, 312]

after = [282, 220, 162, 226, 296, 479, 248, 322, 298, 418, 
                 552, 246, 251, 404, 368, 484, 358, 264, 359, 410, 
                 382, 350, 406, 416, 438, 364, 283, 314, 420, 218]

alpha = 0.05  # critical statistical significance level

results = st.ttest_rel(before, after)

print("Example 1")
print('p-value: ', results.pvalue)

if results.pvalue < alpha:
    print("We reject the null hypothesis")
else:
    print("We can't reject the null hypothesis")
print()