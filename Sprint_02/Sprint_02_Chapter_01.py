#Sprint 2: Working with Data in Python
#Chapter 1: Dictionaries

#Lesson 1: Properties of Dictionaries
print('Lesson 1: Properties of Dictionaries')
print('Lesson 1 Task 1 Output:')
coffee_stocks = {'SBUX': 120.29, 'DNKN': 106.48, 'BROS': 76.25}

print(coffee_stocks)
print(type(coffee_stocks))
print(len(coffee_stocks))
print()

print('Lesson 1 Task 2 Output:')
print(coffee_stocks['BROS'])
print()

#Lesson 2: Accessing Dictionary Data
print('Lesson 2: Accessing Dictionary Data')
print('Lesson 2 Task Output:')
values = tuple(coffee_stocks.values())
print(values)
print()

#Lesson 3: Modifying Dictionaries
print('Lesson 3: Modifying Dictionaries')
print('Lesson 3 Task 1 Output:')
coffee_stocks['SJM'] = 159.22
coffee_stocks['SBUX'] = 120.29
print(coffee_stocks)
print()

print('Lesson 3 Task 2 Output:')
coffee_stocks = {'SBUX': 120.29, 'DKNN': 106.48, 'BROS': 76.25}
dnkn_price = coffee_stocks.pop('DKNN')
coffee_stocks['DNKN'] = dnkn_price
print(dnkn_price)
print(coffee_stocks)
print()

#Lesson 4: Combining Dictionaries and Lists
print('Lesson 4: Combining Dictionaries and Lists')
print('Lesson 4 Task 1 Output:')
ticker = ['SBUX', 'DNKN', 'BROS']
ath_price = [120.29, 106.48, 76.25]
ath_year = [2021, 2020, 2021]

ath_data = {'company': ticker, 'price': ath_price, 'year': ath_year}
print(ath_data['year'][1])
print()

print('Lesson 4 Task 2 Output:')
ath_data = [
    {'company': 'SBUX', 'price': 120.29, 'year': 2021},
    {'company': 'DNKN', 'price': 106.48, 'year': 2020},
    {'company': 'BROS', 'price': 76.25, 'year': 2021}
]

print(ath_data[0]['price'])
print()