#################################
# This code was made by Vortezz #
# NOTICE : Some value has to be #
#   edited before utilisation   #
#################################

from microbit import *

display.off()

def command_mot1 (direction, speed):
    pin8.write_digital(direction)
    pin1.write_analog(speed)

def command_mot2 (direction, speed):
    pin12.write_digital(direction)
    pin2.write_analog(speed)

while True:
    if pin7.read_digital() and pin6.read_digital():
        command_mot1 (0, 0)
        command_mot2 (1, 0)

    elif pin6.read_digital():
        command_mot1 (0, 0)
        command_mot2 (1, 512)


    elif pin7.read_digital():
        command_mot1 (1, 512)
        command_mot2 (0, 0)

    else:
        command_mot1 (1, 512)
        command_mot2 (1, 512)
