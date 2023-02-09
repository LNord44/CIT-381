# CIT 381 
# Luke Nordheim
# 3/2/2022
# code for midterm exam, turns four lights on based off of push button

#importing libraries
from gpiozero import LED, Button
import time

# creating our objects
led1 = LED(5, active_high = False)
led2 = LED(6, active_high = False)
led3 = LED(13, active_high = False)
led4 = LED(19, active_high = False)
button = Button(17, bounce_time=.25)

# creating method to turn lights on, one at a time, and eventually turn them all off
def lights():
    led1.on()
    time.sleep(.5)
    led2.on()
    time.sleep(.5)
    led3.on()
    time.sleep(.5)
    led4.on()
    time.sleep(2)
    led1.off(),led2.off(),led3.off(),led4.off()
#lights()

# while true loop to wait for button press
while True:
    if button.value == 1:
        lights()
