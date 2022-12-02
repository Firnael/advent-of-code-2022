import os
import sys

def read(filePath):
    example = len(sys.argv) >= 2 and sys.argv[1] == 'example'
    path_to_file = 'data_example' if example else 'data'
    data = []
    with open(os.path.join(os.path.dirname(filePath), path_to_file + '.txt'), 'r') as f:
        [data.append(line.strip()) for line in f.readlines()]
    if example:
        print(f'Data {data}')
    return data