import random

bg_colors = {
    "black": '40',
    "red": '41',
    "green": '42',
    "yellow": '43',
    "blue": '44',
    "magenta": '45',
    "cyan": '46',
    "white": '47'
}

fg_colors = {
    "black": '30',
    "red": '31',
    "green": '32',
    "yellow": '33',
    "blue": '34',
    "magenta": '35',
    "cyan": '36',
    "white": '37'
}

ENDC = '\033[0m'

string = "hehehehaw! "*1300

while True:
    bg = random.randint(40, 47)
    fg = random.randint(30, 37)

    effect = random.randint(1,9)

    ansii = f"\033[{fg};{bg};{effect}m"

    print(f"{ansii}{string}{ENDC}")