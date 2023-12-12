from itertools import combinations

with open('input11.txt') as f:
    grid = [[item for item in line] for line in f.read().splitlines()]

def l2_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def coords_after_expansion(coords, multiplier):
    empty_cols_before = sum([1 for col in empty_cols if col < coords[0]])
    empty_rows_before = sum([1 for row in empty_rows if row < coords[1]])
    return (coords[0] + empty_cols_before * (multiplier - 1),
            coords[1] + empty_rows_before * (multiplier - 1))

empty_rows = [y for y, row in enumerate(grid)
              if all(char == '.' for char in row)]
empty_cols = [x for x, cols in enumerate(zip(*grid))
              if all(char == '.' for char in cols)]

galaxy_coords = []
expansion_factor = 1_000_000
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == '#':
            new_x, new_y = coords_after_expansion((x, y), expansion_factor)
            galaxy_coords.append((new_x, new_y))

shortest_paths = [l2_distance(galaxy1[0], galaxy1[1], galaxy2[0], galaxy2[1])
                  for galaxy1, galaxy2 in combinations(galaxy_coords, 2)]
print(sum(shortest_paths))



