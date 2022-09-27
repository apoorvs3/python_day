from msilib import PID_TITLE
import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
lis = ['rock', 'paper', 'scissors']
computer_choice = random.choice(lis)
person_inp = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scirros.'))
print(computer_choice)
print(lis[0])

if computer_choice == lis[0]:
    print('Computer: ')
    print(rock)
    if person_inp == 0:
        print('Stalemate')
        print('You: ')
        print(rock)
    elif person_inp == 1:
        print('You win !')
        print('You: ')
        print(paper)
    elif person_inp == 2:
        print('Computer win !')
        print('You: ')
        print(scissors)
elif computer_choice == lis[1]:
    print('Computer: ')
    print(paper)
    if person_inp == 0:
        print('Computer wins! ') 
        print('You: ')
        print(rock)
    elif person_inp == 1:
        print('Stalemate')
        print('You: ')
        print(paper)
    elif person_inp == 2:
        print('You win !')
        print('You: ')
        print(scissors)
elif computer_choice == lis[2]:
    print('Computer: ')
    print(scissors)
    if person_inp == 0:
        print('You win! ')
        print('You: ')
        print(rock)
    elif person_inp == 1:
        print('Computer wins!')
        print('You: ')
        print(paper)
    elif person_inp == 2:
        print('Stalemate')
        print('You: ')
        print(scissors)
