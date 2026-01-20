# Sprint 4: Statisttical Data Analysis
# Chapter 2: Probability Theory
# Lesson 7: The Binomial Distribution


from matplotlib import pyplot as plt
from math import factorial

'''
Your company is organizing an important event. The PR team is looking for at least six media partners to provide publicity for it. Going by experience, about one in five media outlets that they negotiate with will say yes. Create a probability distribution and histogram for the random variable “number of media representatives who say yes” if you begin negotiations with 30 outlets.
'''

# add your code here: what is the probability of drawing up a contract?
p = 0.20
# add your code here: how many companies will we negotiate with?
n = 30

# add your code here: create a variable for the distribution value
distr = []

for k in range(0 , n + 1):
    # add your code here: generate the probability distribution
    choose = factorial(n)/(factorial(k) * factorial(n-k))
    prob = choose * p**k * (1-p)**(n-k) 
    distr.append(prob)
    
# add your code here: create a histogram of the probability distribution
plt.bar(range(0,n+1), distr)