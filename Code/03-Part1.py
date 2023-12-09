import shared
import re

rows = shared.getInput('03.txt')

numbers = '0123456789'
width = len(rows[0]) - 1
height = len(rows) - 1
symbol_coords = []


# For a given pair of coordinates, check the surrounding coordinates to see if there is a symbol there
def hasAdjacentSymbol(coord_pair):
    has_adjacent_symbol = False
    x = coord_pair[0]
    y = coord_pair[1]
    adjacent_coords = []
        

    # Top left corner
    if x == 0 and y == 0:
        adjacent_coords = [(x+1,y), (x+1,y+1), (x,y+1)]
    # Top right corner
    elif x == width and y == 0:
        adjacent_coords = [(x-1,y), (x-1,y+1), (x,y+1)]
    # Bottom left corner
    elif x == 0 and y == height:
        adjacent_coords = [(x,y+1), (x+1,y+1), (x+1,y)]
    # Bottom right corner
    elif x == width and y == height:
        adjacent_coords = [(x-1,y), (x-1,y-1), (x,y-1)]
    # Left side
    elif x == 0:
        adjacent_coords = [(x,y-1), (x,y+1), (x+1,y-1), (x+1,y), (x+1,y+1)]
    # Top side
    elif y == 0:
        adjacent_coords = [(x-1,y), (x+1,y), (x-1,y+1), (x,y+1), (x+1,y+1)]
    # Right side
    elif x == width:
        adjacent_coords = [(x,y-1), (x,y+1), (x-1,y-1), (x-1,y), (x-1,y+1)]
    # Bottom side
    elif y == height:
        adjacent_coords = [(x-1,y), (x+1,y), (x-1,y-1), (x,y-1), (x+1,y-1)]
    # Everywhere else
    else:
        adjacent_coords = [(x-1,y),(x-1,y-1),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y),(x+1,y-1),(x+1,y+1)]

    for coords in adjacent_coords:
        if coords in symbol_coords:
            return True
    return False



all_nums = []
# Catalog the coordinates for every symbol by creating an array of dictionaries where the dictionary has the value of the number
#       and the coordinates for each part of the number
for x, row in enumerate(rows):
    number = {'value': '', 'coords': []}
    for y, column in enumerate(row):
        # If we encounter a number, start logging it until we hit something else
        if column in numbers:
            number['value'] += column
            number['coords'].append((x,y))
        # When we hit something else
        elif column not in numbers:
            # If we hit a symbol, log it
            if column != '.':
                symbol_coords.append((x,y))
            # This marks the end of encountering a number, log it and reset
            if number['value'] != '':
                all_nums.append(number)
                number = {'value': '', 'coords': []}
        # If we're at the end of row, check if we have a number stored and store it
        if y == width:
            all_nums.append(number)
            number = {'value': '', 'coords': []}


just_nums = []
total = 0
# For each number, loop through the coordinates that make up that number and see if there are any symbols around it
for num in all_nums:
    for coord in num['coords']:
        if hasAdjacentSymbol(coord):
            just_nums.append(int(num['value']))
            total += int(num['value'])
            break

print(total)


