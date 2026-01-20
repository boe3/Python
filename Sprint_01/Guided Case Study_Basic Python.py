console_data = [['NES', 'Nintendo', 1985, 1995, 179.0, 61910000],
 ['Game Boy', 'Nintendo', 1989, 2003, 89.99, 118690000],
 ['SNES', 'Nintendo', 1990, 2003, 199.0, 49100000],
 ['Virtual Boy', 'Nintendo', 1995, 1996, 179.95, 770000],
 ['Game Boy Advance', 'Nintendo', 2001, 2010, 99.99, 81510000],
 ['Atari 2600', 'Atari', 1977, 1992, 199.0, 30000000],
 ['Sega Genesis', 'Sega', 1988, 1997, 189.0, 30750000],
 ['Game Gear', 'Sega', 1990, 1997, 149.99, 10620000],
 ['Sega CD', 'Sega', 1991, 1996, 299.0, 2240000],
 ['3DO', 'The 3DO Company', 1993, 1996, 699.99, 2000000],
 ['PlayStation', 'Sony Electronics', 1994, 2006, 299.0, 102490000],
 ['PlayStation 2', 'Sony Electronics', 2000, 2013, 299.0, 155000000]]

# write your code here
print('Task 1 Output:')
for row in console_data:
    print(row)
print()

print('Task 2 Output:')
print(console_data[8])
print(console_data[1][5])
print()

print('Task 3 Output:')
total_sold = 0
for row in console_data:
    total_sold = total_sold + row[5]
print(total_sold)
print()

print('Task 4 Output:')
nintendo_sold = 0
for i in range(len(console_data)):
    if console_data[i][1] == 'Nintendo':
        nintendo_sold += console_data[i][5]

print(nintendo_sold)
print()

print('Task 5 Output:')
early_units_sold = 0
for i in range(len(console_data)):
    if console_data[i][2] < 1995 and (console_data[i][1] == 'Sega' or console_data[i][1] == 'Sony Electronics'):
        early_units_sold += console_data[i][5]

print(early_units_sold)
print()