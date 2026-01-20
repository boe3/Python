#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 3: Data Visualization


#Task 1: Creating Figures in Python with Matplotlib

import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25], 'c':[1, 3, 6, 10]})
print(df)

df.plot(title='A vs C', x='c', y='a', style='*', xlim=[0, 12], ylim=[1, 6], figsize=[5, 5], color='hotpink', xlabel='C', ylabel='A')
plt.show()
