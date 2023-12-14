import shared
import re
import copy
from pprint import pprint
from itertools import product
import time
start_time = time.time()

# rows = ''
# with open('../Input/14.txt') as f:
#     rows = f.read()
# rows = rows.split('\n\n')

rows = shared.getInput('14.txt')


rows = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''.split('\n')




def rotateArray(array):
    rotated = []
    for thing in list(zip(*array[::-1])):
        modified = ''.join(list(''.join(list(thing))))
        rotated.append(modified)
    return rotated


def tilt(rotated):
    new_map = []
    for row in rotated:
        split_row = row.split('#')
        modified_row = []
        for thing in split_row:
            if thing == '':
                modified_row.append('')
            elif 'O' in thing:
                length = len(thing)
                o_count = thing.count('O')
                other = f'{"."*(length-o_count)}{"O"*o_count}'
                modified_row.append(other)
            elif '.' in thing:
                modified_row.append(thing)
        new_map.append('#'.join(modified_row))
    return new_map



new_map = tilt(rotateArray(rows))
pprint(new_map)
print('\n')
for i in range(10):
    if i % 1000000 == 0:
        print(i)
    new_map = tilt(rotateArray(new_map))
    pprint(new_map)
    input()


# rotated = rotateArray(new_map)
# rotated = rotateArray(rotated)
# rotated = rotateArray(rotated)


height = len(rows)

total = 0
count = 0
for i in range(height, 0, -1):
    total += new_map[count].count('O') * i
    count += 1
print(total)