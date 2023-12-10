with open('input9.txt') as f:
    lines = [list(map(int, line.split(' '))) for line in f.read().splitlines()]

def find_history(line, layers = list()):    
    diff = [] 
    layers.append(line)
    for i, num in enumerate(layers[-1]):                
        if i > 0:
            diff.append(num - line[i-1])    
    if all(v == 0 for v in diff):
        layers.append(diff)
        return layers
    return find_history(diff, layers)

def update(history, i):
    if i == 0:
        history[i].append(0)
    else:
        history[i].append(history[i][-1] + history[i-1][-1])

    i += 1

    if i == len(history):
        return history
    return update(history, i)

counter = 0
for line in lines:
    hist = find_history(line[::-1], [])
    updated_hist = update(hist[::-1], 0)
    counter += updated_hist[-1][-1]
print(counter)