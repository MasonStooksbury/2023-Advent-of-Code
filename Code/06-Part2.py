import shared

# Get the times and distances separate
time, distance = shared.getInput('06.txt')

# Get all the times, combine them, and convert to a number
available_time = int(''.join(time.split()[1:]))
# Get all the distances, combine them, and convert to a number
record = int(''.join(distance.split()[1:]))

# Do the math
total = 0
for t in range(available_time):
    if (t * (available_time - t)) > record:
        total += 1

print(total)
