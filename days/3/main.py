# Day 3
from utils.file_reader import read
data = read(__file__)

# create priority dict
mapping = dict()
for x in range(1, 27):
    upper_case_offset = 64 # ascii code for 'A' is 65
    lower_case_offset = 96 # ascii code for 'a' is 97
    mapping[chr(x + upper_case_offset)] = x + 26
    mapping[chr(x + lower_case_offset)] = x

# part one
value = 0
for x in data:
    half = int(len(x) / 2)
    first_compartment = x[:half]
    second_compartment = x[half:int(len(x))]
    # find item in both compartments
    for i in first_compartment:
        if i in second_compartment:
            # add mapped value to the score
            value += mapping[i]
            break
print(f'Part one solution : {value}')

# part two
value = 0
group = []
for x in data:
    group.append(x)
    if len(group) == 3:
        # find common item
        for i in group[0]:
            if i in group[1] and i in group[2]:
                # add mapped value to the score
                value += mapping[i]
                # reset group buffer
                group = []
                break
print(f'Part two solution : {value}')