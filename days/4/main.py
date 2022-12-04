# Day 4
from utils.file_reader import read
data = read(__file__)

countP1 = 0
countP2 = 0
for x in data:
    elves = x.split(",")
    a = list(map(lambda x: int(x), elves[0].split("-")))
    b = list(map(lambda x: int(x), elves[1].split("-")))

    # part one
    if a[0] == b[0]:
        countP1 += 1
    elif a[0] < b[0]:
        if a[1] >= b[1]:
            countP1 += 1
    else: # a[0] > b[0]
        if a[1] <= b[1]:
            countP1 += 1

    # part two
    if a[0] == b[0] or a[1] == b[1] or a[0] == b[1] or a[1] == b[0]: # same start or same end
        countP2 += 1
    elif a[0] < b[0] and a[1] > b[0]: # a1 b1 a2 b2 
        countP2 += 1
    elif a[0] > b[0] and a[0] < b[1]: # b1 a1 a2 b2
        countP2 += 1
    elif a[0] > b[0] and a[0] < b[1]: # b1 a1 b2 a2
        countP2 += 1
    elif a[0] < b[0] and a[1] > b[1]: # a1 b1 b2 a2
        countP2 += 1
    
print(f'Part one solution : {countP1}')
print(f'Part two solution : {countP2}')