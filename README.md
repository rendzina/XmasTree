# XmasTree
 Code to run different LED patterns using the fantastic [3D RGB Xmas Tree for Raspberry Pi](https://thepihut.com/products/3d-rgb-xmas-tree-for-raspberry-pi) on a Raspberry Pi

 ## Project
 This project is to use a Raspberry Pi to run on an attached [3D RGB Xmas Tree for Raspberry Pi](https://thepihut.com/products/3d-rgb-xmas-tree-for-raspberry-pi), and for it to run unattended (no attached keyboard/mouse), changing the LED lights on the Xmas Tree on an attached Raspberry Pi.

 The project uses a Raspberry Pi (we used a Pi Zero, although any model Pi would do), and based on the [Pi Hut example source code](https://github.com/ThePiHut/rgbxmastree#rgbxmastree).

 ## Software
 The script *`tree.py`* supplied by Pi Hut is used, and must be present in the same directory/folder as the Python scripts here. The reason is that the class 'RGBXmasTree' is imported from it:

 ## Hardware
 The following hardware is used:
 - [Raspberry Pi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero-w/)

This hardware is well designed - having removed the tree parts from the circuit board (clippers will do this, we used a dremmel fine saw). The parts then all push fit together - no soldering is required.

 ## Code
 A variety of code samples are given:
 - *'XmasTree_Colours.py'* Set ALL LEDs to same colour using list, set top LED white
 - *'XmasTree_Colours.py'* Set all LEDs to random colour using list, set top LED white

 There are 25 WS2812 NeoPixel RGB LEDs on the board, numbered 0-24, one of these is the LED on the top of the tree. Experimentation revealed this to be LED number 21. A variable was set up to represent this to allow it to be coloured separately.

 ## Instructions
 The Xmas Tree is fitted to the Raspberry Pi, via the GPIO bus. The orientation of the GPIO plug is critical and MUST be fitted correctly or else voltage will be applied to the data line due to the PCB design (not a good idea!)

 The Pi was set up to run in 'headless' mode (no monitor/keyboard/mouse) - to do this see our [GeoThread blog](http://www.geothread.net/?s=headless), allowing a remote laptop to ssh in to the Pi, and using [FileZilla](https://filezilla-project.org) to copy files over to it.

 ## Testing
 To test the Xmas Tree board, in the same folder as the script *`tree.py`* supplied by Pi Hut, run the Python shell:
 ```
 Python 3.7.3
 >>> from tree import RGBXmasTree
 >>> tree = RGBXmasTree()
 >>> tree[3].color = (0, 1, 0)
 >>> tree.off()
 ```
 Respectively, this sets up the tree, turns on the top LED (3) green, then turns all the LEDs off.

 Next, to test the code, it was run remotely via ssh from a laptop running the python script, the code was located in the home folder *'/home/pi'*, e.g.:
 ```
 > python3 XmasTree_Sparkle.py
 ```

 ## Operation
  To make the code run unattended on the Pi, there needed to be a means to start the programme automatically on boot. The best means to do this was found to be to use an autostart desktop file. A file was therefore created thus:
 ```
 > touch /home/pi/.config/autostart/XmasTree.desktop
 > nano /home/pi/.config/autostart/XmasTree.desktop

 [Desktop Entry]
 Type=Application
 Name=3D Xmas Tree
 Exec=/usr/bin/python3 /home/pi/XmasTree_Sparkle.py
 ```

 ## Observations
 The code here gives some interesting display options, adding to the existing example code. There is huge scope now for further improvements to have different displays. One interesting development would be to link the display to various sensors and events that the Pi can handle - so a PIR detector used to display lights according to proximity of people for example.

 A final note is that the Pi has no graceful way to be shut down when done. Simply turning off the Pi at the mains is not a great idea. One solution is to use a crontab entry to simply close the Pi down at say 23:30 each day (of course it needs to be turned on each day).
```
sudo crontab -e
[add a root user crontab]

 30 23 * * * /sbin/shutdown -h now
```
Now the Pi can be rebooted.
