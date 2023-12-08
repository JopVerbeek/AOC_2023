from math import lcm
from itertools import cycle

with open('input8.txt') as f:
    path = [line for line in f.read().splitlines() if line != '']

directions = path[0]
nodes = path[1:]
wasteland = {}
keys, vals = [], []
for node in nodes:
    k, v = node.split(' = ') 
    keys.append(k)
    vals.append(v.replace('(', '').replace(')', '').split(', '))

wasteland = {k: v for k, v in zip(keys, vals)}

def part_1():  
    steps = 0
    start = 'AAA'
    end = 'ZZZ'
    found = False
    while not found:
        for dir in directions:
            steps += 1
            if dir == 'L':
                start = wasteland[start][0]
            if dir == 'R':
                start = wasteland[start][1]
            if start == 'ZZZ':            
                found = True
                break
    return steps

print(part_1())

def part_2(start):    
    steps = 0

    for dir in cycle(directions):
        steps += 1
        if dir == 'L':
            start = wasteland[start][0]
        if dir == 'R':
            start = wasteland[start][1]
        if start.endswith('Z'):            
            return steps 
        
starts = [key for key in keys if key.endswith('A')]
num_steps = [part_2(start) for start in starts]
print(lcm(*num_steps))