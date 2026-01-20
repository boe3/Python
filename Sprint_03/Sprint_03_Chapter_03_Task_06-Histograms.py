#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 3: Data Visualization

#Lesson 8: Histograms
#Task 1

#Investigate the distribution of weight for different age groups. To start, partition the dataset into three DataFrames by filtering df and assign them to the following variables:
#1. df_20s: Only the rows where 'age' is less than 30
#2. df_30s: Only the rows where 'age' is greater than or equal to 30 and less than 40
#3. df_40s: Only the rows where 'age' is greater than or equal to 40 (includes age 50)

#To verify that you filtered correctly, print the following results:
#1. The sum of the lengths of the three DataFrames (there should be 10,000 rows total)
#2. The min and max value in the 'age' column of df_20s
#3. The min and max value in the 'age' column of df_30s
#4. The min and max value in the 'age' column of df_40s
#5. The precode already contains a template for you to print your results; just finish the code.

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('datasets/height_weight.csv')

# partition df into separate data frames based on age
df_20s = df[df['age'] < 30]
df_30s = df[(df['age'] >= 30) & (df['age'] < 40)]
df_40s = df[df['age'] >= 40]

# print out the results
print("Sum of data frame lengths:", len(df_20s) + len(df_30s) + len(df_40s))
print("Min and max age for df_20s:", df_20s['age'].min(), df_20s['age'].max())
print("Min and max age for df_30s:", df_30s['age'].min(), df_30s['age'].max())
print("Min and max age for df_40s:", df_40s['age'].min(), df_40s['age'].max())


#ALTERNATIVE CODE FOR TASK 1
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('datasets/height_weight.csv')

# partition df into separate data frames based on age
df_20s = df[df['age'] < 30]
df_30s = df[(df['age'] >= 30) & (df['age'] < 40)]
df_40s = df[df['age'] >= 40]

# calculate the sum of the lengths of the three data frames
sum_lengths = len(df_20s) + len(df_30s) + len(df_40s)

# calculate the min and max age for each data frame
min_max_20s = df_20s['age'].min(), df_20s['age'].max()
min_max_30s = df_30s['age'].min(), df_30s['age'].max()
min_max_40s = df_40s['age'].min(), df_40s['age'].max()

# print out the results
print("Sum of lengths of the three data frames:", sum_lengths)
print("Min and max age in df_20s:", min_max_20s)
print("Min and max age in df_30s:", min_max_30s)
print("Min and max age in df_40s:", min_max_40s)


#Task 2
#Create a visualization that has the histogram for each age group all on the same graph. To do so, do the following:
#Call plot() on the 'weight' column of df_20s and set the number of bins to 20
#Then do the same with df_30s, but also include an alpha value of 0.6
#Then do the same with df_40s, but make the alpha value 0.3
#Also, include the following in just the first call to plot() on df_20s:
#1. Title the figure “Weight / lbs”
#2. Label the Y-axis “Frequency”
#Finally, use the legend() function from matplotlib to label each histogram “20s”, “30s”, and “40s” respectively. Also include plt.show() at the end.
#ALTERNATIVE CODE FOR TASK 2
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('datasets/height_weight.csv')

# partition df into separate data frames based on age
df_20s = df[df['age'] < 30]
df_30s = df[(df['age'] >= 30) & (df['age'] < 40)]
df_40s = df[df['age'] >= 40]

df_20s['weight'].plot(kind='hist', bins=20, title='Weight / lbs', ylabel='Frequency')
df_30s['weight'].plot(kind='hist', bins=20, alpha=0.6,)
df_40s['weight'].plot(kind='hist', bins=20, alpha=0.3)

plt.legend(['20s', '30s', '40s'])
plt.show()














