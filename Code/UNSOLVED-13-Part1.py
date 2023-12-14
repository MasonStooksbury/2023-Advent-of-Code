import shared
import re
import copy
from pprint import pprint
from itertools import product
import time
start_time = time.time()

rows = ''
with open('../Input/13.txt') as f:
    rows = f.read()
rows = rows.split('\n\n')


# rows = '''#.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#'''.split('\n\n')


# rows = '''#....#..#....##..
# #..###..###..##..
# .###..##..###..##
# ###..#..#..######
# ##....##....####.
# .#.#..##..#.#..#.
# ..###.##.###....#
# #..#..##.##..##..
# ####.#..#.#######
# .####.##.####..##
# ####......#######'''.split('\n\n')


# rows = '''..###.##.
# ..##.##..
# ...#.....
# ##.#.###.
# ..##.#.##
# ..##.....
# ..#...###
# ###...#.#
# ###...#.#
# ..#...###
# ..##..#..'''.split('\n\n')


# rows = '''.#..#.##.##
# #.#......#.
# ...#.###.##
# ...#.###.##
# #.#......#.
# .#..#.##.##
# #####.##.##
# ....#####..
# ###...#..##
# #.#..##..#.
# .#.######.#
# ##.##.####.
# #.#####..##
# ##.####.###
# ##..#.#.##.
# ##....#.##.
# ##.####.###'''.split('\n\n')


def hasMatch(puzzle):
    puzzle_width = len(puzzle)
    # puzzle_width = len(puzzle) if puzzle_type == 'as_columns' else len(puzzle[0])

    for i in range(len(puzzle)):
        puzzle_copy = puzzle[i:]
        match_found = False
        match_count = 0
        for index, row in enumerate(puzzle_copy):
            if row != puzzle_copy[len(puzzle_copy)-1-index]:
                break
            else:
                match_count += 1
            if match_count == len(puzzle_copy)//2:
                match_found = True
        if match_found:
            # print(len(puzzle), match_count)
            # return [True, [match_count, match_count+1]]
            second_index = (i + (puzzle_width-i)//2)
            return [True, [second_index, second_index+1]]
            # first_index = (puzzle_width+1)//2
            # return [True, [first_index, first_index+1]]
    for i in range(len(puzzle),0,-1):
        puzzle_copy = puzzle[:i]
        match_found = False
        match_count = 0
        for index, row in enumerate(puzzle_copy):
            if row != puzzle_copy[len(puzzle_copy)-1-index]:
                break
            else:
                match_count += 1
            if match_count == len(puzzle_copy)//2:
                match_found = True
        if match_found:
            # return [True, [match_count, match_count+1]]
            first_index = i//2
            return [True, [first_index, first_index]]
            # first_index = (puzzle_width-1)//2
            # return [True, [first_index, first_index+1]]
    return False, []



    
    # puzzle_copy = copy.deepcopy(puzzle)
    # puzzle_copy.pop(0)
    # match_found = False
    # match_count = 0
    # for index, row in enumerate(puzzle_copy):
    #     if row != puzzle_copy[len(puzzle_copy)-1-index]:
    #         break
    #     else:
    #         match_count += 1
    #     if match_count == len(puzzle_copy)//2:
    #         match_found = True
    # if match_found:
    #     first_index = (puzzle_width+1)//2
    #     return [True, [first_index, first_index+1]]
    
    # puzzle_copy = copy.deepcopy(puzzle)
    # puzzle_copy.pop()
    # match_found = False
    # match_count = 0
    # for index, row in enumerate(puzzle_copy):
    #     if row != puzzle_copy[len(puzzle_copy)-1-index]:
    #         break
    #     else:
    #         match_count += 1
    #     if match_count == len(puzzle_copy)//2:
    #         match_found = True
    # if match_found:
    #     first_index = (puzzle_width-1)//2
    #     return [True, [first_index, first_index+1]]
    # return False, []



    # for i in range(len(puzzle)):
    #     copyy = copy.deepcopy(puzzle)
    #     copyy.pop(i)
    #     match_count = 0
    #     for index, row in enumerate(copyy):
    #         if row != copyy[len(copyy)-1-index]:
    #             break
    #         else:
    #             match_count += 1
    #         if match_count == len(copyy)//2:
    #             return True
    # return False







puzzles = {}
for index, row in enumerate(rows):
    map_as_rows = row.split('\n')
    # Rotate the map clockwise once, then reverse. This gives us all the columns as rows
    map_as_columns = []
    map_as_rows_copy = copy.deepcopy(map_as_rows)
    for thing in list(zip(*map_as_rows_copy[::-1])):
        map_as_columns.append(''.join(list(reversed(''.join(list(thing))))))

    # Add to dictionary
    puzzles[index] = {'as_rows': map_as_rows, 'as_columns': map_as_columns}



total_columns = 0
total_rows = 0
for k,v in puzzles.items():
    # print('fuck', k)
    thing, nums = hasMatch(v['as_columns'])
    other_thing, other_nums = hasMatch(v['as_rows'])
    if thing:
        print(thing, nums)
        total_columns += nums[0]
    if other_thing:
        print(other_thing, other_nums)
        total_rows += other_nums[0]


print((total_rows * 100) + total_columns)

# pprint(hasMatch(puzzles[0]['as_columns']))
# pprint(hasMatch(puzzles[1]['as_rows']))