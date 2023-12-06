with open('input.txt') as f:
    blocks = f.read().split('\n\n')

blocks_cleaned = []
for block in blocks:
    block_lines = []
    for line in block.splitlines():
        if ':' in line:
            block_lines.append(line.strip().split(':')[1].strip())
        elif line != '':
            block_lines.append(line.strip())
    block_lines = [list(map(int, line.split(' '))) for line in block_lines if line != '']
    blocks_cleaned.append(block_lines)

seeds, seed2soil, soil2fert, fert2water, water2light, light2temp, temp2humid, humid2loc = blocks_cleaned
seeds = seeds[0]

def make_map(ranges):
    lookup_map = {}
    for i, (dst, src, r) in enumerate(ranges, 1):
        windows = {}
        windows['dst'] = dst 
        windows['src'] = src
        windows['r'] = r
        windows['source_range'] = range(src, src + r)
        lookup_map[i] = windows
    return lookup_map

def make_map_2(ranges):
    lookup_map = {}
    for i, (dst, src, r) in enumerate(ranges, 1):
        windows = {}
        windows['dst'] = dst 
        windows['src'] = src
        windows['r'] = r
        windows['source_range'] = range(dst, dst + r)
        lookup_map[i] = windows
    return lookup_map

def extract_loc(seed_num, maps):
    destination_number = seed_num
    for map in maps:
        found = False
        for v in map.values():
            if destination_number in v['source_range']:            
                if not found:
                    diff = destination_number - v['src']
                    destination_number = v['dst'] + diff
                    found = True
                continue
    return destination_number

def extract_loc_2(loc_num, maps):
    destination_number = loc_num
    for map in maps:
        found = False
        for v in map.values():
            if destination_number in v['source_range']:            
                if not found:
                    diff = destination_number - v['dst']
                    destination_number = v['src'] + diff
                    found = True
                continue
    return destination_number

maps = [make_map(lookup_map) for lookup_map in [seed2soil, soil2fert, fert2water, water2light, light2temp, temp2humid, humid2loc]]
maps_2 = [make_map_2(lookup_map) for lookup_map in [seed2soil, soil2fert, fert2water, water2light, light2temp, temp2humid, humid2loc]][::-1]

ans = min([extract_loc(seed, maps) for seed in seeds])
print([extract_loc(seed, maps) for seed in seeds])

seeds_range = []
for i in range(0, len(seeds), 2):
    start = seeds[i]
    increment = seeds[i+1]
    seeds_range.append(range(start, start + increment))
seeds_range = sorted(seeds_range, key = lambda r: r.start)

def reduce_ranges(seeds_range, loc_num):    
    found = False
    range_reduced = seeds_range
    while not found:    
        loc_num += 1
        seed_num = extract_loc_2(loc_num, maps_2)
        for seed_range in range_reduced:
            if seed_num in seed_range:                
                found = True
                return loc_num
print(reduce_ranges(seeds_range, 0))           