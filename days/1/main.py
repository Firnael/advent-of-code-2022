from utils.file_reader import read 
data, example = read(__file__)

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