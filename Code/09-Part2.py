import shared

rows = shared.getInput('09.txt')


# For a given array, return the array of differences between the elements
def getSubNums(array):
    subs = []
    for index, num in enumerate(array):
        if index + 1 > len(array)-1:
            break
        subs.append(array[index+1] - num)
    return subs

# For a given array, return whether or not the entire array is 0s
def isArrayZeros(array):
    thing = list(set(array))
    return len(thing) == 1 and thing[0] == 0


total = 0
for row in rows:
    # Go backwards because it's basically the same as going the other way
    row = list(reversed([int(x) for x in row.split()]))
    # Start by adding the last number
    total += row[-1]
    # Contains a row, and all subsequent rows of differences
    all_subs = [row]
    next_sub = row
    while not isArrayZeros(next_sub):
        next_sub = getSubNums(next_sub)
        all_subs.append(next_sub)
        total += next_sub[-1]
    
print(total)
