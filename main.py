#################################
# This code was made by Vortezz #
# and edited by Thebloodshadow  #
# NOTICE : Some value has to be #
#   edited before utilisation   #
#################################

from microbit import *

display.off()

def commande_mot1(direction, speed):
    pin8.write_digital(sens)
    pin1.write_analog(vitesse)

def commande_mot2(direction, speed):
    pin12.write_digital(sens)
    pin2.write_analog(vitesse)

def forward():
    commande_mot1(0, 512)
    commande_mot2(1, 512)

def stop():
    commande_mot1(0, 0)
    commande_mot2(1, 0)

def left():
    commande_mot1(0, 512) #I don't know if this is really left since i don't know in wich order are the motors
    commande_mot2(1, 0)   #You may need to change left and right if your robot is not rotating in the direction it should

def right():              #I don't know if this is really right since i don't know in wich order are the motors
    commande_mot1(0, 0)   #You may need to change left and right if your robot is not rotating in the direction it should
    commande_mot2(1, 512)

while True:

    if pin7.read_digital() and pin6.read_digital():
        forward()

    elif pin6.read_digital():
        left()

    elif pin7.read_digital():
        right()

    else:
      stop()
