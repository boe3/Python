#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 3: Data Visualization


#Task 2: Scatterplots

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('/datasets/height_weight.csv')

# write your code here
df.plot(title='Adult heights', x='age', y='height', alpha=0.36, figsize=[8, 6],xlabel='Age / years', ylabel='Height / inches', kind='scatter' )
plt.show()


#Task 3: Correlation task 1
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('/datasets/height_weight.csv')

# write your code here
df.plot(title='Adult heights', x='age', y='height', alpha=0.36, figsize=[8, 6],xlabel='Age / years', ylabel='Height / inches', kind='scatter' )
plt.show()

ah_corr = df['height'].corr(df['age'])
print(ah_corr)


#Task 4: Correlation task 2
import pandas as pd

df = pd.read_csv('/datasets/height_weight.csv')

print(df.corr())