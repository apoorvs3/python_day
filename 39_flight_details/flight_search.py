import requests
from datetime import datetime, timedelta


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, location: str):
        self.FLIGHT_API_KEY = 'NM8Y87WP24zVyQgjfiGAWv8nrCyfh2Rd'
        self.term = location

        self.body = {
            'fly_from': f'{self.term}',
            'date_from': f'{((datetime.today() + timedelta(days=2)).strftime("%d/%m/%Y"))}',
            'date_to': f'{(datetime.today() + timedelta(days=5)).strftime("%d/%m/%Y")}',
            'locale': 'en',
            'limit': 100
        }
        self.end_point = 'https://api.tequila.kiwi.com/v2/search'
        self.HEADER = {
            'accept': 'application/json',
            'apikey': self.FLIGHT_API_KEY
        }
        self.search_flights()

    def search_flights(self):
        response = requests.get(url=self.end_point, params=self.body, headers=self.HEADER).json()
        print(response)
