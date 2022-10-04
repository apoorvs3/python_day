from replit import clear
from art import logo
import os

# HINT: You can call clear() to clear the output in the console.

print(logo)
other_player = True
auction_dict = {}
while other_player:
    name = input('What is your name?: ')
    bid = float(input('What is your bid?: '))
    auction_dict[name] = bid
    other_bidders = input('Are there any other bidders? ').lower()
    if other_bidders == 'no':
        other_player = False
    else:
        clear()


max_ = 0
name_bidder = ''
for key in auction_dict:
    if auction_dict[key] > max_:
        max_ = auction_dict[key]
        name_bidder = key
print(f'The winner is {name_bidder} with a bet of ${max_}')
