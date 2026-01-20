# Sprint 4: Statisttical Data Analysis
# Chapter 2: Probability Theory
# Lesson 8: The Normal Distribution


from scipy import stats as st

mu = 100500 # what is the mean of the distribution?
sigma = 3500 # what is the standard deviation of the distribution?

distr = st.norm(100500,3500)

more_threshold = 111000 # what is the lower limit for number of visitors?
fewer_threshold = 92000 # what is the upper limit for number of visitors?

p_more_visitors =  1 - distr.cdf(more_threshold) # calculate the probability that there are more visitors than the lower threshold
p_fewer_visitors = distr.cdf(fewer_threshold) # calculate the probability that there are fewer visitors than the upper threshold

print(f'Probability there are more than {more_threshold} visitors: {p_more_visitors}')
print(f'Probability there are fewer than {fewer_threshold} visitors: {p_fewer_visitors}')