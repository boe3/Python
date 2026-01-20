#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 7: Data Transformations
#Lesson 4: Processing Grouped data with merge()

import pandas as pd

first_pupil_df = pd.DataFrame(
    {
        'author': ['Alcott', 'Fitzgerald', 'Steinbeck', 'Twain', 'Hemingway'],
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

# Example 1
print('Example 1')
print(first_pupil_df)
print()
print(second_pupil_df)
print()

# Example 2
both_pupils = first_pupil_df.merge(second_pupil_df, on='author')
print('Example 2: Inner merge')
print(both_pupils)
print()

# Example 3
print('Example 3: Outer merge')
both_pupils = first_pupil_df.merge(second_pupil_df, on='author', how='outer')
print(both_pupils)
print()

# Example 4
print('Example 4: Left merge')
both_pupils = first_pupil_df.merge(second_pupil_df, on='author', how='left')
print(both_pupils)
print()

# Example 5
print('Example 5: Consideration of column names')
both_pupils = first_pupil_df.merge(second_pupil_df,
                                   on='author',
                                   suffixes=['_1st_student', '_2nd_student']
                                  )
print(both_pupils)
print()
