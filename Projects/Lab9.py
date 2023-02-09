# CIT 381 
# Luke Nordheim
# 3/30/2022
# This program takes a picture using the Pi Camera and saves it 
# to a file.

# Import needed modules
from picamera import PiCamera

# Set the path and name of the photo
file = "/home/pi/Pictures/cit394.jpg" # Change this to whatever 
# you would like. It currently saves it to the Pictures
# directory.

# Create the camera object.
camera = PiCamera()

# Optionally we can set things like the resolution
camera.resolution = (1920,1080) # Maximum resolution
camera.capture(file) # Takes the picture
camera.stop_preview()  # Removes the preview from the GUI

# CIT 381 
# Luke Nordheim
# 3/30/2022
# This program takes a picture using the Pi Camera when motion is detected and lights a LED

#importing libraries
from gpiozero import LED, MotionSensor
import time
from picamera import PiCamera

# creating objects 
led = LED(26)
camera = PiCamera()
motion = MotionSensor(21)

file = "/home/pi/Pictures/cit381.2.jpg"
camera.resolution = (1920,1080) # Maximum resolution

while True:
    motion.wait_for_motion()
    print("Motion Detected")
    led.on()
    camera.capture(file) # Takes the picture
    camera.stop_preview()  # Removes the preview from the GUI
    time.sleep(3)
    led.off()
