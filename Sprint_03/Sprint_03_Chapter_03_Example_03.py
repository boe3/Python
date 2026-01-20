#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 3: Data Visualization


#Lesson 1: Creating Figures in Python with Matplotlib
#Another option is to writee code that saves our figures as image files. For example, we can save the above figure in PNG format using the savefig() function from matplotlib:
import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})
#print(df)

df['b'].plot()
plt.savefig('myplot.png')
