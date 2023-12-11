import shared
import copy
from pprint import pprint
import time

start_time = time.time()

map_as_rows = shared.getInput('11.txt')


width = len(map_as_rows[0]) - 1
height = len(map_as_rows) - 1



def getDistance(coord1, coord2):
    x1,y1 = coord1
    x2,y2 = coord2

    return abs(x2-x1) + abs(y2-y1)


# Log all the coordinates for all the galaxies
all_galaxies = {}
count = 1
for x, row in enumerate(map_as_rows):
    for y, column in enumerate(row):
        if column == '#':
            all_galaxies[count] = {'coords':(x, y), 'under_rows': 0, 'right_cols': 0, 'new_coords': 0}
            count += 1


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


for k,v in all_galaxies.items():
    for row in rows_to_add:
        if v['coords'][0] > row:
            v['under_rows'] += 1
    for col in columns_to_add:
        if v['coords'][1] > col:
            v['right_cols'] += 1
    

# We can actually just to math to figure out how far away each thing will be and make that the new coordinates
multiplier = 1000000
new_all_galaxies = []
for k,v in all_galaxies.items():
    x = v['coords'][0] + (multiplier * v['under_rows']) - v['under_rows']
    y = v['coords'][1] + (multiplier * v['right_cols']) - v['right_cols']
    new_all_galaxies.append((x,y))



all_pairs = []
total = 0
while True:
    thing = new_all_galaxies.pop(0)
    for i in range(len(new_all_galaxies)):
        total += getDistance(thing, new_all_galaxies[i])
        
    if len(new_all_galaxies) == 0:
        break

print(total)
print(time.time()-start_time)










