import numpy as np

with open('input2.txt') as f:
    lines = f.read().splitlines()

counter = 0
counter_2 = 0
for line in lines:
    id = int(line.split(':')[0].split('Game')[1].strip())
    count_dict = {
        'blue': 0, #14
        'red': 0,  #12
        'green': 0  #13
    }
    subsets = line.split(':')[1].split(';')
    for subset in subsets:
        cubes = subset.strip().split(',')
        for cube in cubes:
            num_cubes, colour = int(cube.strip().split(' ')[0]), cube.strip().split(' ')[1]
            if num_cubes > count_dict[colour]:
                count_dict[colour] = num_cubes
    if count_dict['blue'] <= 14 and count_dict['red'] <= 12 and count_dict['green'] <= 13:
        counter += id
    counter_2 += np.prod(np.array([value for value in count_dict.values()]))



print(counter)
print(counter_2)


    # check of het spel mogelijk is      
            