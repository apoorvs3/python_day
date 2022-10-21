# with open('weather_data.csv', mode='r') as file:
#     content = file.readlines()
#     print(content)
# import csv
#
# with open('weather_data.csv', mode='r') as file:
#     content = csv.reader(file)
#     temperatures = []
#     for row in content:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)


import pandas as pd

data = pd.read_csv('weather_data.csv')
print(data['temp'])

data_dict = data.to_dict()
print(data_dict)