#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 3: Data Visualization


#Lesson 1: Creating Figures in Python with Matplotlib
#We can also set the axis limits using the xlim= and ylim= parameters. Let’s expand the range of the horizontal axis from 0 to 30, but just set the minimum of the vertical axis to 0:
import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})
#print(df)

df.plot(x='b', y='a', title='A vs B', style='o', xlim=[0, 30], ylim=0)
plt.show()