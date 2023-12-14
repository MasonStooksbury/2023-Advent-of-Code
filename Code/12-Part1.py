from itertools import product
import re
import shared

rows = shared.getInput('12.txt')

# rows = '''???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1'''.split('\n')



# Create all permutations of # substituted for ?
def filler(word, from_char, to_char):
    options = [(c,) if c != from_char else (from_char, to_char) for c in word]
    return (''.join(o) for o in product(*options))



# For a given record and set of numbers, figure out how many valid combinations it has
def getCombinationCount(record, numbers):
    count = 0
    for thing in filler(record, "?", "#"):
        if [len(x) for x in re.findall(r"[\#]+", thing) if x != ''] == numbers:
            count += 1
    return count



# Separate all our input data into a dictionary with the record string and numbers as an array
data = {}
count = 0
for row in rows:
    record, numbers = row.split()
    data[count] = {'record': record, 'numbers': [int(x) for x in numbers.split(',')]}
    count += 1


# For all rows, keep a running total of the combination count
total = 0
for k,v in data.items():
    total += getCombinationCount(v['record'], v['numbers'])

print(total)







