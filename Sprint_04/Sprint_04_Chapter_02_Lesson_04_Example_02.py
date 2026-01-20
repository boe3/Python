# Sprint 4: Statisttical Data Analysis
# Chapter 2: Probability Theory
# Lesson 4: Random Numbers, Probability Distributions, and Value Intervals

import pandas as pd

spots = pd.array(
    [
        [2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8],
        [4, 5, 6, 7, 8, 9],
        [5, 6, 7, 8, 9, 10],
        [6, 7, 8, 9, 10, 11],
        [7, 8, 9, 10, 11, 12],
    ]
)

# This example did not work???
pd.Series(spots.reshape(36)).hist(density=True,bins=11)
