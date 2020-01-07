#!/usr/bin/env python3
# XmasTree_WhichLEDIsWhich.py
# Helps identify which LED is which number - to aid development of patterns
# Running this code produces a grid window with 25 buttons - click each number
# to light up the corresponding LED.
from tree import RGBXmasTree
from tkinter import *
from functools import partial

# Instance the  RGBXmasTree
tree = RGBXmasTree(brightness=0.05)
tree.off()

def flashLED(i):
    tree.off()
    tree[i].color = (1, 1, 1)
    print('LED ',i)

master = Tk()
canvas = Canvas(master)
i=0
for c in range(5):
    for r in range(5):
        button = Button(0)
        button.configure(text=i)
        button.configure(command=partial(flashLED,i))
        button.grid(row=r,column=c)
        i+=1

# main loop
try:
    master.mainloop()
except KeyboardInterrupt:
    tree.close()
