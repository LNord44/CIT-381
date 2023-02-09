# CIT 381 
# Luke Nordheim
# 3/2/2022
# code for testing that LCD can display text

# importing libraries 
import time
import I2C_LCD_driver

#making object 
thelcd = I2C_LCD_driver.lcd()

#printing and clearing the display after 10 seconds
while True:
    thelcd.lcd_display_string("Hello world!", 1, 1)
    time.sleep(10)
    thelcd.lcd_clear()
    time.sleep(1)

# CIT 381 
# Luke Nordheim
# 3/2/2022
# code for reading MCP3208 ADC and displaying it to LCD screen

# importing libraries 
from gpiozero import MCP3208
import time
import I2C_LCD_driver

# Define the three channels we are using from the MCP3208
ch0 = MCP3208(channel = 0, differential = False, max_voltage = 3.3)
ch1 = MCP3208(channel = 1, differential = False, max_voltage = 3.3)
ch2 = MCP3208(channel = 2, differential = False, max_voltage = 3.3)
ch3 = MCP3208(channel = 3, differential = False, max_voltage = 3.3)

# creating LCD object
thelcd = I2C_LCD_driver.lcd()

# Main Loop
while True:
    #printing GND
    thelcd.lcd_display_string("GND: " + str(ch0.voltage) + "v")
    time.sleep(2)
    thelcd.lcd_clear()
    time.sleep(.5)
    
    #printing 3.3 V
    thelcd.lcd_display_string("3.3: " + str(ch1.voltage) + "v")
    time.sleep(2)
    thelcd.lcd_clear()
    time.sleep(.5)
    
    # printing 2.5 V
    thelcd.lcd_display_string("2.5: " + str(ch2.voltage) + "v")
    time.sleep(2)
    thelcd.lcd_clear()
    time.sleep(.5)
    
    # printing LM35
    thelcd.lcd_display_string("LM35: " + str(ch3.voltage) + "v")
    time.sleep(2)
    thelcd.lcd_clear()
    time.sleep(.5)
    
    # printing celsius 
    thelcd.lcd_display_string("C temp: " + str(ch3.voltage * 100) + "degrees")
    time.sleep(2)
    thelcd.lcd_clear()
    time.sleep(.5)
    
    # printing farenheit 
    thelcd.lcd_display_string("F temp: " + str((ch3.voltage * 100) * 1.8 + 32) + "degrees")
    time.sleep(2)
    thelcd.lcd_clear()
    time.sleep(.5)
    

time.sleep(5)
