from prettytable import PrettyTable

# https://github.com/jazzband/prettytable

table = PrettyTable()
# print(table)

table.field_names = ['Pokemon name', 'Type']

table.add_row(['Pikachu', 'Electric'])
table.add_row(['Squirtle', 'Water'])
table.add_row(['Charmander', 'Fire'])
table.align = 'l'
print(table)