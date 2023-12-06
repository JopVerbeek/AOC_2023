import re

with open('input6.txt') as f:
    lines = f.read().splitlines()
    
numbers = []
numbers_2 = []
for line in lines:
    nums = list(map(int,(re.findall(r'\d+', line))))
    nums_2 = int(''.join(str(num) for num in nums))
    print(nums_2)
    numbers.append(nums)
    numbers_2.append(nums_2)
times, records = numbers
times_2, records_2 = numbers_2

def get_winning_distances(time, record):   
    counter = 0
    for i in range(time):
        distance = (time - i) * i
        if distance > record:
            counter += 1
    return counter

total = 1
for time, record in zip(times, records):
    total *= get_winning_distances(time, record)

print(total)
print(get_winning_distances(times_2, records_2))