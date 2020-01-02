# XmasTree
 Code to run different LED patterns using the fantastic Pi Hut 3D Xmas Tree on a Raspberry Pi

 ## Project
 This project is to use a Raspberry Pi to run the attached 3D Xmas Teee from Pi Hut, and for it to run unattended (no attached keyboard/mouse), changing the LED lights on the Xmas Tree on an attached Raspberry Pi.

 The project uses the [3D RGB Xmas Tree for Raspberry Pi](https://thepihut.com/products/3d-rgb-xmas-tree-for-raspberry-pi) with a Raspberry Pi Zero (any model Pi would do), and based on the [Pi Hut code](https://github.com/ThePiHut/rgbxmastree#rgbxmastree).

 ## Hardware
 The following hardware is used:
 - [Raspberry Pi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero-w/)

This hardware is well designed - having removed the tree parts from the circuit board (clippers will do this, we used a dremmel fine saw). The parts then all push fit together.

 ## Code
 A variety of code samples are given:
 - *'XmasTree_Colours.py'* Set ALL LEDs to same colour using list, set top LED white
 - *'XmasTree_Colours.py'* Set all LEDs to random colour using list, set top LED white

 There are 25 LEDs on the board, numbered 0-24, one of these relates to the LED on the top of the tree. Experimentation revealed this to be LRD number 21. A variable was set up to represent this to allow it to be coloured separately.

 ## Instructions
 The Xmas Tree is fitted to the Raspberry Pi - the orientation of the GPIO plug is critical and MUST be fitted correctly or else the voltage will be applied to the data line due to the design (not a good idea!)

 The Pi was set up to run in 'headless' mode (no monitor/keyboard/mouse) - to do this see our [GeoThread blog](http://www.geothread.net/?s=headless), allowing a remote laptop to ssh in to the Pi, and using [FileZilla](https://filezilla-project.org) to copy files over to it.

 ## Testing
 To test the code, it was run remotely via ssh from a laptop running the python script, the code was located in the home folder *'/home/pi'*, e.g.:
 ```
 > python3 XmasTree_Colours.py
 ```

 ## Operation
  To make the code run unattended on the Pi, there needed to be a means to start the programme automatically on boot. The best means to do this was found to be to use an autostart desktop file. A file was therefore created thus:
 ```
 > nano /home/pi/.config/autostart/XmasTree.desktop

 [Desktop Entry]
 Type=Application
 Name=3D Xmas Tree
 Exec=/usr/bin/python3 /home/pi/XmasTree_Colours.py
 ```

 ## Observations
 The code here gives some interesting display options, adding to the existing example code. There is huge scope now for further improvements to have different displays. One interesting development would be to link the display to various sensors and events that the Pi can handle - so a PIR detector used to display lights according to proximity of people for example.

 A final note is that the Pi has no graceful way to be shut down when done. Simply turning off the Pi at the mains is not a great idea. One solution is to use a crontab entry to simply close the Pi down at say 23:30 each day (of course it needs to be turned on each day).
```
sudo crontab -e
[add a root user crontab]

 30 23 * * * /sbin/shutdown -h now
```
