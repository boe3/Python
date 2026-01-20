#Sprint 2: Working with Data in Python
#Chapter 2: Functions

#Lesson 1: Function Syntax
print('Lesson 1: Function Syntax')
print('Practice problem:')
animals = ['Koala', 'antelope', 'Gibbon', 'Alligator', 'manatee', 'Capybara']

def sort_alph(sorts):
    sorted_w = []
    for sort in sorts:
        sorted_w.append(sort.lower())

    return sorted(sorted_w)

print(sort_alph(animals))
print()

#Lesson 2: Default Arguments
print('Lesson 2: Default Arguments')
print('Question: What will be displayed by the code below?')
def replicate(text, n=2):
    return text * n * 2

print(replicate('Hey!'))
print()

print('Task')
# List of animals
animals = ['Koala', 'antelope', 'Gibbon', 'Alligator', 'manatee', 'Capybara']

# Function to sort animals and optionally change their case
def sort_animals(animals_list, lowercase=True):
    sorted_animals = []
    
    if lowercase:
        # Convert each animal name to lowercase before sorting
        # (Complete this part)
            for sort in animals_list:
                sorted_animals.append(sort.lower())
        
    else:
        # Keep the original case and add to the sorted list
        # (Complete this part)
            for sort in animals_list:
                sorted_animals.append(sort)
    
    # Sort the list
    # (Complete this part)
    sorted_animals = sorted(sorted_animals)
    
    return sorted_animals

# Example calls to test the function
sorted_lowercase = sort_animals(animals)
sorted_original_case = sort_animals(animals, lowercase=False)

print(sorted_lowercase)
print(sorted_original_case)
print()

#Lesson 3: Positional and Keyword Arguments
print('Lesson 3: Positional and Keyword Arguments')
print('Question: What will the code below display')
def paste(word3, word1, word2):
    print(word1 + word2 + word3)
    
paste('super', 'wonderful', 'amazing')
print()

print('Question: What will the code below display')
def paste(word3, word1, word2):
    print(word1 + word2 + word3)
    
paste(word1='super', word2='wonderful', word3='amazing')
print()

#Lesson 4: Return Values
print('Lesson 4: Return Values')
print('Practice Codiing Question:')
def analyze_number(num):
    if num > 0:
        result = 'positive'
    elif num < 0:
        result = 'negative'
    else:
        result = 'zero'

    square = num * num
    cube = num * num * num
    return result, square, cube

print(analyze_number(10))  # Positive
print(analyze_number(-5))  # Negative
print(analyze_number(0))   # Zero
