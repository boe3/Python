#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 3: Data Visualization


#Lesson 1: Creating Figures in Python with Matplotlib
#If you want to plot two columns against each other, we can use the x= and y= parameters to accomplish this:
import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})
#print(df)

df.plot(x='b', y='a', title='A vs B', style='o')
plt.show()