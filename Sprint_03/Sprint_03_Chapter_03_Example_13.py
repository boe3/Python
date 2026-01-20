#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 3: Data Visualization


#Lesson 1: Creating Figures in Python with Matplotlib
#The width and height in inches are passed as a list: figsize=[width, height]. Let’s compare two differently sized figures:
import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})
#print(df)

# building a small figure
df.plot(x='b', y='a', style='o', xlim=[0, 30], figsize=[2, 2])

# building a large figure
df.plot(x='b', y='a', style='o', xlim=[0, 30], figsize=[10, 4])

plt.show()