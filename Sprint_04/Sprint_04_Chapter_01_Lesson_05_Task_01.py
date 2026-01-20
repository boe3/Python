# Sprint 4: Statisttical Data Analysis
# Chapter 1: Descriptive Statistics
# Lesson 2: Frequency Histograms for Continuous Variablees

import pandas as pd

data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mean_value = data.mean() # write your code here: find the mean value in the dataset
spacing_all = data - mean_value # write your code here: for each element in the dataset, find its distance to the mean
spacing_all_mean = spacing_all.mean() # write your code here: calculate the average distance

# print("Mean")
# print(mean_value)
# print("Distance to Mean")
# print(spacing_all)
# print("Average Distance to Mean")
print(spacing_all_mean)