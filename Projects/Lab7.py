# CIT 381 
# Luke Nordheim
# 3/16/2022
# code for controlling a small motor using a relay

#importing libraries
from gpiozero import LED
from time import sleep

# creating motor object 
motor = LED(19)

# turning motor on and off 4 times
for i in range(0,4):
    motor.on()
    sleep(5)
    motor.off()
    sleep(1)
