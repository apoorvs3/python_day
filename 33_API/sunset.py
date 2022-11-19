import requests
import datetime as dt

MY_LAT = 26.449923
MY_LONG = 80.331871

parameters = {
    "lat": MY_LAT,
    "lang": MY_LONG,
    "formatted": 0
}
response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
data = response.json()
response.raise_for_status()

sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

sunrise_hour = sunrise.split('T')[1].split(':')[0]
sunset_hour = sunset.split('T')[1].split(':')[0]
print(sunrise_hour)
print(sunset_hour)

hour_now = dt.datetime.now().hour
