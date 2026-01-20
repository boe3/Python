# Sprint 4: Statisttical Data Analysis
# Chapter 2: Probability Theory
# Lesson 8: The Normal Distribution


from scipy import stats as st

mu = 24 # place your code here: what is the distribution's mean?
sigma = 3.20 # place your code here: what is the distribution's standard deviation?

distr = st.norm(mu, sigma)

threshold = 0.75 # place your code here: what percentage of orders should cost more than twice the cost of delivery?

max_delivery_price = distr.ppf(1 - threshold) # place your code here: the max delivery cost

print('Maximum cost for courier delivery:', max_delivery_price)