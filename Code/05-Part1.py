#! python3

import shared
import time
start_time = time.time()

with open('../Input/05.txt', 'r') as f:
    input_text = f.read()

rows = input_text.split('\n\n')

seeds = [int(x) for x in rows.pop(0).split(': ')[-1].split()]

# If the number we have is in the range of numbers passed in
def isInRange(check, numbers):
    _, source, span = [int(x) for x in numbers.split()]

    try:
        range(source, source+span).index(check)
        return True
    except:
        return False
    
# For the given source number, give me the corresponding destination number
def getDestinationFromSource(check, numbers):
    destination, source, span = [int(x) for x in numbers.split()]

    try:
        source_index = range(source, source+span).index(check)
        return range(destination, destination+span)[source_index]
    except:
        return False

# For the given number, give me the destination considering all ranges in the map
def getMapping(check, numbers):
    is_in_range = False
    range_found = 0
    for index, num in enumerate(numbers):
        if isInRange(check, num):
            is_in_range = True
            range_found = index

    if is_in_range:
        return getDestinationFromSource(check, numbers[range_found])
    return check



# Create a dictionary with all the maps and their corresponding data values
data_dict = {}
for row in rows:
    category = row.split(':')[0].split()[0]
    data = row.split(':\n')[-1].split('\n')
    data_dict[category] = {}
    data_dict[category]['map'] = data


# For all the seeds, determine their locations and add them to a list so we can print the minimum
nums = []
for seed in seeds:
    next_num = seed
    for k,v in data_dict.items():
        values_array = v['map']
        next_num = getMapping(next_num, values_array)
    nums.append(next_num)

print(min(nums))
print(f'Ran in {time.time()-start_time} seconds')