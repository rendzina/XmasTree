#!/usr/bin/env python3
# XmasTree_Swirl.py
# Multi-pattern designs
from tree import RGBXmasTree
from colorzero import Color
from time import sleep

# generate random floating point values
from random import random
from random import choice

# Instance the  RGBXmasTree
tree = RGBXmasTree(brightness=0.05)
# Named ranges
TOP_LED = 3
SPIRAL = [12,6,15,16,0,7,19,24,11,5,14,17,1,8,20,23,10,4,13,18,2,9,21,22,3]
LAYERS = [[12,6,15,16,0,7,19,24],[11,5,14,17,1,8,20,23],[10,4,13,18,2,9,21,22]]
ROTATE = [[12,11,10],[6,5,4],[15,14,13],[16,17,18],[0,1,2],[7,8,9],[19,20,21],[24,23,22]]
colors = [Color('cyan'), Color('red'), Color('purple'), Color('white'), Color('green'),
  Color('blue'), Color('yellow'), Color('magenta')]

# Function to return a random colour
def random_color():
    h = random()
    s = 1
    v = 1
    hsv = Color.from_hsv(h,s,v)
    rgb = hsv.rgb
    #
    return (rgb)

def Spiral():
    length = len(SPIRAL)
    for number, val in enumerate(SPIRAL):
      print("S",number,number/length,val)
      tree[val].color = Color.from_hsv(0.8,number/length,1).rgb

def Layers():
    for list in LAYERS:
       for number in list:
         print ("L",number)
         tree[number].color = random_color()
    tree[TOP_LED].color = (1, 1, 1) # Set top LED to white

def Rotate():
    for index, list in enumerate(ROTATE):
       print(index,list)
       for number, val in enumerate(list):
         print ("R",val)
         tree[val].color = colors[index]

# main loop
try:
    while True: # cycle through patterns
        tree.off()
        Spiral()
        #
        tree.off()
        Layers()
        #
        tree.off()
        Rotate()
        #
except KeyboardInterrupt:
    tree.close()
