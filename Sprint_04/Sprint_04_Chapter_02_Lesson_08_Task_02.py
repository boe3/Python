# Sprint 4: Statisttical Data Analysis
# Chapter 2: Probability Theory
# Lesson 8: The Normal Distribution


from scipy import stats as st

mu = 420 # place your code here: what is the distribution's mean?
sigma = 65 # place your code here: what is the distribution's standard deviation?

distr = st.norm(mu,sigma)
prob = 0.90 # place your code here: what is the required probability of selling all the products?

n_shipment = distr.ppf(1 - prob) # place your code here: how many items should be ordered?

print('Need to order items:', int(n_shipment)+1)