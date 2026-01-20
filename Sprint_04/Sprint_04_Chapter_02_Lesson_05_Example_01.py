# Sprint 4: Statisttical Data Analysis
# Chapter 2: Probability Theory
# Lesson 5: Expected Value and Variance


import numpy as np

x_probs = {
    '3': 0.1,
    '4': 0.2,
    '5': 0.2,
    '7': 0.3,
    '11': 0.1,
    '16': 0.05,
    '18': 0.05    
}
# E(X): For each dictionary element, we calculate the product of the probability and the value
# of the random variable (the integer representation of the dictionary key), then add it all up:

expectation = 0

for x_i in x_probs:
    expectation += int(x_i)*x_probs[x_i]

print(expectation)