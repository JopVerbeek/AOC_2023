import re
import numpy as np

with open('input3.txt') as f:
    grid = [row for row in f.read().splitlines()]

def find_nums_pos(grid):
    nums, pos = [], []
    for i_pos, r in enumerate(grid):        
        for numbers in re.finditer(r'\d+', r):
            num = int(numbers.group()) 
            start_idx = int(numbers.span()[0])
            end_idx = int(numbers.span()[1])
            nums.append(num)
            pos.append((i_pos, start_idx, end_idx))
    return nums, pos

def check_neighbour(num, pos, grid):
    neighbours = []
    num = num
    r_num, start_idx, end_idx = pos
    if r_num > 0: 
        top_indexes = [(r_num - 1, i) for i in range(start_idx - 1, end_idx + 1) if i >= 0 and i <= len(grid[0]) -1]
        neighbours.extend(top_indexes)
    if r_num < len(grid) - 1:
        bottom_indexes = [(r_num + 1, i) for i in range(start_idx - 1, end_idx + 1) if i >= 0 and i <= len(grid[0]) -1]
        neighbours.extend(bottom_indexes)
    if start_idx - 1 > 0:
        left_side_index = (r_num, start_idx - 1)
        neighbours.append(left_side_index)
    if end_idx + 1 < len(grid[0]) - 1:
        right_side_index = (r_num, end_idx)
        neighbours.append(right_side_index)
    
    for y, x in neighbours:     
        if grid[y][x] != '.' and not grid[y][x].isdigit():
            return True, num, neighbours
    return False, None, None

nums = []
neighbours_list = []
counter = 0
numbers, pos = find_nums_pos(grid)
for number, pos in zip(numbers, pos):        
    valid, number, neighbours = check_neighbour(number, pos, grid)
    if valid:
        counter += number
        nums.append(number)
        neighbours_list.append(neighbours)

star_positions = []
for i, r in enumerate(grid):
    for j , c in enumerate(r):
        if grid[i][j] == '*':
            star_positions.append((i, j))

gear = 0 
for star_pos in star_positions:        
    common = []
    for num, neighbours in zip(nums, neighbours_list):
        if star_pos in neighbours:
            common.append(num)
        if len(common) == 2:
            print(common)
            gear += np.prod(np.array(common))
            common = []
print(gear)