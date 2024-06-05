import os
import time
from ui_elements import *

def file_to_str(file):
    with open(f"ascii_art/{file}") as f:
        lines = f.readlines()

    string = ""
    for line in lines:
        string += line

    return string

# Getting terminal dimensions
rows, columns = os.popen('stty size', 'r').read().split()
rows = int(rows)
columns = int(columns)

screen = Screen(height=rows, width=columns, fps=30, fg="red", bg="black")

music_controls = Box(array=screen.c_arr, height=6, width=columns, y=rows-6, x=0, fg="red", bg="black", fill_color="black")
music_controls.construct()

music_animation = Text(array=screen.c_arr, text="", x=2, y=rows-5, fg="red", bg="black")
music_animation.construct()

play = Text(array=screen.c_arr, text=file_to_str("play"), x=round(columns/2-2), y=rows-5, fg="red", bg="black")
play.construct()

prev = Text(array=screen.c_arr, text=file_to_str("prev"), x=round(columns/2-9), y=rows-5, fg="red", bg="black")
prev.construct()

prev = Text(array=screen.c_arr, text=file_to_str("next"), x=round(columns/2+5), y=rows-5, fg="red", bg="black")
prev.construct()


with open("ascii_art/animation", "r") as f:
    animation = f.readlines()

line = 0

while True:
    music_animation.text = ""

    for i in range(4):
        music_animation.text += animation[line]
        line += 1

    music_animation.construct()

    print(screen, end="")

    if line >= len(animation):
        line = 0

    time.sleep(.7)