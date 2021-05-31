#################################
# This code was made by Vortezz #
# and edited by Thebloodshadow  #
# NOTICE : Some value has to be #
#   edited before use           #
#################################

from microbit import *

pin8.write_digital(0)
pin1.write_analog(256)
pin12.write_digital(1)
pin2.write_analog(256)

seconds_launch = 0
seconds = 0

display.on()


def command_mot1(direction, speed):
    pin8.write_digital(direction)
    pin1.write_analog(speed)


def command_mot2(direction, speed):
    pin12.write_digital(direction)
    pin2.write_analog(speed)


def forward():
    command_mot1(0, 1023)
    command_mot2(0, 1023)


def stop():
    command_mot1(1, 0)
    command_mot2(0, 0)


def left():
    command_mot1(0, 1023)
    command_mot2(1, 0)


def right():
    command_mot1(1, 0)
    command_mot2(0, 1023)


def line_reader():
    if pin13.read_digital() and pin14.read_digital():
        stop()
    elif pin13.read_digital():
        left()
    elif pin14.read_digital():
        right()
    else:
        forward()

def catapult_launch():  # Will send a pulse to your catpult after a certain
    # amount of time
    stop()
    global seconds_launch
    if seconds_launch < 2:
        seconds_launch += 1
        sleep(1000)
    else:
        pin3.write_digital(1)

while True:
    seconds += 1
    if seconds == 5000:
        catapult_launch()
    else:
        line_reader()
    sleep(1)