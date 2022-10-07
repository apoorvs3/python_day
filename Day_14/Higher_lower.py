import art
import random
from game_data import data
import os
from replit import clear

def creator(index):
    alias = data[index]['name']
    profession = data[index]['description']
    region = data[index]['country']
    return f"{alias}, a {profession} from {region}"


print(art.logo)
game_win = True
score = 0
ind_a = random.randint(0, len(data) - 1)
while game_win:
    followers_a = data[ind_a]['follower_count']
    print('Compare A:' + creator(ind_a))
    print(art.vs)

    ind_b = random.randint(0, len(data) - 1)
    while ind_b == ind_a:
        ind_b = random.randint(0, len(data) - 1)

    followers_b = data[ind_b]['follower_count']
    print(f'Against B: ' + creator(ind_b))

    user_input = input('Who has more followers? Type \'A\' or \'B\'').upper()
    if user_input == 'A' and followers_a > followers_b or user_input == 'B' and followers_a < followers_b:
        game_win = True
        score += 1
        ind_a = ind_b
        print(f'You are right, score: {score} \nFollowers for A {followers_a}, Followers for B {followers_b}')
        clear()
    else:
        game_win = False
        print(F'Sorry that\'s wrong, Game Over! \nFollowers for A {followers_a}, Followers for B {followers_b}')
