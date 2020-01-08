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

while True:
    LI = CL.ambient()  # light intensity
    Robot.drive(50, (LI * 2) - 100)
