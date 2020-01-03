#!/usr/bin/env python3
# XmasTree_Sparkle.py
# Set all LEDs to random colour using list, set top LED white
from tree import RGBXmasTree
from colorzero import Color
from time import sleep

# generate random floating point values
from random import random
from random import choice

# Set to LED number for top of Xmas Tree. LEDs are numbered 0-24.
TOP_LED = 3

# Instance the  RGBXmasTree
tree = RGBXmasTree(brightness=0.05)

# Function to return a random colour
def random_color():
    # skew to red end to  prevent 'washed out' colours
    r = round(random() * 0.2,1) # between 0 and 0.2, makes it 5 times more likely to be red
    g = round(1/(5*random()+1),1) # Skew to higher values
    b = round(1/(5*random()+1),1)
    #print(r,g,b)
    return (r, g, b)

# Create a list of all numberes for LEDs, excepting top one
led = list(range(25)[::-1])
led.pop(len(led)-TOP_LED-1)
#print (*led) # just check it removed top number

# main loop
try:
    tree[TOP_LED].color = (1, 1, 1) # Set top LED to white
    while True:
        # Select one of the following two lines:
        tree[choice(led)].color = random_color() # set random LEDs to random colours
        #tree.color = random_color() # alternately set all LEDs to same random colour
except KeyboardInterrupt:
    tree.close()
