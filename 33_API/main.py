import requests

"""
1XX: Hold On
2XX: Here you go
3XX: Go away
4XX: You Screwed up
5XX: I Screwed up
"""


# response = requests.get(url='http://api.open-notify.org/iss-now.json')
response = requests.get(url='https://opentdb.com/api.php?amount=10&type=boolean')
response.raise_for_status()

data = response.json()
print(data)
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
