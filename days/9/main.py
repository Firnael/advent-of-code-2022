# Day 9
from utils.file_reader import read
data = read(__file__)

# consider a 2D orthonormal space where bottom-left is (x=0, y=0)
movement_mapping = { 'R' : (1,0), 'L' : (-1,0), 'U' : (0,1), 'D' : (0,-1)}

# for part one
head = (0, 0)
tail = (0, 0)
tail_history = set()
# for part two
nodes = [(0, 0) for e in range(0, 10)] 
last_node_history = set()

def move(position, movement):
    return tuple([sum(tup) for tup in zip(position, movement)])

def diff(a, b):
    reverted_b = (-b[0], -b[1]) 
    return tuple([abs(sum(tup)) for tup in zip(a, reverted_b)])

def move_head(h, direction):
    movement = movement_mapping[direction]
    return move(h, movement)

def move_tail(t, h):
    # determine which direction tail needs to go based on current head position
    movement = [0, 0]
    difference = diff(t, h)
    if difference[0] > 1 or difference[1] > 1: # no need to move if head is close to tail
        if h[0] == t[0]: # if h.x == t.x : same column
            movement[1] = 1 if h[1] > t[1] else -1 # move up or down ?
        elif h[1] == t[1]: # if h.y == t.y : same line
            movement[0] = 1 if h[0] > t[0] else -1 # move left or right ?
        else: # otherwise : diagonal movement has to happen 😬
            diag = [1 if h[0] > t[0] else -1 , 1 if h[1] > t[1] else -1]
            movement[0] = (1 if difference[0] > 0 else -1) * diag[0]
            movement[1] = (1 if difference[1] > 0 else -1) * diag[1]
    return move(t, tuple(movement))

# zog zog
for line in data:
    instruction = line.split(' ')
    direction = instruction[0]
    steps = int(instruction[1])
    for step in range(0, steps):
        # part one
        head = move_head(head, direction)
        tail = move_tail(tail, head)
        tail_history.add(''.join([str(tail[0]), str(tail[1])]))
        # part two
        nodes[0] = move_head(nodes[0], direction) # nodes[0] is the head
        for x in range(0, 9):
            nodes[x+1] = move_tail(nodes[x+1], nodes[x]) # nodes[x+1] moves as-if nodes[x] is the head
        last_node_history.add(''.join([str(nodes[-1][0]), str(nodes[-1][1])]))

print(f'Part one solution : {len(tail_history)}')
print(f'Part two solution : {len(last_node_history)}')