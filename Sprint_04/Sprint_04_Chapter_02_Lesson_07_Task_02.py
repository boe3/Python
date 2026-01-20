# Sprint 4: Statisttical Data Analysis
# Chapter 2: Probability Theory
# Lesson 7: The Binomial Distribution


from matplotlib import pyplot as plt
from math import factorial

'''
After graduating from the snake nursery, Peter Python decides to apply to a python academy. To get in, he needs to take six different exams (where the probability of passing each is independent of the probability of passing the others). Peter thinks he’s really well prepared: the probability of failing each of these exams, judging by his practice tests, is 15%.
Create a probability distribution for the random variable “number of exams Peter fails” and a histogram for it.
'''

# add your code here: How many exams does he need to pass?
n_exams = 6
# add your code here: what is the probability of him failing one exam?
failure_rate = 0.15

# add your code here: create a variable for the distribution value
distr = []

for k in range(0,n_exams+1):
    # add your code here: calculate the probability of him passing 
    # 0 exams, 1 exam, and so on up to 6
    choose = factorial(n_exams)/(factorial(k) * factorial(n_exams-k))
    prob = choose * failure_rate**k * (1-failure_rate)**(n_exams-k) 
    distr.append(prob)
    
# create a histogram of the probability distribution
plt.bar(range(0, n_exams + 1), distr)