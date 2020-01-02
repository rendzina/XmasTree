#!/usr/bin/env python3
# Set ALL LEDs to same colour using list, set top LED white
from tree import RGBXmasTree
from colorzero import Color
from time import sleep

# generate random floating point values
from random import seed
from random import random
# seed random number generator
seed(1)

# Set to LED number for top of Xmas Tree. LEDs are numbered 0-24.
TOP_LED = 21

# Instance the  RGBXmasTree
tree = RGBXmasTree(brightness=0.05)

colors = [Color('cyan'), Color('yellow'), Color('purple'), Color('red'), Color('green'),
  Color('blue'), Color('magenta')] # add more if you like

# main loop
try:
    while True:
        for color in colors:
            tree.color = color
            # colour top LED white (will flash due to loop)
            tree[TOP_LED].color = (1, 1, 1)
            val = random()/10 # trying to make it 'sparkle'
            sleep(val)
except KeyboardInterrupt:
    tree.close()
