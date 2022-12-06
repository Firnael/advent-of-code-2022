# Day 6
from utils.file_reader import read
data = read(__file__)

def work(size):
    index = 0
    buffer = []
    for c in data[0]: # only one line in file
        if c in buffer:
            # char already exists, takes its index and start again from here +1
            buffer = buffer[buffer.index(c) + 1:]
        buffer.append(c)
        index += 1
        if len(buffer) == size:
            return index, ''.join(buffer) # found it !

print(f'Part one solution : {work(4)}')
print(f'Part two solution : {work(14)}')