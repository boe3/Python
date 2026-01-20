# Run any code you'd like
# You can even import modules
# And feel free to access any of the datasets you're familiar with
import pandas as pd
dataset_list = pd.read_csv('/datasets/datasets.csv')
print(dataset_list)

print(dataset_list['file'][3])

path = '/datasets/' + dataset_list['file'][3]
df = pd.read_csv(path)
print(df)