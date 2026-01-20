# Sprint 4: Statisttical Data Analysis
# Chapter 2: Probability Theory
# Lesson 5: Expected Value and Variance


import numpy as np

# The probability that a python's sign will belong to any one of the 4 elements is 1/4.
# We need to add the probabilities of 2 elemental signs (Fire and Earth) in order to get the probability
# of a python weighing 3 kg. For the other elements, the probability stays at 1/4.

# dictionary creation and calculation code
weight_probs = {
    '2': 0.25,
    '3': 0.5,
    '5': 0.25,
}

expectation = 0
expected_of_square = 0
square_of_expected = 0

for x_i in weight_probs:
    expectation += int(x_i)*weight_probs[x_i]

for x_i in weight_probs:
    expected_of_square += int(x_i)*int(x_i)*weight_probs[x_i]

square_of_expected = expectation ** 2

variance = expected_of_square - square_of_expected

print("Task 2")
print('Expected value:', expectation)
print('Variance:', variance)
print()