import numpy as np
from itertools import combinations

with open('input11.txt') as f:
    grid = [[item for item in line] for line in f.read().splitlines()]


def l2_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

h_index, v_index = [], []
grid = np.array(grid)

for i, row in enumerate(grid):
    if np.all(row == '.'):
        h_index.append(i)

for i, row in enumerate(grid.T):
    if np.all(row == '.'):
        v_index.append(i)

grid = np.insert(grid, h_index, '.', axis = 0)
grid = np.insert(grid.T, v_index, '.', axis = 0)

locs = np.argwhere(grid != '.').tolist()
combs = list(combinations(locs, 2))

dist = 0
for comb in combs:
    x1, y1, x2, y2 = comb[0][0], comb[0][1], comb[1][0], comb[1][1]    
    dist += l2_distance(x1, y1, x2, y2)
print(dist)
    

