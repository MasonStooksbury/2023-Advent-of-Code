#! python3
import shared

map_input = shared.getInput('08.txt')

# Separate instructions and nodes
instructions = map_input[0]
nodes = map_input[2:]

# Create a dictionary of nodes with their corresponding L and R destination nodes
node_dict = {}
for node in nodes:
    position = node.split(' = ')[0]
    left = node.split(' = (')[-1].split(',')[0]
    right = node.split(', ')[-1][:-1]
    node_dict[position] = {'L': left, 'R': right}

# Start at AAA and go until we end up at ZZZ. If we don't find it on the first pass of all instructions, go around again
value = 'AAA'
count = 1
while value != 'ZZZ':
    for instruction in instructions:
        value = node_dict[value][instruction]
        if value == 'ZZZ':
            break
        count += 1
print(count)