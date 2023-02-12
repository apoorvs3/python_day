import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, body):
        self.body = body
        self.end_point = 'https://api.sheety.co/b010bd54119158b2ba704d53265f2684/flightData/sheet1'
        self.sheet_body = {
            'sheet1': self.body
        }
        self.update_sheet()

    def update_sheet(self):
        response = requests.post(url=self.end_point, json=self.sheet_body)
        print(response.text)
