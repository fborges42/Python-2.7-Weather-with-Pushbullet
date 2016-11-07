import urllib2
import json
import re
from pushbullet import Pushbullet

#get location by IP 
url = 'https://freegeoip.net/json/' 
response = urllib2.urlopen (url)
data = json.load (response)
city = data['region_name']
city = "Lisboa"

#get weather for the current location on OpenWeatherMap
response = urllib2.urlopen ('http://api.openweathermap.org/data/2.5/weather?q=' + city + ',uk&appid=bd82977b86bf27fb59a04b61b657fb6f')
data = json.load (response)

main = data['main']
temp = str(main['temp'] - 273) + "C"
humidity = str(main['humidity'])
wind = str(data['wind']['speed'])
clouds = str(data['clouds']['all'])

weather = data['weather']
description = weather[0]['description']

Title = "Weather in " + city + " " + description + " " + temp
Body = "Clouds " + clouds + "\n" + "Humidity is " + humidity + "\n" + "Wind " + wind

print Title
print Body

#send notification to pushbullet
api_key = "API_KEY"
pb = Pushbullet(api_key)
pb.push_note(Title, Body)
