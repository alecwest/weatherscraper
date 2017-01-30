# -*- coding: utf8 -*-
#!/usr/bin/python

# https://www.wunderground.com/weather/api/d/docs?d=data/index

import urllib2
import json

class weather:
    def __init__(self):
        self.temp_f = 0
        self.location = ""
        self.wind = ""

    def forecast(self, city, state, num_days=10):
        if num_days > 10:
            num_days = 10
        elif num_days < 1:
            num_days = 1
        self.location = city + ", " + state
        city = city.replace(" ", "_")
        data = urllib2.urlopen(
            'http://api.wunderground.com/api/1a33fe126e16bb72/forecast10day/q/%s/%s.json'
            % (state, city))
        json_string = data.read()
        parsed_json = json.loads(json_string)
        
        # Print based on number of days requested
        for i in range (0, num_days):
            day = parsed_json['forecast']['simpleforecast']['forecastday'][i]
            
            # Date
            if i == 0:
                print "For Today: "
            elif i == 1:
                print "For Tomorrow: "
            else:
                print "For %s:" % day['date']['weekday'] 

            # High/Low
            print "\tHigh: %s" % day['high']['fahrenheit']
            print "\tLow:  %s" % day['low']['fahrenheit']
            
            # Weather and chance of rain/snow
            if (day['conditions'] == "Chance of Rain" or day['conditions'] == "Chance of Snow"):
                print "\t%s: %s%% " % (day['conditions'], day['pop'])
            else:
                print "\t%s" % day['conditions']
                print "\tChance of Rain: %s%%" % day['pop']
            
            # Wind speed
            print "\tWind: %s at %s mph\n" % (day['avewind']['dir'], day['avewind']['mph'])

        data.close()

def main():
    weather_report = weather()
    weather_report.forecast("Chattanooga", "TN", 10)

if __name__ == "__main__":
    main()