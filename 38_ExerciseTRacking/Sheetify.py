import os

import requests


class SheetIfy:
    def __init__(self, body):
        self.HEADER = {
            'Authorization': os.environ.get('Authorization')
        }
        self.SHEET_EP = 'https://api.sheety.co/b010bd54119158b2ba704d53265f2684/myWorkouts/workouts'
        self.SHEET_BODY = {'workout': body}
        self.write_row()

    def write_row(self):
        response = requests.post(url=self.SHEET_EP, json=self.SHEET_BODY,headers=self.HEADER)
        print(response.text)
