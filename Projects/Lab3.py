# Luke Nordheim, CIT381, DISTANCE SENSOR LAB3 

from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=6, trigger=5, max_distance=3)
while True:
    print("Distance; " + str(sensor.distance * 100) + " centimeters")
    sleep(1)

# Luke Nordheim, CIT381, DISTANCE SENSOR LAB3 Part 2 

from gpiozero import DistanceSensor, LED
import time 

sensor = DistanceSensor(echo=6, trigger=5, max_distance=3)
led1 = LED(17, active_high = False)
led2 = LED(27, active_high = False)
led3 = LED(22, active_high = False)

while True:
    dist = sensor.distance
    print("Distance; " + str(dist) + " light meters")
    if dist  < 1:
        led1.on, led2.off, led3.off
    elif dist <= 2 and dist > 1:
        led1.on, led2.on, led3.off
    elif dist > 2:
        led1.on, led2.on, led3.on
    time.sleep(5)
    led1.off, led2.off, led3.off
