import requests

# api_key='315a1e7c7a790f7f7a68762d287c211a'
# end_point = 'https://api.openweathermap.org/data/2.5/weather'

end_point = 'https://api.open-meteo.com/v1/forecast'
parameters = {
    'latitude': 52.52,
    'longitude': 13.41,
    'hourly': 'temperature_2m'
}

response = requests.get(end_point, params=parameters)
response.raise_for_status()
result = response.json()
hourly_time = result['hourly']['time'][0:11]
temperature_ = result['hourly']['temperature_2m'][0:11]
weather_data = {}
for num in range(len(hourly_time)):
    weather_data[hourly_time[num]] = temperature_[num]

for key in weather_data:
    if weather_data[key] < 1:
        print('Take an umbrella')
        break