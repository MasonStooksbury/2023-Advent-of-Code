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