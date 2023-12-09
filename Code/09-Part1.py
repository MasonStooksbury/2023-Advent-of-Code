import shared

rows = shared.getInput('09.txt')

##
##rows = '''0 3 6 9 12 15
##1 3 6 10 15 21
##10 13 16 21 30 45'''.split('\n')

#rows = [0, 3, 6, 9, 12, 15]


def getSubNums(array):
    subs = []
    for index, num in enumerate(array):
        if index + 1 > len(array)-1:
            break
        subs.append(array[index+1] - num)
    return subs

def isArrayZeros(array):
    thing = list(set(array))
    return len(thing) == 1 and thing[0] == 0


def isEverythingZeros(array):
    for thing in array:
        if not isArrayZeros(thing):
            return False
    return True



total = 0
for row in rows:
    row = [int(x) for x in row.split()]
    all_subs = [row]
    next_sub = row
    while not isArrayZeros(next_sub):
        next_sub = getSubNums(next_sub)
        all_subs.append(next_sub)
    for array in all_subs:
        total += array[-1]
    
print(total)
