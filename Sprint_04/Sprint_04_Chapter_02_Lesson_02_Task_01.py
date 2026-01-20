# Sprint 4: Statisttical Data Analysis
# Chapter 2: Probability Theory
# Lesson 2: The Law of Large Numbers

import random

random.seed(42) # method specifying the level of randomness; don't change parameter 42


def calculate_p(N):
    cnt_21_40 = 0
    for i in range(N):
        random_integer = random.randint(1, 100) # write your code here
        if 21 <= random_integer <= 40:
            cnt_21_40 += 1
    return cnt_21_40 / N

p_20 = calculate_p(20)
p_400 = calculate_p(400)
p_10000 = calculate_p(10000)

# print the probabilities separated by spaces
print("Task 1")
print(p_20, p_400, p_10000)
print()