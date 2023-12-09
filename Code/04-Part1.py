import shared

cards = shared.getInput('04.txt')

total = 0

for card in cards:
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

    if matches != 0:
        total += 2 ** (matches - 1)
    

print(total)
