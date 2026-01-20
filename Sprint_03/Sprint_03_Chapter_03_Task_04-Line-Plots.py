#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 3: Data Visualization


#Task 1: Line Plots

#Create a line plot for the trade volume from the Starbucks stock dataset. Make your plot adhere to the following:
#1. Titled “Historic SBUX volume” (case is important)
#2. X-axis labeled “Date”
#3. Y-axis labeled “Volume”
#4. -axis tick labels rotated 50 degrees
#5. Y-axis range from 1 million to 70 million (i.e. 1e6 and 7e7)
#6. No legend

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('/datasets/sbux.csv')

df.plot(x='date',
        y='volume',
        legend=False,
        title='Historic SBUX volume',
        xlabel='Date',
        ylabel='Volume',
        rot=50,
        ylim=[1e6, 7e7])

plt.show()

#Task 2: Line Plots

#Create a line plot that includes both the opening and closing price. To do this, you can pass the list of column names, cols, provided in the precode as your argument for y=. Since you’ll have two different variables on the same graph, make sure to include a legend this time. Have your plot also adhere to the following:
#1. Titled “Historic SBUX price” (case is important)
#2. X-axis labeled “Date”
#3. Y-axis labeled “Share price / USD”
#4. X-axis tick labels rotated 50 degrees
#Don’t forget to include plt.show().

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('/datasets/sbux.csv')
cols = ['open', 'close']
df.plot(x='date',
        y=cols,
        legend=True,
        title='Historic SBUX price',
        xlabel='Date',
        ylabel='Share price / USD',
        rot=50)
plt.show()
