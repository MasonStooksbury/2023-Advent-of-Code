import shared

cards_input = shared.getInput('04.txt')


# Create an array of dictionaries that includes the card ID and how many cards it wins
# [{1: 4}, {2: 2}, {3: 2}, {4: 1}, {5: 0}, {6: 0}]
cards = []
for card in cards_input:
    # Isolate the card ID
    card_id = int(card.split(': ')[0].split()[-1])

    # Separate winning numbers and my numbers
    winning_numbers, my_numbers = card.split(': ')[-1].split(' | ')
    # Create an array of strings of just numbers:
    #       ['69', '420', '247']
    winning_numbers = winning_numbers.split()
    my_numbers = my_numbers.split()

    # Figure out how many matches we have
    matches = 0    
    for num in my_numbers:
        if num in winning_numbers:
            matches += 1

    cards.append({card_id: matches})


# Start by adding the number of cards we have (cause there's always at least one of each)
total = len(cards)

def getWinnings(card):
    global cards
    global total
    # If the input is {1: 4}, return these (i.e. the next 4):
    #         |------------------------------|
    # [{1: 4}, {2: 2}, {3: 2}, {4: 1}, {5: 0}, {6: 0}]
    start = list(card.keys())[0]
    end = card[start] + start


    total += len(cards[start:end])
    for card in cards[start:end]:
        getWinnings(card)
    return 


for card in cards:
    getWinnings(card)
    
print(total)
