fuck = 'cd9 fg8 ht0 ji3'
# fuck = 'cd9 fg8 ji3 ht0'
label = 'ht0'
value = '0'
index = fuck.find(label)
thing = fuck[:index-1] + fuck[index + len(label) + 1:]

# thing = fuck[:index] + f'{label}{value}' + fuck[index + len(label) + 1:]

# fuck = 'cd9 fg8 ht0 ji3'
fuck = 'cd9 fg8 ji3 ht0'
fuck = fuck.split()
label = 'ht0'
value = '0'
index = fuck.index(label)
del fuck[index]





thing = ' '.join(fuck)
print(thing)
print(f'--{thing}--')
input()



thing = [1,2,3]
shit = [3,2,1]

print(thing == shit)



# first_num = 44
# second_num = 48
# third_num = 54
# fourth_num = 60
# fifth_num = 62
# sixth_num = 68

print(20000 % 10000)
input()



multiplier = 1000000

first_num = 8
first_string = 'C'*(first_num-1) + 'Z'

second_num = 2
second_string = 'C'*(second_num-1) + 'Z'

third_num = 6
third_string = 'C'*(third_num-1) + 'Z'

fourth_num = 5
fourth_string = 'C'*(fourth_num-1) + 'Z'

fifth_num = 62
fifth_string = 'C'*(fifth_num-1) + 'Z'

sixth_num = 68
sixth_string = 'C'*(sixth_num-1) + 'Z'

things = [len(first_string), len(second_string), len(third_string), len(fourth_string)]
# things = [len(first_string), len(second_string), len(third_string), len(fourth_string), len(fifth_string), len(sixth_string)]
# total = 1
# for thing in things:
#     num = thing*thing
#     total *= num
# print(total)
# input()


first = first_string*multiplier
second = second_string*multiplier
third = third_string*multiplier
fourth = fourth_string*multiplier
fifth = fifth_string*multiplier
sixth = sixth_string*multiplier

stuff = list(zip(first,second,third,fourth))
# stuff = list(zip(first,second,third,fourth,fifth,sixth))

# 4 5 7 6
# 17 10 11 9
# 54 36 44 38 26  293436
# 25 18 22 29 26  1866150
# 44, 48, 54, 60, 62    736560
# 44 48 54 60 62 68     12521520
# 45 49 55 61 63 69    34029765
# 9 2 6 5         90



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