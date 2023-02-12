# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager


def sort_data(dict_: dict):
    minimum_price = min(dict_.values())
    my_prices = dm.my_prices
    for pri in my_prices:
        if pri[0] < minimum_price:
            NotificationManager(msg_body=f"You can visit {pri[1]} for ${pri[0]} within next 6 months")


if __name__ == '__main__':
    dm = DataManager()
    price_data = dm.check_sheet()
    sort_data(price_data)
