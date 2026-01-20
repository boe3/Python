#Sprint 2: Working with Data in Python
#Chapter 3: Using pandas to Work with Data


import pandas as pd

# Create a simple DataFrame
data = {
    '    name': ['Robert De Niro', 'Jodie Foster', 'Albert Brooks', 'Harvey Keitel', 'Cybill Shepherd'],
    'Character': ['Travis Bickle', 'Iris Steensma', 'Tom', 'Matthew Sport Higgings', 'Betsy'],
    'rOle': ['ACTOR', 'ACTOR', 'ACTOR', 'ACTOR', 'ACTOR'],
    'TITLE': ['Taxi Driver', 'Taxi Driver', 'Taxi Driver', 'Taxi Driver', 'Taxi Driver'],
    '    Type': ['MOVIE', 'MOVIE', 'MOVIE', 'MOVIE', 'MOVIE'],
    'release Year': [1976, 1976, 1976, 1976, 1976],
    'genres': ['drama,crime', 'drama,crime', 'drama,crime', 'drama,crime', 'drama,crime'],
    'imdb sc0re': [8.2, 8.2, 8.2, 8.2, 8.2],
    'imdb v0tes': [808582.0, 808582.0, 808582.0, 808582.0, 808582.0]
}

df = pd.DataFrame(data)

# Create the index
index_ = ['Row_1', 'Row_2', 'Row_3', 'Row_4', 'Row_5']

# Set the index
df.index = index_

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Add a new column
df['Age in 5 Years'] = df['release Year'] + 5

# Filter rows where Age is greater than 28
filtered_df = df[df['release Year'] > 28]

print("\nDataFrame after adding a column:")
print(df)

print("\nFiltered DataFrame (release Year > 28):")
print(filtered_df)

print("\nRenamed:")
df = df.rename(columns={
        '   name': 'Name',
        'rOle': 'Role',
        'TITLE': 'Title',
		'  Type':'Type',
		'release Year':'Release Year',
		'genres':'Genres',
		'imdb sc0re':'IMDb Score',
		'imdb v0tes':'IMDb Votes',
    })
print(df)

result = df.loc['Row_2', 'name']
print(result)