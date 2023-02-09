# CIT 381 
# Luke Nordheim
# 3/23/2022
# Servo Test Code. This code will control a servo, moving it between the min, mid, and max positions.

# importing libraries
from gpiozero import Servo
from time import sleep

servo = Servo(5) # Servo is connected to GPIO 5
for i in range(0,5):
        print("Moving to minimum position")
        servo.min()
        sleep(1)
        print("Moving to mid position")
        servo.mid()
        sleep(1)
        print("Moving to maximum position")
        servo.max()
        sleep(1)

# CIT 381 
# Luke Nordheim
# 3/23/2022
# Servo Test Code. This code will control a servo, moving it between between -100 and 100 incrementally

# importing libraries
from gpiozero import Servo
from time import sleep

servo = Servo(5) # Servo is connected to GPIO 5
for pos in range(-100,100,4):
        print("Moving to " + str(pos))
        servo.value = pos/100.0
        sleep(.1)


# CIT 381 
# Luke Nordheim
# 3/23/2022
# this script moves the servo between min, mid, and max position based on button presses

# importing libraries
from gpiozero import Servo, Button
from time import sleep

# creating objects
servo = Servo(5) # Servo is connected to GPIO 5
button1 = Button(27, bounce_time=.25)
button2 = Button(23, bounce_time=.25)
button3 = Button(24, bounce_time=.25)

while True:
        # moving to the min position when my leftmost button is pressed
        if button1.value == 1:
            print("Moving to minimum position")
            servo.min()
            sleep(1)
        # moving to the mid position when my middle button is pressed
        elif button2.value == 1:
            print("Moving to mid position")
            servo.mid()
            sleep(1)
        # moving to the max position when my rightmost button is pressed
        elif button3.value == 1:
            print("Moving to maximum position")
            servo.max()
            sleep(1)
