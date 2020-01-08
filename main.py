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

Robot = DriveBase(LM, RM, WD, AT)

while not Button.LEFT in brick.buttons():
    brick.display.text('Press the LEFT button when the sensor is in dim light', (30, 60))
    wait(10)
    brick.display.clear()
dim = CL.ambient()


while not Button.RIGHT in brick.buttons():
    brick.display.text('Press the RIGHT button when the sensor is in bright light', (30, 60))
    wait(10)
    brick.display.clear()
bright = CL.ambient()

while True:
    intensity = CL.ambient()
    steer = (200 * (intensity - dim) / (bright - dim)) - 100
    steer = min(max(steer, -100), 100)
    Robot.drive(30, steer)
    sleep(0.1)


