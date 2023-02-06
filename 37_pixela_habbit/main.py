import requests
from datetime import datetime

end_point = 'https://pixe.la/v1/users'
USER_NAME = 'apoorv'
TOKEN = 'turmenishtam32ffgg'
user_params = {
    'token': TOKEN,
    'username': USER_NAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
# response = requests.post(url=end_point, json=user_params)
# print(response.text)

graph_endpoint = f'{end_point}/{USER_NAME}/graphs'
graph_config = {
    'id': 'graph1',
    'name': 'Cycling graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'shibafu'
}
header = {
    'X-USER-TOKEN': TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)


pixel_end_point = f'{end_point}/{USER_NAME}/graphs/{graph_config["id"]}'
pixel_params = {
    'date': f'{datetime.now().strftime("%Y%m%d")}',
    'quantity': '17.2'
}
# response = requests.post(url=pixel_end_point, json=pixel_params, headers=header)
# print(response.text)

# put

pixel_put_params = {
    'name': 'Cycling graph',
    'date': f'{datetime.now().strftime("%Y%m%d")}',
    'quantity': '21.2'
}
# response = requests.put(url=pixel_end_point, json=pixel_put_params, headers=header)
# print(response.text)

delete_end = pixel_end_point
response = requests.delete(url=delete_end, headers=header)
print(response.text)
