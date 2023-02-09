# Luke Nordheim, script for IOT Lab 2 - blinking red light 
import time
from gpiozero import LED, Button

led = LED(17, active_high = False)

while True: 
    led.blink(on_time=1, off_time=1, n=5)
    time.sleep(5)

# Luke Nordheim, script for IOT Lab 2 - blinking red light with pressed button 
import time
from gpiozero import LED, Button

led = LED(17, active_high = False)
button = Button(27, bounce_time=0.25)

while True:
    if button.value == 1:
        led.blink(on_time=1, off_time=1, n=5)
        time.sleep(5)
        print("Button was pressesed")
