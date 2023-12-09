#! python3

import shared

rows = shared.getInput('01.txt')

first_number = 0
last_number = 0

total = 0

# For every row in input text
for row in rows:
    first_number = 0
    last_number = 0
    # Hunt for the first number, then stop
    for character in row:
        try:
            first_number = int(character)
            break
        except:
            continue
    # Hunt for the last number, then stop
    for character in reversed(row):
        try:
            last_number = int(character)
            break
        except:
            continue
    
    total += int(f'{first_number}{last_number}')

print(total)
