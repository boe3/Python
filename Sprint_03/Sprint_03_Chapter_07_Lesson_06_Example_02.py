#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 7: Data Transformations
#Lesson 4: Processing Grouped data with merge()

import pandas as pd

first_pupil_df = pd.DataFrame(
    {
        'authors': ['Alcott', 'Fitzgerald', 'Steinbeck', 'Twain', 'Hemingway'],
        'title': ['Little Women',
                  'The Great Gatsby',
                  'Of Mice and Men',
                  'The Adventures of Tom Sawyer',
                  'The Old Man and the Sea'
                 ],
    }
)
second_pupil_df = pd.DataFrame(
    {
        'author': ['Steinbeck', 'Twain', 'Hemingway', 'Salinger', 'Hawthorne'],
        'title': ['East of Eden',
                  'The Adventures of Huckleberry Finn',
                  'For Whom the Bell Tolls',
                  'The Catcher in the Rye',
                  'The Scarlett Letter'
                 ],
    }
)

# Example 6
print('Example 6: Consideration of column names')
both_pupils = first_pupil_df.merge(second_pupil_df,
                                   left_on='authors',
                                   right_on='author'
                                  )
print(both_pupils)
print()

# Example 7
print('Example 7: The drop() method')
both_pupils = first_pupil_df.merge(second_pupil_df,
                                   left_on='authors',
                                   right_on='author'
                                  )
print(both_pupils.drop('author', axis='columns'))
print()