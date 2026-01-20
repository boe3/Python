# Sprint 4: Statisttical Data Analysis
# Chapter 3: Testing Hypotheses
# Lesson 3: Formulating One-Tailed Hypotheses


from scipy import stats as st
import pandas as pd

screens = pd.Series([4, 2, 4, 5, 5, 4, 2, 3, 3, 5, 2, 5, 2, 2, 2, 3, 3, 4, 8, 3, 4, 3, 5, 5, 4, 2, 5, 2, 3, 7, 5, 5, 6,  5, 3, 4, 3, 6, 3, 4, 4, 3, 5, 4, 4, 8, 4, 7, 4, 5, 5, 3, 4, 6, 7, 2, 3, 6, 5, 6, 4, 4, 3, 4, 6, 4, 4, 6, 2, 6, 5, 3, 3, 3, 4, 5, 3, 5, 5, 4, 3, 3, 3, 1, 5, 4, 3, 4, 6, 3, 1, 3, 2, 7, 3, 6, 6, 6, 5, 5])

prev_screens_value = 4.867

alpha = 0.05  # critical statistical significance level

results = st.ttest_1samp(screens, prev_screens_value)

# one-sided test: p-value will be halved
print('p-value: ', results.pvalue / 2)
print()

# one-sided test to the left:
# reject the hypothesis only if the sample mean is significantly less than the predicted value
print("Example 1")
if (results.pvalue / 2 < alpha) and (screens.mean() < prev_screens_value):
    print("We reject the null hypothesis")
else:
    print("We can't reject the null hypothesis")
print()

print("Example 2")
if (results.pvalue / 2 < alpha) and (screens.mean() > prev_screens_value):
    print("We reject the null hypothesis")
else:
    print("We can't reject the null hypothesis")
print()