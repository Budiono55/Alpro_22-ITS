# Zaki Zaidan Akbar
# 5007221058

import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("TicTacToe games")
root.geometry("300x200")

label = ttk.Label(text='TikTakTu')
label.grid(row= 1, column= 2)

def clicked():
    label = ttk.Label(text='Invalid')
    label.grid(row= 5, column= 2)

# Build a dict list about column and row
Boxes = {
    'SQ11': [2,1],
    'SQ12': [2,2],
    'SQ13': [2,3],
    'SQ21': [3,1],
    'SQ22': [3,2],
    'SQ23': [3,3],
    'SQ31': [4,1],
    'SQ32': [4,2],
    'SQ33': [4,3],
}

# ------------- AUTO GENERATE MODE ---------------------

r= 0
c = 0

for i in Boxes:
    # debugging
    print(type(i))
    print(Boxes[i][0])
    print(type(Boxes[i][0]))

    
    r = Boxes[i][0]
    c = Boxes[i][1]
    i = Button(text=' X ', command= clicked)
    i.grid(row=r, column=c)

# ------------------------------------------------------

# ------------- MANUAL MODE ----------------------------

# SQ11 = Button(text='click me!', command=clicked)
# SQ11.grid(row = 2, column= 1)

# SQ12 = Button(text='click me!', command=clicked)
# SQ12.grid(row = 2, column= 2)

# SQ13 = Button(text='click me!', command=clicked)
# SQ13.grid(row = 2, column= 3)

# SQ21 = Button(text='click me!', command=clicked)
# SQ21.grid(row = 3, column= 1)

# SQ22 = Button(text='click me!', command=clicked)
# SQ22.grid(row = 3, column= 2)

# SQ23 = Button(text='click me!', command=clicked)
# SQ23.grid(row = 3, column= 3)

# SQ31 = Button(text='click me!', command=clicked)
# SQ31.grid(row = 4, column= 1)

# SQ32 = Button(text='click me!', command=clicked)
# SQ32.grid(row = 4, column= 2)

# SQ33 = Button(text='click me!', command=clicked)
# SQ33.grid(row = 4, column= 3)

# ---------------------------------------------------------

root.mainloop()