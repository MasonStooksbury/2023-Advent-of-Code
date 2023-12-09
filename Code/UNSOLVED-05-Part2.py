#! python3

import shared
import time
start_time = time.time()

input_text = shared.getInput('05.txt')

with open('../Input/05.txt', 'r') as f:
    input_text = f.read()

# input_text ='''seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4'''

rows = input_text.split('\n\n')

seeds = [int(x) for x in rows.pop(0).split(': ')[-1].split()]

def isInRange(check, numbers):
    _, source, span = [int(x) for x in numbers.split()]

    # try:
    #     range(source, source+span).index(check)

    #     return True
    # except:
    #     return False
    return True if check >= source and check <= (source + span) else False
    
def getDestinationFromSource(check, numbers):
    destination, source, span = [int(x) for x in numbers.split()]

    try:
        source_index = range(source, source+span).index(check)
        return range(destination, destination+span)[source_index]
    except:
        return False


def getDestination(check, numbers):
    is_in_range = False
    range_found = 0
    for index, num in enumerate(numbers):
        if isInRange(check, num):
            is_in_range = True
            range_found = index
            break

    
    if is_in_range:
        return getDestinationFromSource(check, numbers[range_found])
    return check




data_dict = {}
for row in rows:
    category = row.split(':')[0].split()[0]
    data = row.split(':\n')[-1].split('\n')
    data_dict[category] = {}
    data_dict[category]['map'] = data


all_minimums = []
new_seeds = []

things = []
while len(seeds) != 0:
    val1 = seeds.pop(0)
    val2 = seeds.pop(0)
    things.append({'seed': val1, 'span': val2})

print(things)
input()


data_dict['seed-to-soil']

# while len(seeds) != 0:
#     val1 = seeds.pop(0)
#     val2 = seeds.pop(0)

#     nums = []
#     for seed in range(val1, val1+val2):
#         next_num = seed
#         for k,v in data_dict.items():
#             values_array = v['map']
#             next_num = getDestination(next_num, values_array)
#         nums.append(next_num)
#     all_minimums.append(min(nums))
#     print(min(nums))
    

print(min(all_minimums))
print(f'Ran in {time.time()-start_time} seconds')