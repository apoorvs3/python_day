import random
import hang_art
from hang_art import logo

stage = hang_art.stages
word_list = ['adrvark', 'baboon', 'camel']
print(logo)
choosen_word = random.choice(word_list)
print(choosen_word)
# 

emp_list = []
for num in range(len(choosen_word)):
    emp_list.append('_')

lives = len(emp_list)
while '_' in emp_list and lives != 0:
    guess = input('Guess the letter: ').lower()
    if guess not in choosen_word:
        print(stage[lives])
        lives -= 1
        print(f'{lives} lives remaining')
    if lives == 0:
        print('Game over ! ')
        print(stage[0])
    if guess in emp_list:
        print(f'You have already choosen {guess}')
    for position in range(len(emp_list)):
        letter = choosen_word[position]
        if letter == guess:
            emp_list[position] = letter
    if '_' not in emp_list:
        print('You Win! ')
    print(emp_list)
