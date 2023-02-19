from data_manager import DataManager


class FlightData:
    def __init__(self, flight_data):
        self.flightData = flight_data
        self.get_locations()

    def get_locations(self):
        print(type(self.flightData))
        locations = self.flightData['data']
        destinations = {}
        for num in range(int(len(locations)/33)):
            destinations['cityTo'] = locations[num]['cityTo']
            destinations['distance'] = locations[num]['distance']
            destinations['duration'] = locations[num]['duration']['total']
            destinations['price'] = locations[num]['price']
            print(destinations)
            dm = DataManager(body=destinations)
