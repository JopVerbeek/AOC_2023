import subprocess
import os
from datetime import date
import sys
from secret import secret

SESSION = secret

#Get today number of day
day_today = date.today().strftime("%d").lstrip("0")

#If we provide an argument, use it as the desired day. Ex: ./startDay.py 5. Otherwise use day_today
if len(sys.argv) > 1:
    day = int(sys.argv[1])
    if day<0 or day>31 or day>int(day_today):
        exit("Day is not valid")
else:
    day = day_today

print(f"Initializing day {day}")

useragent = 'https://github.com/JopVerbeek/AOC_2023/tree/main//get_input.py by jop.verbeek@gmail.com'

if not os.path.exists(f"day{day}"):
    os.mkdir(f"day{str(day).zfill(2)}")
    os.chdir(f"day{str(day).zfill(2)}")
    cmd = f'curl https://adventofcode.com/2023/day/{day}/input --cookie "session={SESSION}" -A {useragent}'
    output = subprocess.check_output(cmd, shell=True)
    output = output.decode('utf-8')
    output = output.split('<HTML>')[0]
    temp_read = f"with open('input{day}.txt') as f:"
    with open(f"input{day}.txt","w") as f:
        f.write(output)
    with open(f"day{str(day).zfill(2)}.py", "w") as c:
        c.write(temp_read)