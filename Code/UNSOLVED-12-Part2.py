import shared
import re
import copy
from pprint import pprint
from itertools import product
import time
start_time = time.time()
rows = shared.getInput('12.txt')

rows = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''.split('\n')


def filler(word, from_char, to_char):
    options = [(c,) if c != from_char else (from_char, to_char) for c in word]
    return (''.join(o) for o in product(*options))


def getCombinationCount(record, numbers):
    count = 0
    for thing in filler(record, "?", "#"):
        if [len(x) for x in re.findall(r"[\#]+", thing) if x != ''] == numbers:
            count += 1
    return count




data = {}
count = 0
for row in rows:
    record, numbers = row.split()
    original_record = record
    original_numbers = numbers
    for x in range(4):
        record += f'?{original_record}'
        numbers += f',{original_numbers}'
    data[count] = {'record': record, 'numbers': [int(x) for x in numbers.split(',')]}
    count += 1


total = 0
for k,v in data.items():
    print(k)
    total += getCombinationCount(v['record'], v['numbers'])

print(total)
print(f'Ran in {time.time()-start_time} seconds')






