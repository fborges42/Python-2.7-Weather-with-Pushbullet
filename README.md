# Python-2.7-Weather-with-Pushbullet
Small script that fetches weather info based on IP localization and sends notifications using pushbullet API.
This script can be used on a scheduled daily task to send notifications thru pushbullet to your smartphone with weather info.

# Location Information
The weather info is based on IP. Meaning you might have problems if you're using proxies. 
This scripts uses location and country iso 2.
IP info is collected from https://freegeoip.net/json/.

# Weather info
Weather info comes from yahoo API you can change/check weather info from https://developer.yahoo.com/weather/.

#Quote of the day
The quote of the day data comes from http://quotes.rest/qod.json

#Pushbullet
First you have to install this: pip install Pushbullet.py
And then you can generate an API for you Pushbullet from the settings options.


