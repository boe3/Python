#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 3: Data Visualization


#Lesson 1: Creating Figures in Python with Matplotlib
#Let's add gridlines to help the eye catch which values we're plotting. To do so, set the grid= parameter to True (by default, this parameter is set to False):
import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})
#print(df)

df.plot(x='b', y='a', title='A vs B', style='o', grid=True)
plt.show()