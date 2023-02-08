import os

import requests
from Sheetify import SheetIfy
from datetime import datetime
from dotenv import load_dotenv, find_dotenv

load_dotenv('./environ.env')
APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')
WEIGHT = 72.5
HEIGHT = 153.45
AGE = 26

HEADERS = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}
BODY = {
    "gender": "male",
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

end_point = 'https://trackapi.nutritionix.com/v2/natural/exercise'


def get_response(inp_):
    BODY['query'] = inp_
    response = requests.post(url=end_point, json=BODY, headers=HEADERS).json()
    return response


Inp = input('Tell me the exercise you did today: ')
if type(Inp) != str:
    print('Not a valid word')
else:
    nutrition_response = get_response(Inp)
    num_of_exercise = len(nutrition_response["exercises"])
    values = nutrition_response
    temp_body = {}
    for num in range(num_of_exercise):
        temp_body['duration'] = f'{nutrition_response["exercises"][num]["duration_min"]}'
        temp_body['exercise'] = f'{nutrition_response["exercises"][num]["name"]}'
        temp_body['calories'] = f'{nutrition_response["exercises"][num]["nf_calories"]}'
        temp_body['date'] = datetime.now().strftime('%d/%m/%Y')
        temp_body['time'] = datetime.now().strftime('%H:%M:%S')
        print(temp_body)
        sheet = SheetIfy(body=temp_body)
# I ran for 5 minutes and did yoga for 10 minutes