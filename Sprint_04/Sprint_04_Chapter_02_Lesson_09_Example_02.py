# Sprint 4: Statisttical Data Analysis
# Chapter 2: Probability Theory
# Lesson 9: Normal Approximation to the Binomial Distribution

from scipy import stats as st
import math as mt

binom_n = 5000
binom_p = 0.15

clicks = 715

mu = binom_n * binom_p
sigma = mt.sqrt(binom_n * binom_p * (1 - binom_p))

p_clicks = st.norm(mu, sigma).cdf(clicks)
print(p_clicks)