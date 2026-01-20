brands = ['lenovo', 'apple', 'hp', 'dell']
models = ['ideapad', 'macbook air', 'hd+', 'inspiron']
sizes = [15.6, 13.3, 17.3, 16.0]
prices = [399.99, 749.99, 349.99, 599.99]

print()
print('WORKSPACE:')
laptop_data = {'brand': brands, 'model': models, 'size': sizes, 'price': prices }
print(laptop_data)
print("The size column:", laptop_data['size'])
print("HP size:", laptop_data['size'][2])

laptop_data =  [
    {'brand': 'lenovo', 'model': 'ideapad', 'size': 15.6, 'price': 399.99},
    {'brand': 'apple', 'model': 'macbook air', 'size': 13.3, 'price': 749.99},
    {'brand': 'hp', 'model': 'hd+', 'size': 17.3, 'price': 349.99},
    {'brand': 'dell', 'model': 'inspiron', 'size': 16.0, 'price': 599.99}
]

print(laptop_data)
print("The third row:", laptop_data[2])
print("HP size:", laptop_data[2]['size'])