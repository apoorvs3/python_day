import os

import requests
import smtplib
import os
# f45aaa1bc2cd448585314919233101
api_key = os.environ.get('api_key')
print(api_key)
end_point = 'http://api.weatherapi.com/v1/forecast.json?'
param = {
    'key': api_key,
    'q': 'Kanpur',
    'days': 1,
    'aqi': 'no',
    'alerts': 'no'
}
response = requests.get(url=end_point, params=param)
response.raise_for_status()
print(f'Status code: {response.status_code}')


Forecast = response.json()['forecast']['forecastday'][0]['hour']

weather = {}

for hour in range(24):
    text = Forecast[hour]['condition']['text']
    time = f"{Forecast[hour]['time']}"
    weather[time] = text

if 'Sunny' in weather.values():
    print('Put some lotion as its going to be a sunny day')
elif 'Rainy' in weather.values():
    print('Bring an umbrella')

