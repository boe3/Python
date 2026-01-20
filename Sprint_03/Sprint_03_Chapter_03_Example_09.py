#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 3: Data Visualization


#Lesson 1: Creating Figures in Python with Matplotlib
#To change the axis labels, we can use the xlabel= and ylabel= parameters in the plot() method:
import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})
#print(df)

df.plot(x='b',
        y='a',
        title='A vs B',
        style='o',
        xlabel="Hi, I'm B",
        ylabel="Hi, I'm A")

plt.show()