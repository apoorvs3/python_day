# File not found
# with open('a_file.txt') as file:
#     file.read()

# keyerror
# Index error - out of bound
# type error

"""
try: Something that might cause an exception
except: Do this is there was an exception
else: Do this is there was no exceptiom
finally: Do this no matter what happens
"""
# try:
#     file = open('a_file.txt')
#     a_dict = {'key': 'value'}
#     print(a_dict['key'])
# except FileNotFoundError:
#     file = open('a_file.txt', mode='w')
#     file.write('something')
# except KeyError as error_message:
#     print(f'key not exist with error: {error_message}')
# else:
#     print(file.read())
# finally:
#     raise KeyError
#     # file.close()
#     # print('The file is closed')


# our own exceptions

# height = float(input('Height: '))
# weight = float(input('Weight: '))
#
# if height > 3:
#     raise ValueError('Human height sjould not go above than 3 m')
#
# bmi = weight / (height ** 2)
# print(f'Your BMI is: {bmi}')


# exercise

fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as e:
        print('Have a fruit Pie')
        print(f'Not so many fruits because: {e}')
    else:
        print(fruit + " pie")


make_pie(5)
