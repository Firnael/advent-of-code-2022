import os
import sys

def read(filePath):
    path_to_file = 'data_' + sys.argv[1] if len(sys.argv) >= 2 else 'data'
    data = []
    with open(os.path.join(os.path.dirname(filePath), path_to_file + '.txt'), 'r') as f:
        [data.append(line.strip()) for line in f.readlines()]
    return data