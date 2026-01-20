# Sprint 4: Statisttical Data Analysis
# Chapter 2: Probability Theory
# Lesson 8: The Normal Distribution

from scipy import stats as st

# normal distribution with an expected value of 1000
# and a standard deviation of 100
distr = st.norm(1000, 100)

x = 1000
x1 = 900
x2 = 1100


# the probability of getting 1000 or less with this distribution is 0.5
result = distr.cdf(x)  # calculate probability of getting the value x
print("Example 1")
print(result)
print()

# Note that you can get the same result without using intermediate variables.
# the probability of getting 1000 or less with this distribution is 0.5
result2 = st.norm(1000, 100).cdf(1000)
print("Example 2")
print(result2)
print()

# Here' another example. Let’s see what the probability of falling between 900 and 1100 is
print("Example 3")
result3 = distr.cdf(x2) - distr.cdf(x1)
print(result3)
print()

print("Example 4")
p1 = 0.841
result4 = distr.ppf(p1)
print(result4)
print()
