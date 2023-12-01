import regex as re

with open('input.txt') as f:
    lines = f.read().splitlines()

lookup = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        }

def extract_number(string):
    if string.isdigit():
        return int(string)    
    return lookup[string]

def find_first_last(regex_str, line):
    digits = re.findall(regex_str, line, overlapped=True)
    return extract_number(digits[0]) * 10 + extract_number(digits[-1])

sum_1 = 0
for line in lines:
    sum_1 += find_first_last("[0-9]", line) 
print(sum_1)

sum_2 = 0
for line in lines:
    sum_2 += find_first_last("[0-9]|one|two|three|four|five|six|seven|eight|nine", line)
print(sum_2)