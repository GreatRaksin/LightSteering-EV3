#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from time import sleep

# Write your program here
CL = ColorSensor(Port.S1)
LM = Motor(Port.B)
RM = Motor(Port.C)
WD = 56
AT = 114

btn = brick.buttons()
print(btn)

Robot = DriveBase(LM, RM, WD, AT)

def limit(value):
    # returns a value within the range -100 to +100
    return min(max(value, -100), 100)

while not Button.LEFT in brick.buttons():
    brick.display.text('Press the left button when the sensor is in dim light', (50, 60))
    sleep(0.7)
    brick.display.clear()
dim = CL.ambient()


while not Button.RIGHT in brick.buttons():
    brick.display.text('Press the RIGHT button when the sensor is in dim light', (50, 60))
    sleep(0.7)
    brick.display.clear()
bright = CL.ambient()

while True:
    intensity = CL.ambient()
    steer = limit((200 * (intensity - dim) / (bright - dim)) - 100)
    Robot.drive(50, steer)
    sleep(0.1)