import random
import time


length = 20
chance = 10

for j in range(10):
    # Line 0
    line_0 = []
    for i in range(length):
        rng = random.randint(0,chance)

        if rng == 0:
            line_0.append("|")
        else:
            line_0.append(" ")



    # Line 1
    line_1 = []

    for char in line_0:
        line_1.append(char)



    for i in range(length):
        rng = random.randint(0, round(chance/2))

        if rng == 0:
            line_1[i] = "|"


    # Line 2
    line_2 = []

    for char in line_1:
        line_2.append(char)



    for i in range(length):
        rng = random.randint(0, round(chance/4))

        if rng == 0:
            line_2[i] = "|"

    # Line 3
    line_3 = "+"*length


    line = ""
    for char in line_0:
        line += char
    line += "\n"
    with open("animation", "a") as f:
        f.write(line)

    line = ""
    for char in line_1:
        line += char
    line += "\n"
    with open("animation", "a") as f:
        f.write(line)

    line = ""
    for char in line_2:
        line += char
    line += "\n"
    with open("animation", "a") as f:
        f.write(line)

    line = ""
    for char in line_3:
        line += char
    line += "\n"
    with open("animation", "a") as f:
        f.write(line)


