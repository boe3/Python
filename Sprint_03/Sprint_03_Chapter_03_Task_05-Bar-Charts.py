#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 3: Data Visualization

#Lesson 8: Bar Charts
#Task 1

#The population of California is so much greater than Oregon and Washington that it’s hard to get a sense of the data for those two states from the plot we made. Create a bar chart that shows only the populations of Oregon and Washington for each year in the dataset. Do this by calling plot() on df with arguments that give your figure the following properties:
#1. Includes only data for Oregon and Washington
#2. Titled “Pacific Northwest population growth” (case is important)
#3. X axis labeled “Year”
#4. Y axis labeled “Population (millions)”
#5. Legend with labels “OR” and “WA” for Oregon and Washington populations, respectively

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('/datasets/west_coast_pop.csv')

# write your code here
df.plot(x='year',
        y=['or_pop', 'wa_pop'],
        kind='bar',
        title='Pacific Northwest population growth',
        xlabel='Year',
        ylabel='Population (millions)')

plt.legend(['OR', 'WA'])
plt.show()