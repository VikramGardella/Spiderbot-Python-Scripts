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
ang_2 = 90

#channels FL=1, FR=14, BL=4, BR=11 for middle motors

kit.servo[0].angle = 100
kit.servo[1].angle = 90
kit.servo[2].angle = 90

kit.servo[3].angle = 90
kit.servo[4].angle = 90
kit.servo[5].angle = 90

dir = 1

try:

    while True:
        if(ang > 120):
            dir *= -1
        if(ang < 60):
            dir *= -1
        print('ang is %d' % ang)
        print('dir is %d' % dir)

        ang += (dir * 1)
        ang_2 += (dir * 2)

        kit.servo[1].angle = ang
        kit.servo[2].angle = ang_2

        kit.servo[4].angle = ang
        kit.servo[5].angle = ang_2

        time.sleep(0.05)

except KeyboardInterrupt:
    terminate()

finally:
    terminate()
