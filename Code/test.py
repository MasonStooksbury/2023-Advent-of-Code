
multiplier = 1000000

first_num = 44
first_string = 'C'*(first_num-1) + 'Z'

second_num = 48
second_string = 'C'*(second_num-1) + 'Z'

third_num = 54
third_string = 'C'*(third_num-1) + 'Z'

fourth_num = 60
fourth_string = 'C'*(fourth_num-1) + 'Z'

fifth_num = 62
fifth_string = 'C'*(fifth_num-1) + 'Z'

sixth_num = 68
sixth_string = 'C'*(sixth_num-1) + 'Z'

things = [len(first_string), len(second_string), len(third_string), len(fourth_string), len(fifth_string), len(sixth_string)]
total = 1
for thing in things:
    num = thing*thing
    total *= num
print(total)
input()


first = first_string*multiplier
second = second_string*multiplier
third = third_string*multiplier
fourth = fourth_string*multiplier
fifth = fifth_string*multiplier
sixth = sixth_string*multiplier

stuff = list(zip(first,second,third,fourth,fifth,sixth))

#4 5 7 6
#17 10 11 9
#54 36 44 38 26  293436
#25 18 22 29 26  1866150
#44, 48, 54, 60, 62    736560
#44 48 54 60 62 68     12521520
#45 49 55 61 63 69    34029765



print(len(first_string), len(second_string), len(third_string), len(fourth_string), len(fifth_string), len(sixth_string), end='')
count = 0
check = tuple('Z'*len(''.join(stuff[0])))
for thing in stuff:
    count += 1
    if thing == check:
        found = True
        break
if found:
    print(f'     {count}')
else:
    print('Not found')