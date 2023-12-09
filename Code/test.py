#! python3


instruction = 0

for thing in range(10):
    instruction %= instruction + 2
    print(instruction)