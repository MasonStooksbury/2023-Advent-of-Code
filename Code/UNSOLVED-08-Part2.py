#! python3
import shared

map_input = shared.getInput('08.txt')


map_input = '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''.split('\n')




def getNext(value, instruction):
    return node_dict[value][instruction]


instructions = map_input[0]
nodes = map_input[2:]

node_dict = {}

for node in nodes:
    position = node.split(' = ')[0]
    left = node.split(' = (')[-1].split(',')[0]
    right = node.split(', ')[-1][:-1]

    node_dict[position] = {'L': left, 'R': right}


starting_positions = []

for key in node_dict.keys():
    if key[-1] == 'A':
        starting_positions.append(key)

def positionsEndInZ(positions):
    for position in positions:
        if position[-1] != 'Z':
            return False
    return True


count = 0
new_positions = starting_positions
outer_break = False
instruction = 0

while not positionsEndInZ(new_positions):
    other = []
    for position in new_positions:
        other.append(node_dict[position][instructions[instruction]])
    instruction += 1
    new_positions = other
    count += 1
    if positionsEndInZ(other):
        outer_break = True
        break
    if instruction > len(instructions) -1:
        instruction = 0

print(count)


# while not positionsEndInZ(new_positions):
#     for instruction in instructions:
#         other = []
#         for position in new_positions:
#             other.append(node_dict[position][instruction])
#         new_positions = other
#         count += 1
#         if positionsEndInZ(other):
#             outer_break = True
#             break
# print(count)