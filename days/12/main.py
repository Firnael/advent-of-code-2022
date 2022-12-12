# Day 12
from utils.helpers import pretty_print_grid
from utils.file_reader import read
data = read(__file__)

class Node:
    x = 0 # coordinate X
    y = 0 # coordinate Y
    v = 0 # value
    c = 'bite' # char
    def __init__(self, x, y, v, c):
        self.x = x
        self.y = y
        self.v = v
        self.c = c

def ascii_to_int(char):
    if char == 'S':
        return 0
    elif char == 'E':
        return 27
    # ascii code for 'a' is 97, so this returns 1 if char == 'a'
    return ord(char) - 96

# implement DFS algorithm (like I have nothing else to do, wtf AoC...)
def dfs(graph, root: Node):
    visited = { root: 0 }
    queue = [root]
    while queue:
        node = queue.pop(0)
        current_step = visited[node] # keep the step linked to the node
        for edge in graph[node]:
            if edge.c == 'E':
                return current_step + 1
            if edge not in visited:
                queue.append(edge)
                visited[edge] = current_step + 1

grid = []
nodes = []

# build grid and corresponding nodes map (with values from 0 to 26)
for i, line in enumerate(data):
    grid.append(list([l for l in line]))
    nodes.append(list([Node(i, j, ascii_to_int(c), c) for j,c in enumerate(line)]))

root = None
graph = dict()

# create graph
for i, x in enumerate(nodes):
    for j, y in enumerate(nodes[i]):
        node = nodes[i][j]
        if node.c == 'S':
            root = node
        if node not in graph:
            graph[node] = []
        if i > 0 and node.v - nodes[i-1][j].v >= -1 : # up
            graph[node].append(nodes[i-1][j])
        if i < len(nodes) - 1 and node.v - nodes[i+1][j].v >= -1: # down
            graph[node].append(nodes[i+1][j])
        if j > 0 and node.v - nodes[i][j-1].v >= -1: # left
            graph[node].append(nodes[i][j-1])
        if j < len(nodes[i]) - 1 and node.v - nodes[i][j+1].v >= -1: # right
            graph[node].append(nodes[i][j+1])
            
# part one
# run DFS (ta grosse daronne)
steps = dfs(graph, root)
print(f'Part one solution: {steps}')

# part two
# just run DFS for every 'a' and 'S', and take the min value among results (and ignore 'None')
steps_from_scenic = [dfs(graph, n) if n.c == 'a' or n.c == 'S' else None for sub in nodes for n in sub]
print(f'Part two solution: {min([i for i in steps_from_scenic if i is not None])}')