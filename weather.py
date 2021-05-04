#!/usr/bin/env python
import requests
import json
from sys import stderr
from pprint import pprint

response = requests.get('https://api.forecast.io/forecast/5e2226c786c32cbfcd925a75f52f9494/51.531801,-0.060318?units=uk')
data = json.loads(response.content)

#pprint(data, stream=stderr)

current_summary = data['currently']['summary']
temp_c = data['currently']['temperature']
temp_f = (temp_c * 9.0 / 5) + 32
app_temp_c = data['currently']['apparentTemperature']
app_temp_f = (app_temp_c * 9.0 / 5) + 32
humidity = data['currently']['humidity']
wind_bearing = data['currently']['windBearing']
wind_compass = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'N'][int(wind_bearing / 45.0 + 0.5)]
wind_speed = data['currently']['windSpeed']
minute_summary = data['minutely']['summary']
day_summary = data['daily']['summary']

feels_like = ''
if app_temp_c != temp_c:
    feels_like = u' (feels like %.1f\u00b0)' % (
        app_temp_c,
    )

msg = u'Currently %.1f\u00b0C%s, humidity %s%%, wind: %s at %.0fmph. %s %s' % (
    temp_c,
    feels_like,
    int(humidity * 100),
    wind_compass,
    wind_speed,
    minute_summary,
    day_summary,
)
print (msg.encode('utf-8'))
