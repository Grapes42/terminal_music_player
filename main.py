import numpy as np

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

class Screen:
    def __init__(self, height, width, fps, bg=None, fg=None):
        self.carr = np.full((height, width), "#")

        self.height = height
        self.width = width
        
        self.frame_del = fps/60



        if fg == None and bg == None:
            self.ansii = ""
        elif bg == None:
            fg_code = fg_colors[fg]

            self.ansii = f"\033[{fg_code}m"
        elif fg == None:
            bg_code = bg_colors[bg]

            self.ansii = f"\033[{bg_code}m"
        else:
            fg_code = fg_colors[fg]
            bg_code = bg_colors[bg]

            self.ansii = f"\033[{fg_code};{bg_code}m"
    

    def __str__(self):
        screen_string = ""

        for y in range(self.height):
            for x in range(self.width):
                screen_string += str(f"{self.ansii}{screen.carr[y][x]}{ENDC}")
            screen_string += "\n"

        return screen_string


import os
rows, columns = os.popen('stty size', 'r').read().split()
rows = int(rows)
columns = int(columns)

screen = Screen(height=rows, width=columns, fps=30, fg="white", bg="magenta")







print(screen)
