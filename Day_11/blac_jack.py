"""
welcome to the black jack by joker
"""
import random

cards_on_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_tot = 0
computer_tot = 0


def generate_new_card(cards_in_deck):
    card = random.choice(cards_in_deck)
    return card


def show_card(computer_total, player_total):
    if check_bust(player_total):
        return 'loose'
    elif player_total == 21:
        if check_black_j(computer_total):
            return 'draw'
        else:
            return 'win'
    else:  # Player total is less than 21
        while computer_total < 17:
            computer_total += generate_new_card()
        if check_bust(computer_total):
            return 'win'
        elif check_draw(computer_total, player_total):
            return 'draw'
        elif computer_total < player_total:
            return 'win'
        else:
            return 'loose'


def check_black_j(total):
    if total == 21:
        return True
    else:
        return False


def check_bust(total):
    if total > 21:
        return True
    else:
        return False


def check_draw(computer_total, player_total):
    if computer_total == player_total:
        return True
    else:
        return False


print('********** Welcome to the black jack in Kanpuriya Casino **********')
player_card_1 = generate_new_card(cards_on_deck)
player_card_2 = generate_new_card(cards_on_deck)
computer_card_1 = generate_new_card(cards_on_deck)
print(f'Your deck of card reveals: {player_card_1} and {player_card_2}')
print(f'Computer card reveals card as {computer_card_1}')
show_cards = input("if you would like to show then type 'yes' else if you want to Hit type 'no': ").lower()

if show_cards == 'no':
