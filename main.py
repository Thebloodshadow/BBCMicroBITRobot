#################################
# This code was made by Vortezz #
# and edited by Thebloodshadow  #
# NOTICE : Some value has to be #
#   edited before utilisation   #
#################################

from microbit import *

display.off()

def command_mot1(direction, speed):
    pin8.write_digital(direction)
    pin1.write_analog(speed)

def command_mot2(direction, speed):
    pin12.write_digital(direction)
    pin2.write_analog(speed)

def forward():
    command_mot1(0, 512)
    command_mot2(1, 512)

def stop():
    command_mot1(0, 0)
    command_mot2(1, 0)

def left():
    command_mot1(0, 512)
    command_mot2(1, 0)

def right():
    command_mot1(0, 0)
    command_mot2(1, 512)

while True:

    if pin7.read_digital() and pin6.read_digital():
        forward()

    elif pin6.read_digital():
        left()

    elif pin7.read_digital():
        right()

    else:
        stop()
