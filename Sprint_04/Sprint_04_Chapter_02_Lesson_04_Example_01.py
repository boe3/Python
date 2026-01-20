# Sprint 4: Statisttical Data Analysis
# Chapter 2: Probability Theory
# Lesson 4: Random Numbers, Probability Distributions, and Value Intervals

import numpy as np

spots = np.array(
    [
        [2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8],
        [4, 5, 6, 7, 8, 9],
        [5, 6, 7, 8, 9, 10],
        [6, 7, 8, 9, 10, 11],
        [7, 8, 9, 10, 11, 12],
    ]
)

spot_counts = {}

for i in range(0, 6):
    for j in range(0, 6):
        if spots[i][j] not in spot_counts.keys():
            spot_counts[spots[i][j]] = 1
        else:
            spot_counts[spots[i][j]] += 1
print(spot_counts)


spot_probs = {}
for k in spot_counts:
    spot_probs[k] = spot_counts[k]/36
print(spot_probs)
