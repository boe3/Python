# Sprint 4: Statisttical Data Analysis
# Chapter 2: Probability Theory
# Lesson 7: The Binomial Distribution

from matplotlib import pyplot as plt
from math import factorial


x = factorial(5)
print("Example 1")
print(x)
print()

c = factorial(14)/(factorial(3)*factorial(11))
print("Example 2")
print(c)
print()


n = 5
p = 0.5

distr = []

for k in range(0,n+1):
    choose = factorial(n)/(factorial(k) * factorial(n-k))
    prob = choose * p**k * (1-p)**(n-k) 
    distr.append(prob)
    
plt.bar(range(0,n+1), distr)

