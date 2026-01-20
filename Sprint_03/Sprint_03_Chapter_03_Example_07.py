#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 3: Data Visualization


#Lesson 1: Creating Figures in Python with Matplotlib
#Different styles can even be combined. For example, when we want both lines and points, there's style='o-':
import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})
#print(df)

df.plot(title='A and B', style='o-')
plt.show()
