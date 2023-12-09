import shared
import re

games = shared.getInput('02.txt')

##games = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
##Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
##Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
##Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
##Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''.split('\n')

total = 0
game_total = 1

# Iterate over the games
for game in games:
    game_total = 1
    # Isolate the game ID
    game_id = int(game.split(':')[0].split(' ')[-1])

    # Isolate all "pulls" (with semicolons)
    # Looks like: 7 green, 4 blue, 3 red; 4 blue, 10 red, 1 green; 1 blue, 9 red
    pulls = game.split(': ')[-1]
    
    # Replace all the ; with , and throw it into an array
    # Looks like: [7 green, 4 blue, 3 red, 4 blue, 10 red, 1 green, 1 blue, 9 red]
    pulls = re.sub(';', ',', ''.join(pulls)).split(', ')

    colors_dict = {
        'red': [],
        'green': [],
        'blue': []
    }

    # For each pull in a game, put it in the correct place in the dictionary
    for pull in pulls:
        number, color = pull.split()
        colors_dict[color].append(int(number))

    # Iterate over each color, sort the array to put the largest number on one end
    #       then multiplicatively add that number to the game total
    for k,v in colors_dict.items():
        v.sort()
        game_total *= int(v[-1])

    # Add the sum of cubes for this game to the overall total
    total += game_total

print(total)
