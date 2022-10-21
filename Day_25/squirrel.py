import pandas as pd

data = pd.read_csv('squirrel_count.csv')


# print(data['Primary Fur Color'].unique())


def return_count(colour):
    count = 0
    color_list = data['Primary Fur Color'].tolist()
    for color in color_list:
        if color == colour:
            count += 1
    return count


def angela_s(color):  # better than mine
    squirrel_count = len(data[data['Primary Fur Color'] == color])
    return squirrel_count


data_dict = {
    'color': ['Gray', 'Cinnamon', 'Black'],
    'count': [angela_s('Gray'), angela_s('Cinnamon'), angela_s('Black')]
}

df = pd.DataFrame(data_dict)
df.to_csv('created.csv')