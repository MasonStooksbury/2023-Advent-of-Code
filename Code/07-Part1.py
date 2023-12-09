import shared
from pprint import pprint


rows = shared.getInput('07.txt')


types = {'five': 6,
         'four': 5,
         'full': 4,
         'three': 3,
         'two': 2,
         'one': 1,
         'high': 0
         }

labels = {'A': 12,
          'K': 11,
          'Q': 10,
          'J': 9,
          'T': 8,
          '9': 7,
          '8': 6,
          '7': 5,
          '6': 4,
          '5': 3,
          '4': 2,
          '3': 1,
          '2': 0,
          }



def getWinner(card1, card2):
    for index, card in enumerate(card1['hand']):
        if labels[card] < labels[card2['hand'][index]]:
            return True
        elif labels[card] == labels[card2['hand'][index]]:
            continue
        return False # This is important, will affect final value

def bubblesort(elements):
    swapped = False
    # Looping from size of array from last index[-1] to index [0]
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if getWinner(elements[i], elements[i + 1]):
                swapped = True
                # Swapping data if the element is less than next element in the array
                elements[i], elements[i + 1] = elements[i + 1], elements[i]        
        if not swapped:
            # Exiting the function if we didn't make a single swap
            # Meaning that the array is already sorted
            return

def getType(hand):
    dedupe = list(set(hand))
    dedupe_length = len(dedupe)
    
    if dedupe_length == 1:
        return 'five'
    elif dedupe_length == 5:
        return 'high'
    elif dedupe_length == 4:
        return 'one'
    # Either full house or four of a kind
    elif dedupe_length == 2:
        if hand.count(dedupe[0]) == 2 or hand.count(dedupe[0]) == 3:
            return 'full'
        else:
            return 'four'
    # Either two pair or three of a kind
    elif dedupe_length == 3:
        if hand.count(dedupe[0]) == 3 or hand.count(dedupe[1]) == 3 or hand.count(dedupe[2]) == 3:
            return 'three'
        else:
            return 'two'


hands_by_types_dict = {'five': [],
         'four': [],
         'full': [],
         'three': [],
         'two': [],
         'one': [],
         'high': []
         }

# Populate the dictionary with the hands
for row in rows:
    hand, bid = row.split()
    hand_type = getType(hand)
    
    hands_by_types_dict[hand_type].append({'hand': hand, 'bid': int(bid), 'rank': 0, 'type': hand_type})


# Bubblesort each type array, then add that to the final array to create a fully-sorted array of hands
final_array = []
for hand_type, cards in hands_by_types_dict.items():
    if cards:
        bubblesort(cards)
        final_array += cards

# Multiply the bid by the rank and add that to the total
count = 1
total = 0
for x in range(len(final_array)-1, -1, -1):
    total += final_array[x]['bid'] * count
    count += 1

print(total)
