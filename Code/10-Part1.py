import shared
from pprint import pprint

rows = shared.getInput('10.txt')

##rows = '''..F7.
##.FJ|.
##SJ.L7
##|F--J
##LJ...'''.split('\n')


width = len(rows[0]) - 1
height = len(rows) - 1



# For a given pair of coordinates, return the surrounding coordinates' symbols from the table
def getNeighbors(coord_pair):
    y, x = coord_pair
    adjacent_coords = []
        

    # Top left corner
    if x == 0 and y == 0:
        adjacent_coords = ['~', (x,y+1), (x+1,y), '~']
    # Top right corner
    elif x == width and y == 0:
        adjacent_coords = ['~', (x,y+1), '~', (x-1,y)]
    # Bottom left corner
    elif x == 0 and y == height:
        adjacent_coords = [(x,y-1), '~', (x+1,y), '~']
    # Bottom right corner
    elif x == width and y == height:
        adjacent_coords = [(x,y-1), '~', '~', (x-1,y)]
    # Left side
    elif x == 0:
        adjacent_coords = [(x,y-1), (x,y+1), (x+1,y), '~']
    # Top side
    elif y == 0:
        adjacent_coords = ['~', (x,y+1), (x+1,y), (x-1,y)]
    # Right side
    elif x == width:
        adjacent_coords = [(x,y-1), (x,y+1), '~', (x-1,y)]
    # Bottom side
    elif y == height:
        adjacent_coords = [(x,y-1), '~', (x+1,y), (x-1,y)]
    # Everywhere else
    else:
        adjacent_coords = [(x,y-1), (x,y+1), (x+1,y), (x-1,y)]

    final = []
    for coord in adjacent_coords:
        if coord == '~':
            final.append(coord)
            continue
        y, x = coord
        final.append(table[x][y])
    return final



valid_neighbors = {
    '|': {'north': 'F7|S', 'south': '|LJS', 'west': '', 'east': ''},
    '-': {'north': '', 'south': '', 'west': 'LF-S', 'east': '7J-S'},
    'L': {'north': 'F7|S', 'south': '', 'west': '', 'east': '7J-S'},
    'J': {'north': 'F7|S', 'south': '', 'west': 'SLF-', 'east': ''},
    '7': {'north': '', 'south': '|LJS', 'west': 'SLF-', 'east': ''},
    'F': {'north': '', 'south': '|LJS', 'west': '', 'east': '7J-S'},
    }



# Based on the current pipe, is the neighbor pipe valid for the given direction?
def isValidNeighbor(current, neighbor, direction):
    if neighbor == '.' or neighbor == '~' or neighbor == 'S':
        return None
    return current in valid_neighbors[neighbor][direction]



# Figure out what the start pipe is
def determineStartPipe(neighbors):
    north, south, east, west = neighbors

    # The logic here is that current is opposite the neighbor (so the first example specifies that
    #       the current is south of the northern neighbor)
    n = isValidNeighbor('S', north, 'south')
    s = isValidNeighbor('S', south, 'north')
    e = isValidNeighbor('S', east, 'west')
    w = isValidNeighbor('S', west, 'east')

    if n and s:
        return '|'
    if n and e:
        return 'L'
    if n and w:
        return 'J'
    if e and s:
        return 'F'
    if e and w:
        return '-'
    if s and w:
        return '7'
    


# Convert text input to a 2D array and set the starting coordinates
starting_coordinates = 0
table = []
for x, row in enumerate(rows):
    columns = []
    for y, column in enumerate(row):
        columns.append(column)
        if column == 'S':
            starting_coordinates = (x, y)
    table.append(columns)


def goDirection(coords, direction):
    x, y = coords
    match direction:
        case 'north':
            if x == 0:
                return None
            return (x-1, y)
        case 'south':
            if x == height:
                return None
            return (x+1, y)
        case 'east':
            if y == width:
                return None
            return (x, y+1)
        case 'west':
            if y == 0:
                return None
            return (x, y-1)



# If we're close to the start, just call it
# The only reason I need this is it's late and I don't want to change other code
def closeToStart(coords):
    x,y = coords
    north = (x, y+1)
    south = (x, y-1)
    east = (x+1,y)
    west = (x-1,y)
    
    if starting_coordinates == north or starting_coordinates == south or starting_coordinates == east or starting_coordinates == west:
        return True
    return False



# Figure out what type of pipe our starting point is
current_symbol = determineStartPipe(getNeighbors(starting_coordinates))
true_directions = ['north', 'south', 'east', 'west']
directions = ['south', 'north', 'west', 'east']
current_position = starting_coordinates
came_from = 0
total = 0
# I'm sorry
while True:
    neighs = []
    # This is super gross, but basically, we know we're done if it's been a while, and we're close to the
    #       starting point. Will break for smaller examples
    if total > 20 and closeToStart(current_position):
        total += 1
        break
    # Create an array of valid neighbors
    #   [False, True, True, False]
    for index, neighbor in enumerate(getNeighbors(current_position)):
        thing = False
        if isValidNeighbor(current_symbol, neighbor, directions[index]):
            thing = True
        neighs.append(thing)
    # For each neighbor, follow only the valid ones that aren't the direction we just came
    for index, neigh in enumerate(neighs):
        # Must be valid and not the direction we just came
        if not neigh or index == came_from:
            continue
        current_position = goDirection(current_position, true_directions[index])
        current_symbol = table[current_position[0]][current_position[1]]
        # Set the direction we came from to the opposite so that the next position's check will be accurate
        came_from = directions.index(true_directions[index])
        break
    total += 1

# Because the loop is closed, the furthest point is the midpoint of the loop. Meaning we can just count EVERY
#       step and divide by 2
print(total//2)
