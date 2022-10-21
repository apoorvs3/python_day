import pandas as pd

content = pd.read_csv('weather_data.csv')
temp = content['temp']


print(temp.to_dict())
temp_list = temp.to_list()

print(sum(temp_list)/len(temp_list))
print(temp.mean())
print(temp.max())
print(temp)

print(content[content['day'] == 'Monday'])
print(content[content['temp'] == temp.max()])

monday = content[content.day == 'Monday']
print(monday.condition)


data_dict = {
    "student" : ['Raju', 'Shyam', 'Babu Rao'],
    "scores" : [67, 92, 41]
}

print(pd.DataFrame(data_dict))