import os
from ui_elements import *

# Getting terminal dimensions
rows, columns = os.popen('stty size', 'r').read().split()
rows = int(rows)
columns = int(columns)

screen = Screen(height=rows, width=columns, fps=30, fg="red", bg="black")

music_controls = Box(array=screen.c_arr, height=5, width=columns, y=rows-5, x=0, fg="red", bg="black", fill_color="black")
music_controls.construct()


print(screen, end="")

while True:
    pass