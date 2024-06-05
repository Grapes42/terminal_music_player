import random

ENDC = '\033[0m'

while True:

    space = " "*random.randint(0, 9)
    string = f"hehehehaw!{space}"*300

    bg = random.randint(40, 47)
    fg = random.randint(30, 37)

    effect = random.randint(1,9)

    ansii = f"\033[{fg};{bg};{effect}m"

    print(f"{ansii}{string}{ENDC}")