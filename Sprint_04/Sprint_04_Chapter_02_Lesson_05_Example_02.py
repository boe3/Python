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

expected = 0
expected_of_square = 0
square_of_expected = 0

# E(X) - expected value
for x_i in x_probs:
    expected += int(x_i)*x_probs[x_i]

# E(X^2) - expected value of squared random variable
for x_i in x_probs:
    expected_of_square += int(x_i)*int(x_i)*x_probs[x_i]

# E(X)^2 - square of expected value
square_of_expected = expected ** 2

variance = expected_of_square - square_of_expected
print(variance)