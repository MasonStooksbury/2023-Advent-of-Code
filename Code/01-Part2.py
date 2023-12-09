import shared
import re

rows = shared.getInput('01.txt')

numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
    }

def getNumsAndPositions(row):
    first_num = None
    first_num_index = None
    for index, num in enumerate([*row]):
        try:
            first_num = int(num)
            first_num_index = index
            break
        except:
            continue

    if first_num is None:
        return None

    last_num = None
    last_num_index = None
    for index, num in enumerate([*row]):
        try:
            last_num = int(num)
            last_num_index = index
        except:
            continue
    
    if last_num is None:
        last_num = first_num
        last_num_index = first_num_index

    return {'first': first_num, 'first_position': first_num_index,
            'last': last_num, 'last_position': last_num_index}


total = 0

# For every row in input text
for row in rows:
    nums = getNumsAndPositions(row)

    # Hunt for the first "word-like" number
    first_word_number = ''
    first_word_position = 9999999999
    for k,v in numbers.items():
        res = re.search(k, row)
        if res is not None:
            res.group()
            if res.start() < first_word_position:
                first_word_number = v
                first_word_position = res.start()

    # Hunt for the last "word-like" number
    last_word_number = ''
    last_word_position = 0
    for k,v in numbers.items():
        res = re.search(k, row)
        if res is not None:
            last_occurence = row.rfind(res.group())
            if last_occurence > last_word_position:
                last_word_number = v
                last_word_position = last_occurence

    # If we don't have a last word-like number, just make it match the first
    if not last_word_number:
        last_word_number = first_word_number
        last_word_position = first_word_position


    final_thing = {'first': '', 'last': ''}


    # If we don't have any actual numbers, we definitely have some word-like numbers
    if nums is None:
        total += int(f'{first_word_number}{last_word_number}')
        continue

    # If we have numbers and word-like ones, figure out which ones came first and last
    if nums and first_word_number and last_word_number:
        if nums['first_position'] < first_word_position:
            final_thing['first'] = nums['first']
        elif first_word_position < nums['first_position']:
            final_thing['first'] = first_word_number

        if nums['last_position'] > last_word_position:
            final_thing['last'] = nums['last']
        elif last_word_position > nums['last_position']:
            final_thing['last'] = last_word_number
        total += int(f'{final_thing["first"]}{final_thing["last"]}')
        continue

    # If we only have actual numbers (and no word-like ones)
    total += int(f'{nums["first"]}{nums["last"]}')

print(total)









