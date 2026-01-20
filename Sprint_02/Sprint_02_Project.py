#Import the pandas library as 'pd'
import pandas as pd

# Read the dataset into a DataFrame
df = pd.read_csv('/datasets/movies_and_shows.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Get information about the DataFrame and print the column names
df.info()


#Task 1: Data Cleaning
# Rename columns to make them consistent and correct errors
print(df.columns)
df = df.rename(columns={
        '   name': 'Name',
        'r0le': 'Role',
        'TITLE': 'Title',
		'  Type':'Type',
		'release Year':'Release Year',
		'genres':'Genres',
		'imdb sc0re':'IMDb Score',
		'imdb v0tes':'IMDb Votes',
    })

# Print the updated column names to confirm changes
print(df)


#Task 2: Correcting a Misspelled Name in the Data
# Locate the row with the incorrect name
result = df.loc[85576,'Name']
print(result)

# Correct the name
df.loc[85576, 'Name'] = 'Ines Prieto'

# Verify the correction
result = df.loc[85576,'Name']
print(result)


#Task 3: Finding All Movies and Shows Featuring Ines Prieto
# Filter rows where the actor's name is "Ines Prieto" and display the title, release_year, genres, and imdb_score
filtered_df = df[df['Name'] == 'Ines Prieto'][['Title', 'Release Year', 'Genres', 'IMDb Score']]

# Display the result
print(filtered_df)


# Task 4: Finding Highly Rated Movies
# Filter for movies with an IMDb score above 9.0
high_rated_movies = df[df['IMDb Score'] > 9.0][['Title', 'Release Year', 'Genres', 'IMDb Score']]

# Extract the 'title' column from the filtered DataFrame
print(high_rated_movies)

# Get a unique set of titles
unique_titles = set(high_rated_movies['Title'])

# Print the unique titles
print()
print('Unique:')
print(unique_titles)


# Task 5: Creating a Function to Find Unique Top-Rated Movies
# Define the function
def get_unique_top_movies(min_score):
     # Filter for movies with IMDb score above min_score
    filtered_movies = df[df['IMDb Score'] > min_score]
    # Extract the 'title' column
    titles = filtered_movies['Title']
     # Remove duplicate titles
    unique_titles = set(titles)
    # Return unique titles
    return unique_titles    

# Test the function
print(get_unique_top_movies(9.0))


# Task 6: Creating a Function to Find Top Movies from a Specific Decade
# Define the function
def get_top_movies_from_decade(decade_start, min_score):
    # Filter for movies released within the decade
    decade_end = decade_start + 9
    decade_movies = df[(df['Release Year'] >= decade_start) & (df['Release Year'] <= decade_end)]
    # Further filter by IMDb score
    high_rated_decade_movies = decade_movies[decade_movies['IMDb Score'] > min_score]
    # Extract the 'Title' column   
    titles = high_rated_decade_movies['Title']
    # Extract and remove duplicate titles
    unique_titles = set(titles)
    # Return unique titles
    return unique_titles
  
# Test the function
print(get_top_movies_from_decade(1990, 8.5))


# Task 7: Creating a Function to List All  Actors in a Given Title
# Define the function
def get_actors_for_title(title):
    # Filter for rows with the specified title and role as 'ACTOR'
    actors = df[(df['Title'] == title) & (df['Role'] == 'ACTOR')]
    # Extract the 'name' column for actor names
    actor_names = actors['Name']
    # Combine names into a single string
    result = ', '.join(actor_names)
    # Return the result
    return result


# Task 8: Creating a Function to Categorize Movies by IMDb Score
# Define the function
def categorize_imdb_score(title):
    # Filter for the row with the specified title
    movie = df[df['Title'] == title]

    # Check if title exists
    if movie.empty:
        return "Title not found"
  
    # Retrieve the IMDb score for the movie
    imdb_score = movie.iloc[0]['IMDb Score']

    # Categorize score using if-else and return the ranking accordingly
    if imdb_score >= 9.0:
        return "Excellent"
    elif 7.0 <= imdb_score < 9.0:
        return "Good"
    elif 5.0 <= imdb_score < 7.0:
        return "Average"
    else:
        return "Poor"  

# Test the function
print(categorize_imdb_score("Taxi Driver"))










