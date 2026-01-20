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
for i in range(len(console_data)):
    print(f"The {console_data[i][0]} console was made by {console_data[i][1]} released on {console_data[i][2]} discontinued on {console_data[i][3]} and sold for ${console_data[i][4]} selling {console_data[i][5]} units.")


if console_data[8][0] == 'Sega CD':
    print("The Sega CD was an add-on for the Sega Genesis console.")
    print(console_data[8])


print('Task 3 Output:')
total_sold = 0
for row in console_data:
    total_sold += row[5]

print(f'Total units sold: {total_sold}')
print()