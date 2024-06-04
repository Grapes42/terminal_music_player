import os
from ui_elements import *

# Getting terminal dimensions
rows, columns = os.popen('stty size', 'r').read().split()
rows = int(rows)
columns = int(columns)

screen = Screen(height=rows, width=columns, fps=30, fg="white", bg="black")

a = Box(array=screen.c_arr, height=10, width=20, y=0, x=9)
a.add()

b = Box(array=screen.c_arr, height=20, width=10, y=0, x=0)
b.add()

b = Box(array=screen.c_arr, height=10, width=15, y=5, x=17)
b.add()

print(screen)
