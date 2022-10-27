import pandas as pd

df = pd.read_csv('50_states.csv')

# print(df[df['state'] == 'Alaska'])

boools = [True, True, False]

if False in boools:
    print('yup')