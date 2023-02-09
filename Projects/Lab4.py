# Testing the button and reed switch 
# puch is on gpi017, reed switch is on gpi20
from gpiozero import Button

#button = Button(17)
#button.wait_for_press()
#print("Button was pressed")

buttonReed = Button(20)
buttonReed.wait_for_press()
print("Reed switch was pressed")

# Luke Nordheim, Part 3 of IOT Lab 4 

# importing modules
from gpiozero import Button, MotionSensor, LED
from time import sleep
#import smtplib
#import subprocess
#import urllib.request

# creaing our objects
button = Button(17)
buttonReed = Button(20)
motion = MotionSensor(21)
alarmLED = LED(26, active_high = False)
armedLED = LED(19, active_high = False)

#turning the lights off
alarmLED.off()
armedLED.off()

# defining our states
isArmed = False
sendAlarm = False

# creating functions for when actions are done
def armed():
    global isArmed
    global armedLED
    global sendAlarm 
    if isArmed:
        isArmed = False
        alarmSent = False
        alarmLED.off()
        armedLED.off()
    else:
        armedLED.on()
        isArmed = True

def motionDetect():
    global isArmed
    global alarmLED
    global sendAlarm 
    if isArmed == True and sendAlarm  == False:
        alarmLED.on()
        print("MOTION DETECTED!")
        sendEmail()
        sendAlarm = True

def reset():
    global isArmed
    on.when_pressed = armed
motion.when_motion = motionDetect
motion.when_no_motion = reset

 

while True:
    sleep(0.01)
    global alarmLED
    global sendAlarm 
    if isArmed == True and sendAlarm == True:
        alarmLED.off()
        print("Alarm reset")
        sendAlarm = False

def sendEmail():
            user = "timmyhasburner@gmail.com"
            password = "burner123$"
            to = "8599059020@txt.att.net"
            subject = "MOTION DETECTED"

button.when_pressed = armed
motion.when_motion = motionDetect
motion.when_no_motion = reset

 

while True:
    sleep(0.01)
