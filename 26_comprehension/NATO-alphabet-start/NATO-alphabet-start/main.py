import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

def data_nacho():
    # my_dict1 = {}
    # for (index, row) in df.iterrows():
    #     my_dict1[row['letter']] = row['code']
    # return my_dict1
    return {row['letter']: row['code'] for (index, row) in df.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
my_dict = data_nacho()
name = input('Please enter your name: ').upper()
result = [my_dict[nam] for nam in name]

print(result)
