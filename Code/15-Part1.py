import shared
from pprint import pprint

rows = shared.getInput('15.txt')[0]

# Return the hash for a given string
def getHash(string):
    current_value = 0
    for character in string:
        current_value += ord(character)
        current_value *= 17
        current_value %= 256
    return current_value


total = 0
for thing in rows.split(','):
    total += getHash(thing)
print(total)