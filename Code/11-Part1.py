import shared
import copy
from pprint import pprint

map_as_rows = shared.getInput('11.txt')

##map_as_rows = '''...#......
##.......#..
###.........
##..........
##......#...
##.#........
##.........#
##..........
##.......#..
###...#.....'''.split('\n')

width = len(map_as_rows[0]) - 1
height = len(map_as_rows) - 1


def addRow(row_index):
    global map_as_rows
    map_as_rows.insert(row_index, '.'*(width+1))

def addColumn(col_index):
    global map_as_rows
    new_rows = []
    for row in map_as_rows:
        new_rows.append(row[:col_index] + '.' + row[col_index:])
    map_as_rows = new_rows

def getDistance(coord1, coord2):
    x1,y1 = coord1
    x2,y2 = coord2

    return abs(x2-x1) + abs(y2-y1)


# Rotate the map clockwise once, then reverse. This gives us all the columns as rows
map_as_columns = []
map_as_rows_copy = copy.deepcopy(map_as_rows)
for thing in list(zip(*map_as_rows_copy[::-1])):
    map_as_columns.append(''.join(list(reversed(''.join(list(thing))))))


# Figure out where we need to add blank rows
rows_to_add = []
for index, row in enumerate(map_as_rows):
    if list(set(row))[0] == '.':
        rows_to_add.append(index)
    

# Figure out where we need to add blank columns
columns_to_add = []
for index, column in enumerate(map_as_columns):
    if list(set(column))[0] == '.':
        columns_to_add.append(index)


# Add in all of our blank rows starting from the bottom (otherwise it just adds everything to the top because it's moving)
for row_index in reversed(rows_to_add):
    addRow(row_index)
# Add in all of our blank columns starting from the right (otherwise it just adds everything to the left because it's moving)    
for col_index in reversed(columns_to_add):
    addColumn(col_index)


all_galaxies = []
for x, row in enumerate(map_as_rows):
    for y, column in enumerate(row):
        if column == '#':
            all_galaxies.append((x, y))

all_pairs = []
total = 0
while True:
    thing = all_galaxies.pop(0)
    for i in range(len(all_galaxies)):
        #all_pairs.append([thing, all_galaxies[i]])
        total += getDistance(thing, all_galaxies[i])
        
    if len(all_galaxies) == 0:
        break

print(total)











