from __future__ import division
import RPi.GPIO as gpio
import time
#import curses
from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16)

#screen = curses.initscr()
#curses.noecho()
#curses.cbreak()
#screen.keypad(True)
#screen.nodelay(True)

#kit.servo[x].set_pulse_width_range(min, max)

limb_names = ['front_left', 'front_right', 'back_left', 'back_right']
limb_motor_channels = [[0, 1, 2], [15, 14, 13], [3, 4, 5], [12, 11, 10]]
limb_index = 0

top_motor_angs = [90, 90, 90, 90]
mid_motor_angs = [90, 90, 90, 90]
bot_motor_angs = [90, 90, 90, 90]

ang = 90

#channels 1, 14, 4, 11 for middle motors

while True:
    if(ang >= 180):
        ang = 0
    print('ang is %d' % ang)
    kit.servo[1].angle = ang
    time.sleep(0.05)
    kit.servo[14].angle = ang
    time.sleep(0.05)
    kit.servo[4].angle = ang
    time.sleep(0.05)
    kit.servo[11].angle = ang
    time.sleep(0.05)
    kit.servo[2].angle = ang
    time.sleep(6.0)
    ang = 90
