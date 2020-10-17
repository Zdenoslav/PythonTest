import names
import random
import io
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
f = io.open("test_data.txt", mode="w", encoding="utf-8")
for i in range(10):
    f.write(str(ids[i]) + ":" + first_names[i] + ":" +
            last_names[i] + ":" + chosenDepartments[i] + "\n")
