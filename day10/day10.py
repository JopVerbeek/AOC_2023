from collections import deque

with open('input10.txt') as f:
    grid = f.read().splitlines()

for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col == 'S':
            start_row = r
            start_col = c

visited = {(start_row, start_col)}
Q = deque([(start_row, start_col)])

while Q:
    r, c = Q.popleft()
    curr_character = grid[r][c] 

    if r > 0 and curr_character in 'S|JL' and grid[r-1][c] in '|7F' and (r-1, c) not in visited:
        visited.add((r - 1, c))
        Q.append((r - 1, c))

    if r < len(grid) -1 and curr_character in 'S|7F' and grid[r+1][c] in '|JL' and (r + 1, c) not in visited:
        visited.add((r + 1, c))
        Q.append((r + 1, c))

    if c > 0 and curr_character in 'S-J7' and grid[r][c - 1] in '-LF' and (r, c - 1) not in visited:
        visited.add((r , c - 1))
        Q.append((r, c - 1))

    if c < len(grid[0]) - 1 and curr_character in 'S-LF' and grid[r][c + 1] in '-J7' and (r, c + 1) not in visited:
        visited.add((r , c + 1))
        Q.append((r, c + 1))

print(len(visited) // 2)
    
counter = 0
for r, row in enumerate(grid):
    inside = False
    for c, col in enumerate(row):
        if grid[r][c] in "|JLS" and (r, c) in visited:
            inside = not inside
        if inside and (r, c) not in visited:
            counter += 1

print(counter)