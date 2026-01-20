# Sprint 4: Statisttical Data Analysis
# Chapter 2: Probability Theory
# Lesson 4: Random Numbers, Probability Distributions, and Value Intervals

import numpy as np

spot_matrix = np.array(
    [
        [10, 11, 12, 13, 14, 15],
        [11, 12, 13, 14, 15, 16],
        [12, 13, 14, 15, 16, 17],
        [13, 14, 15, 16, 17, 18],
        [14, 15, 16, 17, 18, 19],
        [15, 16, 17, 18, 19, 20],
    ]
)

spot_counts = {}
#loop code
for i in range(6): 
    for j in range(6): 
        value = spot_matrix[i][j] 
        if value not in spot_counts: 
            spot_counts[value] = 1 
        else: spot_counts[value] += 1

# dictionary code
spot_probs = {} 
total_outcomes = 36 # 6×6 matrix 
for k in spot_counts: 
    spot_probs[k] = spot_counts[k] / total_outcomes

print("Task 1")
for i in range(10, 21):
    print(i, spot_probs[i])
print()

print("Task 2")
sum_probs_one = sum(spot_probs.values())
sum_probs_one = int(sum_probs_one)
print(sum_probs_one)
print()
