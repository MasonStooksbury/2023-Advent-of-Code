#! python3

seed = 79
numbers = '52 50 48'

destination, source, span = [int(x) for x in numbers.split()]

print(range(source, source+span).index(seed))

if seed in range(source, source+span):
    print(range(source, source+span).index(seed))
