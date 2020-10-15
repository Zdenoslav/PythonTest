import random
import names
import io
import argparse
import ugen
import os

# create the testing files
first_names = []
for i in range(10):
    first_names.append(names.get_first_name())

last_names = []
for i in range(10):
    last_names.append(names.get_last_name())

ids = []
for i in range(10):
    ids.append(random.randint(1111, 9999))

departments = ["Sales", "Legal", "Defence", "Development"]
chosenDepartments = []
for i in range(10):
    chosenDepartments.append(random.choice(departments))

    # Generating names part
    # print(names.get_full_name())

# Creating of the files part
f = io.open("test_data1.txt", mode="w", encoding="utf-8")
for i in range(10):
    f.write(str(ids[i]) + ":" + first_names[i] + ":" +
            last_names[i] + ":" + chosenDepartments[i] + "\n")

# run the ugen.py program and give it the input files

os.system('python3 ugen.py')
# read the output file and see if the data is as expected


if __name__ == '__main__':
    # code for a help method
    parser = argparse.ArgumentParser(description='This is my help')
    parser.add_argument('tested_files', type=str, help='create an output file')
    parser.add_argument('test_data', type=str)
    args = parser.parse_args()
