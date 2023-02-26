"""
welcome to the black jack by joker
"""
import random

cards_on_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
added_in_func = 0
temp = 0


def generate_new_card(cards_in_deck):
    card = random.choice(cards_in_deck)
    return card


def show_card(computer_total, player_total):
    global temp, added_in_func
    if check_bust(player_total):
        return 'lost'
    elif player_total == 21:
        if check_black_j(computer_total):
            return 'draw'
        else:
            return 'won'
    else:  # Player total is less than 21
        temp = computer_total
        while computer_total < 17:
            computer_total +=  generate_new_card(cards_on_deck)
        added_in_func = computer_total - temp
        if check_bust(computer_total):
            return 'won'
        elif check_draw(computer_total, player_total):
            return 'draw'
        elif computer_total < player_total:
            return 'won'
        else:
            return 'lost'


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
computer_card_2 = generate_new_card(cards_on_deck)

print(f'Your deck of card reveals: {player_card_1} and {player_card_2}')
print(f'Computer card reveals card as {computer_card_1}')
show_cards = input("if you would like to show then type 'show' else if you want to Hit type 'hit': ").lower()

player_tot = player_card_1 + player_card_2
computer_tot = computer_card_1 + computer_card_2
card_n = 0
while show_cards == 'hit':
    card_n = generate_new_card(cards_on_deck)
    player_tot += card_n
    if player_tot > 21:
        print(f'You loose the game, your total is {player_tot}')
        break
    else:
        print(f'cards total fr you is: {player_tot}')
        show_cards = input("if you would like to show then type 'show' else if you want to Hit type 'hit': ").lower()
if show_cards == 'show':
    """
    show the hand of computer
    """
    result = show_card(computer_tot, player_tot)
    computer_tot += added_in_func
    print(f'The game is {result} \nYour total: {player_tot}\nComputer total: {computer_tot}')
