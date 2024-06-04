import os
from ui_elements import *

# Getting terminal dimensions
rows, columns = os.popen('stty size', 'r').read().split()
rows = int(rows)
columns = int(columns)

screen = Screen(height=rows, width=columns, fps=30, fg="white", bg="black")

box = Box(array=screen.carr, height=5, width=20, y=0, x=0)
box.add()

print(screen)
