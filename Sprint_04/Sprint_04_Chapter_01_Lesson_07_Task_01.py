# Sprint 4: Statisttical Data Analysis
# Chapter 1: Descriptive Statistics
# Lesson 7: Standard Deviation

import pandas as pd
import numpy as np

# Task 1
data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
variance = np.var(data)
print("Task 1")
print(variance)
print()

# Task 2
print("Task 2")
standard_dev = np.std(data)
print(standard_dev)
print()

# Task 3
adv_mean = 3
adv_var = 0.25
adv_std = np.sqrt(adv_var) # calculate standard deviation
adv_time = adv_mean + (3 * adv_std) # calculate the message display time
print("Task 3")
print("Message display time is", adv_time)
print()

# Task 4
bolt_mean = 10.0  # mm
bolt_std = 0.15   # mm

lower_bound = bolt_mean - (3 * bolt_std) # calculate the lower boundary 
upper_bound = bolt_mean + (3 * bolt_std) # calculate the upper boundary 
print("Task 4")
print(f"Acceptable range: {lower_bound:.2f} to {upper_bound:.2f} mm")
print()

