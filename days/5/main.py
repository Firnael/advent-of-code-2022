# Day 5
import functools
import re
import copy

from utils.file_reader import read
data = read(__file__, False) # do not strip lines

# count stacks (one crate every 4 characters)
stack_count = int(len(data[0]) / 4)

# parse file
stacks = [[] for _ in range(stack_count)]
instructions = []
separator_index = 0
for i, x in enumerate(data):
    if separator_index > 0: # fill instructions
        instructions.append(x.strip())
    elif len(x.strip()) == 0: # blank line, set separator index
        separator_index = i
    elif x.strip()[0] == '1': # separator line (crates numbers), ignore
        continue
    else: # fill stacks
        stack_index = 1
        for y in range(stack_count):
            i2 = y + stack_index
            if x[i2] != ' ':
                stacks[y].append(x[i2])
            stack_index += 3

stacksP1 = copy.deepcopy(stacks)
stacksP2 = copy.deepcopy(stacks)
for x in instructions:
    parsed = re.search(r"(move (\d+) from (\d+) to (\d+))", x)
    w = int(parsed.groups()[1])
    f = int(parsed.groups()[2])
    t = int(parsed.groups()[3])
    # part one
    for y in range(w):
        stacksP1[t-1].insert(0, stacksP1[f-1].pop(0))
    # part two
    crates = []
    for y in range(w):
        crates.append(stacksP2[f-1].pop(0))
    reversed = crates.reverse()
    for z in crates:
        stacksP2[t-1].insert(0, z)

print(f'Part one solution : {functools.reduce(lambda a, b: a+b, [x[0] for x in stacksP1])}')
print(f'Part two solution : {functools.reduce(lambda a, b: a+b, [x[0] for x in stacksP2])}')