# CIT 381 
# Luke Nordheim
# 4/12/2022
# what this program reads data from accuweather, conditions logic whether to run a sprinkler system

#importing libraries
import json, time, urllib.request, time
from gpiozero import LED
import I2C_LCD_driver

# creating objects
motor = LED(19)
thelcd = I2C_LCD_driver.lcd()

# this function gives me the location ID from the locations URL
def getLocID():
    API = "pEYEcIYCTm0CvkvMx3KW7XslLWRNbFdY"
    ZIP = '41006'
    apiurl ='http://dataservice.accuweather.com/locations/v1/postalcodes/us/search?apikey=%s&q=%s&language=en-us&details=false' % (API, ZIP)
    print(apiurl)
    with urllib.request.urlopen(apiurl) as url:
        data = json.loads(url.read().decode())
    print(data)
    return data[0]['Key']

# this function gives me the current conditions of the location I requested and writes them to a .txt file
def getCurrCondtions():
    API = "pEYEcIYCTm0CvkvMx3KW7XslLWRNbFdY"
    LOCATION_ID = "17764_PC"
    apiurl = 'http://dataservice.accuweather.com/currentconditions/v1/%s?apikey=%s&details=true' % (LOCATION_ID, API)
    print(apiurl)
    with urllib.request.urlopen(apiurl) as url:
        data = json.loads(url.read().decode())
    f = open("c:/home/pi/Documents/curr.txt", "w")
    f.write(json.dumps(data))
    f.close()

# this function gives me the 24 hour conditions of the location I requested and writes them to a .txt file
def get24HourCond():
    API = "pEYEcIYCTm0CvkvMx3KW7XslLWRNbFdY"
    LOCATION_ID = "17764_PC"
    apiurl = 'http://dataservice.accuweather.com/currentconditions/v1/' + LOCATION_ID + '/historical/24?apikey=pEYEcIYCTm0CvkvMx3KW7XslLWRNbFdY&details=true'
    print(apiurl)
    with urllib.request.urlopen(apiurl) as url:
        data = json.loads(url.read().decode())
    f = open("c:/tmp/24.txt", "w")
    f.write(json.dumps(data))
    f.close()

# this function gives me the 5 day forcast of the location I requested and writes them to a .txt file
def get5DayForc():
    API = "pEYEcIYCTm0CvkvMx3KW7XslLWRNbFdY"
    LOCATION_ID = "17764_PC"
    apiurl = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/%s?apikey=%s&details=true' % (LOCATION_ID, API)
    print(apiurl)
    with urllib.request.urlopen(apiurl) as url:
        data = json.loads(url.read().decode())
    f = open("c:/tmp/5.txt", "w")
    f.write(json.dumps(data))
    f.close()

# this function decides whether or not there has been precipitation in the last few hours
def logic1():
    f = open("c:/home/pi/Documents//24.txt", "r")
    data = json.loads(f.read())
    f.close()
    precipitation_summary = data[0]['PrecipitationSummary']
    rainSummary = precipitation_summary['Past24Hours']['Imperial']['Value']
    if (rainSummary > .15):
        return False, rainSummary
    else:
        return True, rainSummary

# this function decides whether or not it is currently raining
def logic2():
    f = open("c:/home/pi/Documents/curr.txt", "r")
    data = json.loads(f.read())
    f.close()
    precipitation_summary = data[0]['HasPrecipitation']
    if (precipitation_summary == False):
        return True, precipitation_summary
    else:
        return False, precipitation_summary

# this function decides whether or not there is a chance of rain in the forcast
def logic3():
    f = open("c:/home/pi/Documents/tmp/5.txt", "r")
    data = json.loads(f.read())
    f.close()
    precipitation_summary = data['DailyForecasts'][1]['Day']['PrecipitationProbability']
    rainSummary = data['DailyForecasts'][1]['Day']['TotalLiquid']['Value']
    if precipitation_summary > 70 and rainSummary > .15:
        return False
    else:
        return True
# calling functions
locationID = getLocID()
getCurrCondtions()
get24HourCond()
get5DayForc()
bool1, pastRain = logic1()
bool2, currentRain = logic2()
bool3 = logic3()
# deciding whether to give water and turning relay on and off if we do
if bool1 == False or bool2 == False or bool3 == False:
    print("We do not want to water")
else:
    print("We need to water!")
    # turning motor on and off 4 times
    for i in range(0,4):
        motor.on()
        sleep(5)
        motor.off()
        sleep(1)
   
#displaying values on the LCD display 
while True:
    thelcd.lcd_display_string("It has rained " + str(pastRain) + " inches in the last day")
    time.sleep(2)
    thelcd.lcd_clear()
    time.sleep(.5)
    thelcd.lcd_display_string("It has rained " + str(pastRain) + " inches today")
    time.sleep(2)
    thelcd.lcd_clear()
    time.sleep(.5)
