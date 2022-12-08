# Day 8
from utils.file_reader import read
data = read(__file__)

# for debug
def pretty_print(grid):
    for line in grid:
        print(line)

# for P1
def check_visibility(index, values):
    value = values[index]
    # check left, then right directions if all values are below our tree value
    if all([x < value for x in values[:index]]) or all([x < value for x in values[index+1:]]):
        return True
    return False

# for P2
def compute_scenic_score(v, l_i, line, c_i, column):
    up, left, down, right = 0, 0, 0, 0
    for x in list(reversed(line[:c_i])): # left
        left += 1
        if x >= v:
            break
    for x in line[c_i+1:]: # right
        right += 1
        if x >= v:
            break
    for x in list(reversed(column[:l_i])): # up
        up += 1
        if x >= v:
            break
    for x in column[l_i+1:]: # down
        down += 1
        if x >= v:
            break
    return up * left * down * right

# put input into grid & create bitmap
length = len(data[0])
grid = []
bitmap = []
for i, line in enumerate(data):
    grid.append(list([int(l) for l in line]))
    bitmap.append(list([1 if i == 0 or i == len(data)-1 or j == 0 or j == len(line)-1 else 0 for j, l in enumerate(line)]))

# lezgong
visible_trees_count = 0
best_scenic_score = 0
for i, x in enumerate(grid): # lines
    for j, y in enumerate(grid[i]): # columns
        # part one
        if bitmap[i][j] != 1: # do not recheck
            h_check = check_visibility(j, x) # x is a line
            if not h_check: # not visible horizontally, check vertically
                column = list([grid[x][j] for x in range(0, length)])
                v_check = check_visibility(i, column)
                if v_check:
                    bitmap[i][j] = 1
            else:
                bitmap[i][j] = 1
        if bitmap[i][j] == 1:
            visible_trees_count += 1
        # part two
        scenic_score = compute_scenic_score(grid[i][j], i, x, j, list([grid[l][j] for l in range(0, length)]))
        best_scenic_score = scenic_score if scenic_score > best_scenic_score else best_scenic_score

print(f'Part one solution : {visible_trees_count}')
print(f'Part two solution : {best_scenic_score}')