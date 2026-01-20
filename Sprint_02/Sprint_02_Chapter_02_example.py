#Sprint 2: Working with Data in Python
#Chapter 2: Functions

#Lesson 1: Function Syntax
print('Lesson 1: Function Syntax')
print('Example: Creating a Function')
def square_and_halve(number):
    result = (number ** 2) / 2
    return result

x = square_and_halve(6)
print(x)
print()

print('Example: Expanding functions to work with lists')
def square_and_halve_list(numbers):
    result_list = []
    for number in numbers:
        result = (number ** 2) / 2
        result_list.append(result)
    return result_list

numbers = [2, 4, 6, 8]
x = square_and_halve_list(numbers)
print(x)
print()

#Lesson 2: Default Arguments
print('Lesson 2: Default Arguments')
print('Example: What is a default argument?')
def square_and_halve(number=10):
    result = (number ** 2) / 2
    return result

x = square_and_halve()
print(x)
print()

print('Example 2: Flags')
asc = sorted([10, 3, 4, 7, 9, 2, 1, 6, 5, 8])
desc = sorted([10, 3, 4, 7, 9, 2, 1, 6, 5, 8], reverse=True)

print(f"Sorts in ascending order by default: {asc}")
print(f"Change flag to sort in descending order: {desc}")
print()

#Lesson 3: Positional and Keyword Arguments
print('Lesson 3: Positional and Keyword Arguments')
print('Example: Passing only positional arguments')
def division(numerator, denominator): 
    result = numerator / denominator
    print(result)

division(10, 2)
print()
def division(denominator, numerator): 
    result = numerator / denominator
    print(result)

division(10, 2)
print()

print('Example: Passing only keyword arguments')
def division(numerator, denominator): 
    result = numerator / denominator
    print(result)

division(numerator=10, denominator=2)
division(denominator=2, numerator=10)
print()

print('Example: Combining positional and keyword arguments')
def division(numerator, denominator): 
    result = numerator / denominator
    print(result)

division(10, denominator=2)
print('NOTE: Positional arguments MUST come before keyword arguments.')
print()

#Lesson 4: Return Values
print('Lesson 4: Return Values')
print('Example: Returing single values')
# Create a function that returns the square of a number
def square(num):
    return num * num

# Call the function
result = square(4)

# Print the result
print(result)
print()

print('Example: Returning multiple values')
# Create a function that returns the square and the cube of a number
def square_and_cube(num):
    square = num * num
    cube = num * num * num
    return square, cube

# Call the function
sqr, cub = square_and_cube(3)

# Print the results
print(f"Square: {sqr}, Cube: {cub}")
print()

print('Example: Multiple return Statements in a function')
# Create a function that returns a different value based on a condition
def check_sign(num):
    if num > 0:
        return "Positive",num
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Call the function with different values
print(check_sign(10))  # Positive
print(check_sign(-5))  # Negative
print(check_sign(0))   # Zero
print()





