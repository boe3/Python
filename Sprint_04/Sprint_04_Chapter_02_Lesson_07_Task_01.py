# Sprint 4: Statisttical Data Analysis
# Chapter 2: Probability Theory
# Lesson 7: The Binomial Distribution


from math import factorial

'''
On some days, the pythons in the python nursery are fed apples, and on other days they’re given pears.
There’s a three-day supply of pears and a four-day supply of apples for the next week (seven days). On any given day, the pythons can be fed only apples or pears, not a combination.
So an example of their diet would be pears, apples, pears, pears, apples, apples, apples.
How many different combinations of a pears-and-apples diet can there be this week? Save the results to the n_diets variable and print it.
'''

# Number of ways to get k days out of n days:
# C(n, k) =  **n! / ( k! * (n-k)! )


n_diets = factorial(7)/(factorial(3)*factorial(4))

print(n_diets)
print()