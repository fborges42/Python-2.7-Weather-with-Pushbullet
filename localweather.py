#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import json
import re
from pushbullet import Pushbullet

#get weather for the current location on OpenWeatherMap
def GetYahooWeather(city, country):
    yahooWeather = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22"+city+"%2C%20"+country+"%22)%20and%20u%3D%27c%27&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
    response = urllib2.urlopen (yahooWeather)
    data = json.load(response)

    yahooChannel = data['query']['results']['channel']
    yahooItem = yahooChannel['item']
    yahooWeatherText = yahooItem['condition']['text']
    yahooWeatherTemp = yahooItem['condition']['temp'] + u'\N{DEGREE SIGN}' + yahooChannel['units']['temperature']
    title = city + " " + yahooWeatherTemp + " sky is " + yahooWeatherText
    return title

#get inspirational quote of the day
def GetQuoteOfTheDay():
    response = urllib2.urlopen('http://quotes.rest/qod.json')
    data = json.load(response)

    quotes = data['contents']['quotes'][0]
    quoteOfTheDay = quotes['quote'] + ' - ' + quotes['author']
    return quoteOfTheDay

#send notification to pushbullet
def SendPushBullet (title, body):
    api_key = "_INSERT_YOUR_API_HERE_"
    pb = Pushbullet(api_key)
    pb.push_note(title, body)

def main():
    #get location by IP
    url = 'https://freegeoip.net/json/'
    response = urllib2.urlopen (url)
    data = json.load (response)
    city = data['region_name']
    country = data['country_code']

    weather = GetYahooWeather(city, country)
    quoteOfTheDay = GetQuoteOfTheDay()
    SendPushBullet(weather, quoteOfTheDay)

if __name__ == "__main__":
    main()
