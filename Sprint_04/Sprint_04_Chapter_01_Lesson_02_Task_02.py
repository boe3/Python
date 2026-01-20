# Sprint 4: Statisttical Data Analysis
# Chapter 1: Descriptive Statistics
# Lesson 2: Frequency Histograms for Continuous Variablees

import pandas as pd

# the pur_time (purchase time) dataset
pur_time = pd.Series([36, 44, 73, 32, 44, 29, 63, 60, 55, 74, 61, 26, 76, 40, 39, 28, 69, 61, 54, 58, 47, 41, 70, 51, 58, 36, 71, 47, 74, 59, 50, 78, 59, 48, 67, 53, 67, 52, 38, 55, 53, 53, 43, 77, 44, 63, 63, 54])

# Task 02
pur_time.hist(bins=[15, 35, 55, 75, 90], alpha=0.5)

pur_time.hist(bins=[15, 45, 55, 90], alpha=0.5)