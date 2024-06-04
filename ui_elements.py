import numpy as np

ENDC = '\033[0m'

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

class Screen:
    def __init__(self, height, width, fps, bg=None, fg=None):
        self.c_arr = np.full((height, width), " ")

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
            screen_string += "\n"
            for x in range(self.width):
                screen_string += str(f"{self.ansii}{self.c_arr[y][x]}{ENDC}")

        return screen_string


class Box:
    def __init__(self, array, width, height, y, x):
        self.array = array

        self.width = width - 1
        self.height = height - 1

        self.y = y
        self.x = x

    def h_line(self, row):

        finish = self.x + self.width

        self.array[row][self.x] = "+"
        self.array[row][finish] = "+"

        pos = self.x+1

        while pos < finish:
            self.array[row][pos] = "-"
            pos += 1

    def v_line(self, column):

        finish = self.y + self.height

        pos = self.y + 1

        while pos < finish:
            if self.array[pos][column] != "+": 
                self.array[pos][column] = "|"
            pos += 1

    def add(self):

        self.h_line(row=self.y)
        self.h_line(row=self.y+self.height)

        self.v_line(column=self.x)
        self.v_line(column=self.x + self.width)

        