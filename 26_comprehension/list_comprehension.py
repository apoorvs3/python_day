# new_list = [new_item(put the expression here) for item in list]
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = 'Angela'
new_list = [letter for letter in name]
print(new_list)

new_ran = [car * 1.5 for car in range(1, 5)]
print(new_ran)

"""
conditional list comprehension

new_list = [new_item for item in list if test]
"""

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) <= 4]
print(short_names)

capital_names = [car.upper() for car in names if len(car) >= 5]
print(capital_names)
