# Day 13
from utils.file_reader import read
from utils.helpers import bcolors, pretty_print_grid
data = read(__file__)

def compare(l, r):
    if l == None:
        return True
    elif r == None:
        return False
    if isinstance(l, int) and isinstance(r, int): # compare ints
        return compare_ints(l, r)
    else: # compare lists
        return compare_lists(l, r)

def compare_ints(l, r):
    if l == r: return None
    return True if l < r else False

def compare_lists(l, r):
    if isinstance(l, int):
        l = [l]
    if isinstance(r, int):
        r = [r]
    if len(l) == 0:
        return True # left list is empty, right order
    last_result = True
    for li, x in enumerate(l):
        if x == None:
            return True
        elif len(r) == li: 
            return None
        elif isinstance(x, list) or isinstance(r[li], list):
            result = compare_lists(x, r[li])
            if result == None:
                continue
            else:
                return result
        else:
            result = compare_ints(x, r[li])
            if result == None:
                last_result = None
                continue
            else:
                return result
    return last_result # ran out of entries in l and len(l) < len(r)

def pair_is_in_right_order(left, right):
    a, b = eval(left), eval(right)

    # if lists have different length, add "None" values so we can zip without losing data
    diff = len(a) - len(b)
    if diff > 0: # a longer than b
        { b.append(None) for x in range(0, diff) }
    elif diff < 0: # b longer than a
        { a.append(None) for x in range(0, abs(diff)) }
    zipped = list(zip(a,b))
    
    # compare this shit
    for x in zipped:
        result = compare(x[0], x[1])
        if result == None:
            continue
        else:
            return result

# part one
current_pair_index = 1
buffer = []
sorted_list = [] # for part two
counter = 0
for i, line in enumerate(data):
    buffer.append(line)
    if not line or i == len(data) - 1: # encountered blank line, or EOF
        sorted_list.append(buffer[0])
        sorted_list.append(buffer[1])
        l, r = eval(buffer[0]), eval(buffer[1])
        result = pair_is_in_right_order(buffer[0], buffer[1])
        print(f'For a={buffer[0]},b={buffer[1]}')
        print(f'Result : {bcolors.OKGREEN if result else bcolors.FAIL}{result}{bcolors.ENDC}, Index: {bcolors.WARNING}{current_pair_index}{bcolors.ENDC}')
        if result == True:
            counter += current_pair_index
        buffer = []
        current_pair_index += 1
        continue
print(f'Part one solution : {counter}')

# part two
sorted_list.append('[[2]]')
sorted_list.append('[[6]]')
perfect = False
iteration = 0
while not perfect:
    iteration += 1
    #print(pretty_print_grid(sorted_list))
    #print(f'iteration : {iteration}')
    perfect = True
    for i, x in enumerate(sorted_list):
        if i < len(sorted_list) - 1:
            result = pair_is_in_right_order(x, sorted_list[i+1])
            if result == False:
                perfect = False
                sorted_list[i] = sorted_list[i+1]
                sorted_list[i+1] = x

print(pretty_print_grid(sorted_list))
key_1 = sorted_list.index('[[2]]') + 1
key_2 = sorted_list.index('[[6]]') + 1
print(f'Part two solution : {key_1 * key_2}')