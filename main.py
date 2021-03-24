#################################
# This code was made by Vortezz #
# and edited by Thebloodshadow  #
# NOTICE : Some value has to be #
#   edited before utilisation   #
#################################
seconds_launch = 0
sseconds = 0
from microbit import *

display.off()

def command_mot1(direction, speed):
    pin8.write_digital(direction)
    pin1.write_analog(speed)

def command_mot2(direction, speed):
    pin12.write_digital(direction)
    pin2.write_analog(speed)

def forward():
    command_mot1(0, 1023)
    command_mot2(1, 1023)

def stop():
    command_mot1(0, 0)
    command_mot2(1, 0)

def left():
    command_mot1(0, 1023)
    command_mot2(1, 0)

def right():
    command_mot1(0, 0)
    command_mot2(1, 1023)

def catapult_launch():
    stop() 
    global seconds_launch
    if seconds_launch < 2:
        seconds_launch += 1
        basic.pause(1000)
    else:
         pin3.write_digital(1)

while True:
    seconds += 1
    if seconds == 5:
        catapult_launch()
    elif pin7.read_digital() and pin6.read_digital():
        forward()
    elif pin6.read_digital():
        left()
    elif pin7.read_digital():
        right()
    else:
      stop()
    basic.pause(1000)

#Test to see something

motorbit.forward(100)
basic.pause(2000)
motorbit.back(100)
basic.pause(2000)
motorbit.right(100)
basic.pause(2000)
motorbit.left(100)