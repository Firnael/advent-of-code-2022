# Day 7
from functools import reduce
import operator

from utils.file_reader import read
data = read(__file__)

tree = { '/' : {} }
current_directory_path = ['/']
directories = { '/' }
sizes = {}
listing = False

def get_from_tree(complete_path):
    return reduce(operator.getitem, complete_path, tree)

def set_in_tree(complete_path, value):
    get_from_tree(complete_path[:-1])[complete_path[-1]] = value

def compute_directory_size(d):
    counter = 0
    for k in sizes.keys():
        if d in k:
            counter += sizes[k]
    return counter

# build tree
for line in data:
    s = line.split(' ')
    if listing:
        if s[0] == '$': # listing is over
            listing = False 
        else:
            # here s[1] is dir name / file name
            complete_path = [e for e in current_directory_path]
            complete_path.append(s[1])

            if s[0] == 'dir': # add dir to current directory
                set_in_tree(complete_path, {})
                directories.add('>'.join(complete_path))
            else: # add file to current directory
                # here, s[0] is file size
                set_in_tree(complete_path, s[0])

                # store sizes for future counting
                sizes[('>'.join(complete_path))] = int(s[0])
            continue
    if s[0] == '$': # command
        if s[1] == 'cd':
            if s[2] == '/': # moving to root
                current_directory_path = ['/']
            elif s[2] == '..': # moving up
                current_directory_path.pop()
            else: # moving down
                current_directory_path.append(s[2])
        elif s[1] == 'ls':
            listing = True # next lines will be the dir content (or another command)
        else:
            print(f"Something went wrong, unknown command : {s[1]}")

# part one
countP1 = 0
directories_sizes = {}
for x in directories:
    result = compute_directory_size(x)
    directories_sizes[x] = result
    if result <= 100000:
        countP1 += result

print(f'Part one solution : {countP1}')

# part two
countP2 = 0
rootDirSize = directories_sizes['/']
print(f"Root '/' size : {rootDirSize}")
unusedSpace = 70000000 - rootDirSize
print(f"Unused space : {unusedSpace}")
minimumSizeNeeded = 30000000 - unusedSpace
print(f"Minimum size needed : {minimumSizeNeeded}")

directory_to_delete_size = 99999999
for k,v in directories_sizes.items():
    if v < directory_to_delete_size and v >= minimumSizeNeeded:
        directory_to_delete_size = v

print(f'Part two solution : {directory_to_delete_size}')