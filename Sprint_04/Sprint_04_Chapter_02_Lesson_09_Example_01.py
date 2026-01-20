# Sprint 4: Statisttical Data Analysis
# Chapter 2: Probability Theory
# Lesson 9: Normal Approximation to the Binomial Distribution

from matplotlib import pyplot as plt
from math import factorial
from scipy.stats import norm

# binomial distribution with n **= 50 and p = 0.8
p = 0.8
n = 50

binom = []
for k in range(0, n + 1):
    choose = float(factorial(n)) / (factorial(k) * factorial(n - k))
    prob = choose * p ** k * (1 - p) ** (n - k)
    binom.append(prob)

# normal distribution with n **= 50 and p = 0.8
mu = n * p
var = n * p * (1 - p)
sigma = var ** 0.5

x = range(0, n + 1)
norm = norm.pdf(x, mu, sigma)

plt.bar(range(25, n + 1), binom[25:], alpha=0.3)
plt.plot(range(25, n + 1), norm[25:], 'g-')
plt.show()