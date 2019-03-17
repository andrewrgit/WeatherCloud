import time
from neopixel import *
import sqlite3
import os
import pendulum
import urllib, json
import random
import traceback

time.sleep(12)

#LED strip configuration:
LED_COUNT      = 60    # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255    # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, pixelsLess=0, wait_ms=20):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()-pixelsLess):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def getPreviousDayValues():
    c.execute('SELECT * FROM weather WHERE DateAccessed >= datetime("now","localtime","start of day","-1 day") AND DateAccessed <= datetime("now","localtime","start of day")')
    r = c.fetchone()
    if r is None:
        print("Attempted to get Previous Day values, however no data exists")
        return None
    else:
        print("Grabbed Values for " + r[1])
        dictionary = {"DateAccessed":r[1], "weather1":r[2], "rain1":r[3],"snow1":r[4],"temp1":r[5],"weather2":r[6],"rain2":r[7],"snow2":r[8],"temp2":r[9],"weather3":r[10],"rain3":r[11],"snow3":r[12],"temp3":r[13],"weather4":r[14],"rain4":r[15],"snow4":r[16],"temp4":r[17]}
        return dictionary
def getCurrentDayValues():
    c.execute('SELECT * FROM weather WHERE DateAccessed >= datetime("now","localtime","start of day") AND DateAccessed <= datetime("now","localtime","start of day","+1 day")')
    r = c.fetchone()
    if r is None:
        print("Attempted to get current values, however no data exists")
        return None
    else:
        print("Grabbed Values for " + r[1])
        dictionary = {"DateAccessed":r[1], "weather1":r[2], "rain1":r[3],"snow1":r[4],"temp1":r[5],"weather2":r[6],"rain2":r[7],"snow2":r[8],"temp2":r[9],"weather3":r[10],"rain3":r[11],"snow3":r[12],"temp3":r[13],"weather4":r[14],"rain4":r[15],"snow4":r[16],"temp4":r[17]}
        return dictionary

thunderstorm = [201,202,211,212,221,231,232]
lightThunderstorm = [200,230]
drizzle=[301,302,311,312,313,314]
lightDrizzle=[300,310,321]
lightRain=[500,520]
Rain=[501,511,521]
HeavyRain=[502,503,504,522,531]
Snow=[601,602,616,621,622]
lightSnow=[600,611,612,615,620]
atmosphere=[701,711,721,731,741,751,761,762,771,781]
clear=[800,801]
clouds=[802,803,804]

def getWeather(currentWeather):
    for i in thunderstorm:
        if currentWeather == i:
            return "thunderstorm"
    for i in lightThunderstorm:
        if currentWeather == i:
            return "lightThunderstorm"
    for i in drizzle:
        if currentWeather == i:
            return "drizzle"
    for i in lightDrizzle:
        if currentWeather == i:
            return "lightDrizzle"
    for i in lightRain:
        if currentWeather == i:
            return "lightRain"
    for i in Rain:
        if currentWeather == i:
            return "rain"
    for i in HeavyRain:
        if currentWeather == i:
            return "heavyRain"
    for i in Snow:
        if currentWeather == i:
            return "snow"
    for i in lightSnow:
        if currentWeather == i:
            return "lightSnow"
    for i in atmosphere:
        if currentWeather == i:
            return "atmosphere"
    for i in clear:
        if currentWeather == i:
            return "clear"
    for i in clouds:
        if currentWeather == i:
            return "clouds"

def displayWeather(strip, weatherName, Rain, Snow):
    if weatherName == "lightThunderstorm":
        for i in range(5):
            spot = random.randint(4, 26)
            start = 100
            strip.setPixelColorRGB(spot, 100, 100, 100)
            strip.show()
            for x in range(20):
                start = start - 5
                if start < 0:
                    start = 0
                strip.setPixelColorRGB(spot, start, start, start)
                strip.show()
                time.sleep(0.1)
    if weatherName == "thunderstorm":
        for i in range(5):
            spot = random.randint(4, 26)
            start = 255
            strip.setPixelColorRGB(spot, 255, 255, 255)
            strip.setPixelColorRGB(spot+1, 255,255,255)
            strip.show()
            for x in range(40):
                start = start - 8
                if start < 0:
                    start = 0
                strip.setPixelColorRGB(spot, start, start, start)
                strip.setPixelColorRGB(spot+1, start, start, start)
                strip.show()
                time.sleep(0.03)
    if weatherName == "lightDrizzle" or weatherName == "lightRain" or weatherName == "drizzle":
        if Rain >= 0.025:
            start = 80
            for i in range(30):
                strip.setPixelColorRGB(i, 0,0,start)
                strip.show()
                time.sleep(0.02)
            for x in range(35):
                start = start - 2
                for i in range(30):
                    strip.setPixelColorRGB(i, 0,0,start)
                    strip.show()
                time.sleep(0.04)
            for x in range(35):
                start = start + 2
                for i in range(30):
                    strip.setPixelColorRGB(i, 0,0,start)
                    strip.show()
                time.sleep(0.04)
        else:
            weatherName = "clouds"
    if weatherName == "heavyRain" or weatherName == "rain" :
        start = 255
        for i in range(30):
            strip.setPixelColorRGB(i, 0,0,start)
            strip.show()
            time.sleep(0.02)
        for x in range(40):
            start = start - 6
            for i in range(30):
                strip.setPixelColorRGB(i, 0,0,start)
                strip.show()
            time.sleep(0.01)
        for x in range(40):
            start = start + 6
            for i in range(30):
                strip.setPixelColorRGB(i, 0,0,start)
                strip.show()
            time.sleep(0.01)
    if weatherName == "lightSnow" and Snow >= 0.025:
        start = 80
        for i in range(30):
            strip.setPixelColorRGB(i, start,start,start)
            strip.show()
            time.sleep(0.02)
        for x in range(40):
            start = start - 2
            for i in range(30):
                strip.setPixelColorRGB(i, start,start,start)
                strip.show()
            time.sleep(0.03)
        for x in range(40):
            start = start + 2
            for i in range(30):
                strip.setPixelColorRGB(i, start,start,start)
                strip.show()
            time.sleep(0.03)
    elif weatherName == "lightSnow" and Snow <0.025:
        weatherName = "clouds"
    if weatherName == "snow":
        start = 255
        for i in range(30):
            strip.setPixelColorRGB(i, start,start,start)
            strip.show()
            time.sleep(0.02)
        for x in range(40):
            start = start - 6
            for i in range(30):
                strip.setPixelColorRGB(i, start,start,start)
                strip.show()
            time.sleep(0.01)
        for x in range(40):
            start = start + 6
            for i in range(30):
                strip.setPixelColorRGB(i, start,start,start)
                strip.show()
            time.sleep(0.01)
    if weatherName == "atmosphere" or weatherName == "clouds":
        for i in range(30):
            strip.setPixelColorRGB(i, 0,0,0)
            strip.show()
            time.sleep(0.02)
    if weatherName == "clear":
        for i in range(30):
            strip.setPixelColorRGB(i, 90,180,0)
            strip.show()
            time.sleep(0.02)

def displayTemp(strip, previousTemp, currentTemp):
    if currentTemp >= previousTemp:
        diff = int(round((currentTemp-previousTemp)*6))
        if diff >255:
            diff = 255
        #strip.setBrightness(diff)
        for i in range(30,strip.numPixels()):
            strip.setPixelColorRGB(i, 0, diff, 0)

            strip.show()
            time.sleep(0.03)
    if currentTemp < previousTemp:
        diff = int(round((previousTemp-currentTemp)*6))
        if diff >255:
            diff = 255
        #strip.setBrightness(diff)
        for i in range(30,strip.numPixels()):
            strip.setPixelColorRGB(i, 0, 0,diff)

            strip.show()
            time.sleep(0.03)


def getRGB(RGBint):
    blue = RGBint & 255
    green = (RGBint >> 8) & 255
    red = (RGBint >> 16) & 255
    return red, green, blue
def getWeatherData(url):
    response = urllib.urlopen(url)
    jsonData = json.loads(response.read())
    return jsonData
def getWindChill(temp, windspeed):
    if temp <= 50 and windspeed >= 3:
        return round(35.74 + (.6215*temp)-(35.75*(windspeed**.16))+((.4275*temp)*(windspeed**.16)),1)
    else:
        return temp
def parseAlarmTime(hour, mode):
    if mode == "pm":
        if hour != 12:
            hour = hour + 12
        if hour == 24:
            hour = 0
    if mode == "am":
        if hour == 12:
            hour = 0
    return hour

#Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

print(strip.getPixelColor(1))
num = 0
for j in range(8):
    for i in range(strip.numPixels()):
        strip.setPixelColorRGB(i, 20,0,0,255)
        strip.show()
        num+=1
        time.sleep(.01)
print(strip.getPixelColor(1))
print(getRGB(strip.getPixelColor(1))[0])

conn=sqlite3.connect('/var/www/html/led_db')
conn.row_factory = sqlite3.Row
c=conn.cursor()

numOfExceptions = 0
time.sleep(5)
while True:
    try:
        c.execute('select * from mode')
        r = c.fetchone()
        selection = r[0]
        alarmHour = parseAlarmTime(r[3],r[5])
        alarmMinute = r[4]
        print(alarmHour)
        print(alarmMinute)

        if alarmHour == pendulum.now().hour and alarmMinute == pendulum.now().minute and alarmHour != 0 and alarmMinute != 0:
            selection = "weather"
            print("Alarm time, changed to weather")
            c.execute('UPDATE mode SET status="weather"')
            conn.commit()
        if alarmHour + 1 == pendulum.now().hour and alarmMinute == pendulum.now().minute and alarmHour != 0 and alarmMinute != 0:
            if selection == "weather":
                print("Turning off weather mode")
                selection = "none"
        
        if selection != "weather" and r[2] != "default":
            c.execute('UPDATE mode SET weatherTime="default"')
            conn.commit()
        if r[1] == "low":
            strip.setBrightness(20)
        if r[1] == "medium":
            strip.setBrightness(80)
        if r[1] == "high":
            strip.setBrightness(255)
        if selection == "red":
            colorWipe(strip, Color(0,255,0))
            #displayTemp(strip, 27.8,25.2)
            #displayWeather(strip, "thunderstorm")
        if selection == "green":
            colorWipe(strip, Color(255,0,0))
        if selection == "blue":
            colorWipe(strip, Color(0,0,255))
        if selection == "pink":
            colorWipe(strip, Color(0,255,120))
        if selection == "orange":
            colorWipe(strip, Color(70,255,0))
        if selection == "white":
            colorWipe(strip, Color(255,255,255), 5)
            for i in range(55,60):
                strip.setPixelColorRGB(i,0,0,0)
                strip.show()
                time.sleep(0.02)
        if selection == "none":
            colorWipe(strip, Color(0,0,0))
        if selection == "rainbow":
            rainbow(strip)
        if selection == "rainbow2":
            rainbowCycle(strip,40,1)
        if selection == "wild":
            theaterChase(strip, Color(0, 255,0))
            theaterChase(strip, Color(255, 0,0))
            theaterChase(strip, Color(0, 0,255))
            theaterChaseRainbow(strip)
        if selection == "colorStripes":
            colorWipe(strip, Color(random.randint(0,120),random.randint(0,120),random.randint(0,120)))
        if selection == "christmas":
            for i in range(40,60):
                strip.setPixelColor(i, Color(255,0,0))
                
            for i in range(20,39):
                strip.setPixelColor(i,Color(0,255,0))
                
            for i in range(0,19):
                strip.setPixelColor(i,Color(255,255,255))
            strip.show()
            time.sleep(2)
            for i in range(40,60):
                strip.setPixelColor(i, Color(255,255,255))
                
            for i in range(20,39):
                strip.setPixelColor(i, Color(255,0,0))
                
            for i in range(0,19):
                strip.setPixelColor(i, Color(0,255,0))
            strip.show()
            time.sleep(2)
            for i in range(40,60):
                strip.setPixelColor(i, Color(0,255,0))
                
            for i in range(20,39):
                strip.setPixelColor(i, Color(255,255,255))
                
            for i in range(0,19):
                strip.setPixelColor(i, Color(255,0,0))
            strip.show()
            time.sleep(2)
        if selection == "weather":
            previousDay = getPreviousDayValues()
            currentDay = getCurrentDayValues()
            if previousDay is None or currentDay is None:
                print("Weather cannot be computed, as there is incomplete weather data")
                colorWipe(strip, Color(165,255,0))
                time.sleep(2)
            else:
                if r[2] == "default":
                    if pendulum.now().hour >= 0 and pendulum.now().hour < 9:
                        displayTemp(strip, previousDay['temp1'], currentDay['temp1'])
                        displayWeather(strip, getWeather(currentDay['weather1']), currentDay['rain1'], currentDay['snow1'])
                    if pendulum.now().hour >= 9 and pendulum.now().hour < 15:
                        displayTemp(strip, previousDay['temp2'], currentDay['temp2'])
                        displayWeather(strip, getWeather(currentDay['weather2']), currentDay['rain2'], currentDay['snow2'])
                    if pendulum.now().hour >= 15 and pendulum.now().hour < 20:
                        displayTemp(strip, previousDay['temp3'], currentDay['temp3'])
                        displayWeather(strip, getWeather(currentDay['weather3']), currentDay['rain3'], currentDay['snow3'])
                        #displayWeather(strip, "snow", 0.08)
                    if pendulum.now().hour >=20 and pendulum.now().hour <= 24:
                        displayTemp(strip, currentDay['temp1'], currentDay['temp4'])
                        displayWeather(strip, getWeather(currentDay['weather4']), currentDay['rain4'], currentDay['snow4'])
                if r[2] == "nineWeather":
                    displayTemp(strip, previousDay['temp1'], currentDay['temp1'])
                    displayWeather(strip, getWeather(currentDay['weather1']), currentDay['rain1'], currentDay['snow1'])
                if r[2] == "threeWeather":
                    displayTemp(strip, previousDay['temp2'], currentDay['temp2'])
                    displayWeather(strip, getWeather(currentDay['weather2']), currentDay['rain2'], currentDay['snow2'])
                if r[2] == "weatherNine":
                    displayTemp(strip, previousDay['temp3'], currentDay['temp3'])
                    displayWeather(strip, getWeather(currentDay['weather3']), currentDay['rain3'], currentDay['snow3'])
                if r[2] == "nextWeather":
                    displayTemp(strip, currentDay['temp1'], currentDay['temp4'])
                    displayWeather(strip, getWeather(currentDay['weather4']), currentDay['rain4'], currentDay['snow4'])

        if selection == "shutdown":
            colorWipe(strip, Color(0,0,0))
            c.execute("UPDATE mode SET status='none'")
            conn.commit()
            conn.close()
            os.system('sudo shutdown -h now')

        time.sleep(0.2)

        now = pendulum.now()
        if now.hour >= 3 and now.minute >= 1:
            if pendulum.now().hour<4:
                print("Past 3:00 AM")
                c.execute('SELECT * FROM weather WHERE DateAccessed>datetime("now","localtime","start of day")')
                r = c.fetchone()
                if r is None:
                    print("No data entry for today, waiting a minute to gather data")
                    time.sleep(90)
                    weatherData = getWeatherData('http://api.openweathermap.org/data/2.5/forecast?id=4414001&appid=883e596b8d5b90f6f035a8d74d1161f3&units=imperial')
                    NineWeather = filter(lambda data: data['dt_txt'] == (pendulum.now().format('YYYY-MM-DD') + " 15:00:00"), weatherData['list'])
                    ThreeWeather = filter(lambda data: data['dt_txt'] == (pendulum.now().format('YYYY-MM-DD') + " 21:00:00"), weatherData['list'])
                    Weather9 = filter(lambda data: data['dt_txt'] == (pendulum.tomorrow().format('YYYY-MM-DD') + " 03:00:00"), weatherData['list'])
                    NextWeather = filter(lambda data: data['dt_txt'] == (pendulum.tomorrow().format('YYYY-MM-DD') + " 15:00:00"), weatherData['list'])
                    DateAccessed = pendulum.now().format('YYYY-MM-DD HH:mm:ss')
                    weather1 = NineWeather[0]['weather'][0]['id']
                    if 'rain' in NineWeather[0]:
                        if bool(NineWeather[0]['rain']):
                            rain1 = round(NineWeather[0]['rain']['3h'], 4)
                        else:
                            rain1 = 0
                    else:
                        rain1 = 0
                    if 'snow' in NineWeather[0]:
                        if bool(NineWeather[0]['snow']):
                            snow1 = round(NineWeather[0]['snow']['3h'], 4)
                        else:
                            snow1 = 0
                    else:
                        snow1 = 0
                    wind1 = NineWeather[0]['wind']['speed']
                    temp1 = getWindChill(NineWeather[0]['main']['temp'], wind1)

                    weather2 = ThreeWeather[0]['weather'][0]['id']
                    if 'rain' in ThreeWeather[0]:
                        if bool(ThreeWeather[0]['rain']):
                            rain2 = round(ThreeWeather[0]['rain']['3h'], 4)
                        else:
                            rain2 = 0
                    else:
                        rain2 = 0
                    if 'snow' in ThreeWeather[0]:
                        if bool(ThreeWeather[0]['snow']):
                            snow2 = round(ThreeWeather[0]['snow']['3h'], 4)
                        else:
                            snow2 = 0
                    else:
                        snow2 = 0
                    wind2 = ThreeWeather[0]['wind']['speed']
                    temp2 = getWindChill(ThreeWeather[0]['main']['temp'], wind2)

                    weather3 = Weather9[0]['weather'][0]['id']
                    if 'rain' in Weather9[0]:
                        if bool(Weather9[0]['rain']):
                            rain3 = round(Weather9[0]['rain']['3h'], 4)
                        else:
                            rain3 = 0
                    else:
                        rain3 = 0
                    if 'snow' in Weather9[0]:
                        if bool(Weather9[0]['snow']):
                            snow3 = round(Weather9[0]['snow']['3h'], 4)
                        else:
                            snow3 = 0
                    else:
                        snow3 = 0
                    wind3 = Weather9[0]['wind']['speed']
                    temp3 = getWindChill(Weather9[0]['main']['temp'], wind3)

                    weather4 = NextWeather[0]['weather'][0]['id']
                    if 'rain' in NextWeather[0]:
                        if bool(NextWeather[0]['rain']):
                            rain4 = round(NextWeather[0]['rain']['3h'], 4)
                        else:
                            rain4 = 0
                    else:
                        rain4 = 0
                    if 'snow' in NextWeather[0]:
                        if bool(NextWeather[0]['snow']):
                            snow4 = round(NextWeather[0]['snow']['3h'], 4)
                        else:
                            snow4 = 0
                    else:
                        snow4 = 0
                    wind4 = NextWeather[0]['wind']['speed']
                    temp4 = getWindChill(NextWeather[0]['main']['temp'], wind4)

                    c.execute('INSERT INTO weather (DateAccessed, weather1, rain1, snow1, temp1, weather2, rain2, snow2, temp2, weather3, rain3, snow3, temp3, weather4, rain4, snow4, temp4) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                              (DateAccessed, weather1, rain1, snow1, temp1, weather2, rain2, snow2, temp2, weather3, rain3, snow3, temp3, weather4, rain4, snow4, temp4))
                    conn.commit()

                else:
                    print("There is a data entry detected for today, " + pendulum.now().format('YYYY-MM-D'))
            else:
                print("Past 4:00 AM and can't grab weather data that late or theres already data today")
                print("Number of exceptions: " + str(numOfExceptions))
        else:
            print("Not past 3:00 AM yet")

    except KeyboardInterrupt:
        colorWipe(strip, Color(0,0,0))
        c.close()
        print("closed connection")
        break
    except Exception as e:
        print("Exception occured, printing exception and repeating loop")
        numOfExceptions += 1
        print("Number of exceptions: " + str(numOfExceptions))
        print(e)
        traceback.print_exc()
        time.sleep(3)
