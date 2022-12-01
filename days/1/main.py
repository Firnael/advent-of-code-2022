import os
import sys

example = len(sys.argv) >= 2 and sys.argv[1] == 'example'
path_to_file = 'data_example' if example else 'data'
data = []

with open(os.path.join(os.path.dirname(__file__), path_to_file + '.txt'), 'r') as f:
    [data.append(line.strip()) for line in f.readlines()]

if example:
    print(f'Data {data}')

# Part one
elves_calories = []
acc = 0
for x in data:
    if not x: # string is empty
        elves_calories.append(acc)
        acc = 0
    else:
        acc += int(x)
elves_calories.append(acc) ## add last elf

elves_calories.sort(reverse=True)

print(f'Part ONE solution: ', elves_calories[0])

# Part two
print(f'Part TWO solution: ', elves_calories[0] + elves_calories[1] + elves_calories[2])