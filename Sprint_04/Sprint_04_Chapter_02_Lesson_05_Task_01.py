# Sprint 4: Statisttical Data Analysis
# Chapter 2: Probability Theory
# Lesson 5: Expected Value and Variance


import numpy as np

x_probs = {
    '-4': 0.05,
    '-2': 0.25,
    '0': 0.1,
    '1': 0.1,
    '5': 0.1,
    '7': 0.05,
    '15': 0.35,
}
# code for your calculations
expectation = 0
expected_of_square = 0
square_of_expected = 0

for x_i in x_probs:
    expectation += int(x_i)*x_probs[x_i]

for x_i in x_probs:
    expected_of_square += int(x_i)*int(x_i)*x_probs[x_i]

square_of_expected = expectation ** 2

variance = expected_of_square - square_of_expected

print("Task 1")
print('Expected value:', expectation)
print('Variance:', variance)
print()
