import shared
import time
start_time = time.time()

# Get the times and distances separate
time, distance = shared.getInput('06.txt')

# Separate the times, put them in an array, and make sure they're all numbers
times = [int(x) for x in time.split()[1:]]
# Separate the distances, put them in an array, and make sure they're all numbers
distances = [int(x) for x in distance.split()[1:]]

# Zip the times and distances together so we have them beside one another
scores = list(zip(times, distances))


# Do the math
total = 1
for score in scores:
    ways_to_win = 0
    for t in range(score[0]):
        left = score[0] - t
        hold = t

        distance = hold * left
        if distance > score[1]:
            ways_to_win += 1
    total *= ways_to_win

print(time.time()-start_time)
print(total)
