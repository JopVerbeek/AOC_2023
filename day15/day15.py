from collections import OrderedDict

with open('input15.txt') as f:    
    hashes = f.read().strip('\n')

def hash(seq):
    num = 0
    for char in seq:
        num += ord(char)
        num *= 17
        num %= 256
    return num

dict_lenses = OrderedDict()

counter = 0
for seq in hashes.split(','):
    box_num = hash(seq[:-1] if '-' in seq else seq[:-2])
    counter += box_num
    if '=' in seq:
        lens, strength = seq.split('=')
        if box_num not in dict_lenses:
            dict_lenses[box_num] = {lens: int(strength)}
        else:
            lens, strength = seq.split('=')
            dict_lenses[box_num].update({lens: int(strength)})
    else:
        lens = seq.split('-')[0]
        if box_num in dict_lenses:
            if lens in dict_lenses[box_num]:
                del dict_lenses[box_num][lens]

total = 0
#  box + 1 * pos * v
for k, v in dict_lenses.items():
    for i, val in enumerate(v.values(), start=1):
        print(k+1, i, val)
        total += (((k + 1) * i) * val)

print(total)