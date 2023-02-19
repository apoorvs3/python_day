import requests
from flight_search import FlightSearch


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.end_point = 'https://api.sheety.co/b010bd54119158b2ba704d53265f2684/flightData/sheet1'
        self.response = requests.get(url=self.end_point).json()
        self.my_prices = [(x['lowestPrice'], x['city']) for x in self.response["sheet1"]]

    def check_sheet(self):
        price_list = {}
        num_places = len(self.response['sheet1'])
        for num in range(num_places):
            fs = FlightSearch(fly_to=f'{self.response["sheet1"][num]["iataCode"]}')
            price = fs.search_flight_price()
            price_list[f'{self.response["sheet1"][num]["city"]}'] = price
        return price_list

