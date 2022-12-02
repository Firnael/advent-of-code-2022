# - Appens a new line to the README.md
# - Creates the directory & files for the new day
import os, sys

if len(sys.argv) < 3:
    print("Missing args")
    quit(1)
day = sys.argv[1]
desc = sys.argv[2]

# append new line to README
path = os.path.join(os.path.dirname(__file__), "../README.md")
readme = open(path, 'a')
readme.write('\n')
readme.write("- [{day} - {desc}](https://adventofcode.com/2022/day/{day}) - [code](/days/{day}/main.py)".format(day=day, desc=desc))
readme.close()

# create directory & files
files = ["data.txt", "data_example.txt", "main.py"]
for file in files:
    path = "days/{day}/{file}".format(day=day, file=file)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        if file == "main.py":
            f.write("# Day {day}\n".format(day=day))
            f.write("from utils.file_reader import read\n")
            f.write("data = read(__file__)\n")
        else:
            f.write("")