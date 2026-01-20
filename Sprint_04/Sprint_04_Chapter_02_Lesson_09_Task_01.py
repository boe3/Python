# Sprint 4: Statisttical Data Analysis
# Chapter 2: Probability Theory
# Lesson 9: Normal Approximation to the Binomial Distribution


from scipy import stats as st
import math as mt

from scipy import stats as st
import math as mt

binom_n = 23000      # total newsletters sent
binom_p = 0.40       # probability of opening

threshold = 9000     # target number of opens

mu = binom_n * binom_p
sigma = mt.sqrt(binom_n * binom_p * (1 - binom_p))

p_threshold = 1 - st.norm(mu, sigma).cdf(threshold)
print(p_threshold)