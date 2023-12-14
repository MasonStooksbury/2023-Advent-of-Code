import shared
import re
import copy
from pprint import pprint
from itertools import product
import time
start_time = time.time()


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



# Rotates the array clockwise one time
def rotateArray(array):
    rotated = []
    for thing in list(zip(*array[::-1])):
        modified = ''.join(list(''.join(list(thing))))
        rotated.append(modified)
    return rotated

# Shifts all the rocks to the right
def moveRocks(rotated):
    new_map = []
    for row in rotated:
        # We can cheat by splitting on the #, moving things in their respective string, and then joining back on #
        split_row = row.split('#')
        modified_row = []
        # For each piece of the recreate the split_row but with modified strings
        for thing in split_row:
            if thing == '':
                modified_row.append('')
            # For something like '..OO.O.', this will convert it to '....OOO'
            elif 'O' in thing:
                o_count = thing.count('O')
                modified_row.append(f'{"."*(len(thing)-o_count)}{"O"*o_count}')
            elif '.' in thing:
                modified_row.append(thing)
        # By splitting on the # we essentially preserved where they should be. Joining the strings back together will give us the completed row
        new_map.append('#'.join(modified_row))
    return new_map


# Rotate the map one time and move the rocks to move things "north". The put it back by rotating 3 more times
#       (no, I don't wanna waste time writing an algorithm to undo it)
rotated = rotateArray(rotateArray(rotateArray(moveRocks(rotateArray(rows)))))


total = 0
count = 0
for i in range(len(rows), 0, -1):
    total += rotated[count].count('O') * i
    count += 1
print(total)