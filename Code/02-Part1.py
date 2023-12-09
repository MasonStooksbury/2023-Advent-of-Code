import shared
import re

games = shared.getInput('02.txt')

total = 0

# Checks to see if we've exceeded the maximum for a given color
def exceedsMax(number, color):
    number = int(number)
    match color:
        case 'red': return number > 12
        case 'green': return number > 13
        case 'blue': return number > 14
    

# Iterate over the games
for game in games:
    # Isolate the game ID
    game_id = int(game.split(':')[0].split(' ')[-1])

    # Isolate all "pulls" (with semicolons)
    # Looks like: 7 green, 4 blue, 3 red; 4 blue, 10 red, 1 green; 1 blue, 9 red
    pulls = game.split(': ')[-1]
    
    # Replace all the ; with , and throw it into an array
    # Looks like: [7 green, 4 blue, 3 red, 4 blue, 10 red, 1 green, 1 blue, 9 red]
    pulls = re.sub(';', ',', ''.join(pulls)).split(', ')

    # Loop through all the pulls, if anything exceeds the max, mark and ignore it
    # If the game is good (all pulls pass), add that game ID to the total
    is_good = True
    for pull in pulls:
        number, color = pull.split()
        if exceedsMax(number, color):
            is_good = False
            break
    if is_good:
        total += game_id
        
print(total)
