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

def return_ansii(bg=None, fg=None):
    if fg == None and bg == None:
        ansii = ""
    elif bg == None:
        fg_code = fg_colors[fg]

        ansii = f"\033[{fg_code}m"
    elif fg == None:
        bg_code = bg_colors[bg]

        ansii = f"\033[{bg_code}m"
    else:
        fg_code = fg_colors[fg]
        bg_code = bg_colors[bg]

        ansii = f"\033[1;{fg_code};{bg_code}m"

    return ansii









class Screen:
    def __init__(self, height, width, fps, bg=None, fg=None):
        self.height = height
        self.width = width
        
        self.frame_del = fps/60

        self.ansii = return_ansii(bg, fg)

        self.c_arr = np.full((height, width), f"{self.ansii} {ENDC}")
    

    def __str__(self):
        screen_string = ""

        for y in range(self.height):
            screen_string += "\n"
            for x in range(self.width):
                screen_string += str(self.c_arr[y][x])

        return screen_string










class Box:
    def __init__(self, array, width, height, y, x, fg=None, bg=None, fill_color=None):
        self.array = array

        self.width = width - 1
        self.height = height - 1

        self.y = y
        self.x = x

        self.ansii = return_ansii(bg, fg)

        self.fill_ansii = return_ansii(bg=fill_color)

    def h_line(self, row):

        finish = self.x + self.width

        self.array[row][self.x] = f"{self.ansii}+{ENDC}"
        self.array[row][finish] = f"{self.ansii}+{ENDC}"

        pos = self.x+1

        while pos < finish:
            self.array[row][pos] = f"{self.ansii}-{ENDC}"
            pos += 1

    def v_line(self, column):

        finish = self.y + self.height

        pos = self.y + 1

        while pos < finish:
            if "+" not in self.array[pos][column]: 
                self.array[pos][column] = f"{self.ansii}|{ENDC}"
            pos += 1

    def construct(self):

        # Contructing lines
        self.h_line(row=self.y)
        self.h_line(row=self.y+self.height)

        self.v_line(column=self.x)
        self.v_line(column=self.x + self.width)


        y_pos = self.y+1

        while y_pos < (self.y + self.height):
            x_pos = self.x+1
            while x_pos < (self.x + self.width):
                val = self.array[y_pos][x_pos]
                self.array[y_pos][x_pos] = f"{self.fill_ansii} {ENDC}"
                x_pos += 1
            y_pos += 1


        