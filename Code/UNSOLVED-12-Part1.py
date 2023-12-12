import shared
import copy
from pprint import pprint

rows = shared.getInput('11.txt')

rows = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''.split('\n')

def getPermutationCount(record, numbers):
    pass




data = {}
count = 0
for row in rows:
    record, numbers = row.split()
    data[count] = {'record': record, 'numbers': numbers.split(',')}
    count += 1

test_data = {0: {'record': '?###????????', 'numbers': [3,2,1]}}

# print([x for x in '.#...#....###'.split('.') if x != ''])

string = '?###????????'
numbers = [3,2,1]



