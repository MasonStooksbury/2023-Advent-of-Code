import shared

rows = shared.getInput('15.txt')[0]

# Return the hash for a given string
def getHash(string):
    current_value = 0
    for character in string:
        current_value += ord(character)
        current_value *= 17
        current_value %= 256
    return current_value


# Loop through everything and do the necessary organizing
hashmap = {}
for thing in rows.split(','):
    label = ''
    value = ''
    # Set the label and value
    if '-' in thing:
        label = thing.split('-')[0]
    else:
        label, value = thing.split('=')
    
    # Figure out the hashed version of the label to use as a key in the dictionary. This will be the box number
    hashed_label = getHash(label)

    # If the box number already exists in the dictionary
    if hashed_label in hashmap.keys():
        # If the value is nothing (i.e. we're removing a lens)
        if value == '':
            # If the label we need to do an operation on is actually in our values, 
            if label in hashmap[hashed_label]:
                # Split the values to make operations a little easier
                split_values = hashmap[hashed_label].split()
                index = 0
                # Find the index of the lens that has our label
                for i, v in enumerate(split_values):
                    if label in v:
                        index = i
                # Remove the lens from the array
                del split_values[index]
                # Join everything back together and save it to the hashmap
                hashmap[hashed_label] = ' '.join(split_values)
        # Else, we're replacing a lens
        else:
            if label in hashmap[hashed_label]:
                # Split the values to make operations a little easier
                split_values = hashmap[hashed_label].split()
                index = 0
                # Find the index of the lens that has our label
                for i, v in enumerate(split_values):
                    if label in v:
                        index = i
                # Remove the lens from the array
                del split_values[index]
                # Add our new lens where we removed the old one
                split_values.insert(index, f'{label}{value}')
                # Join everything back together and save it to the hashmap
                hashmap[hashed_label] = ' '.join(split_values)
            else:
                hashmap[hashed_label] += f'{label}{value}' if len(hashmap[hashed_label]) == 0 else f' {label}{value}'
    # Otherwise, if the first thing is an addition and not an operation, add the box number and the first value
    elif value != '':
        hashmap[hashed_label] = f'{label}{value}'


# Do all the requisite math to get our total 
total = 0
for k,v in hashmap.items():
    for slot, lens in enumerate(v.split()):
        total += (int(k) + 1) * (slot + 1) * int(lens[-1])

print(total)