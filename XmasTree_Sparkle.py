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
    # For bright colours, use the hsv model
    h = random()
    s = 1
    v = 1
    hsv = Color.from_hsv(h,s,v) # takes values 0-1
    rgb = hsv.rgb
    #
    # or for more subtle colours, use the rgb model
    #r = random()
    #g = random()
    #b = random()
    #rgb = Color.from_rgb(r,g,b).rgb
    #
    return (rgb)

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
