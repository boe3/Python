# Sprint 4: Statisttical Data Analysis
# Chapter 1: Descriptive Statistics
# Lesson 4: Measures of Location

import pandas as pd

data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Example 1")
print('The mean is', data.mean())
print('The median is', data.median())
print()


data_new = pd.Series([0, 0.1, 0.2, 0.3, 0.4, 5, 60, 70, 80, 90, 100])
print("Example 2")
print('The new mean is', data_new.mean())
print('The new median is', data_new.median())
print()
