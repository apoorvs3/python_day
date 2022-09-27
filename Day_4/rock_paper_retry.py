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

game_images = [rock, paper, scissors]
person_inp = int(input('Please choose 0 for Rock, 1 for Paper and 2 for Scissors\n'))
computer_inp = random.randint(1, 2)

if person_inp < 0 or person_inp > 2:
    print('Out of expected values you loose')
else:

    print('person chooses\n'+game_images[person_inp])
    print('Comuper chooses\n'+ game_images[computer_inp])

    if person_inp == computer_inp:
        print('This is a Draw')
    elif computer_inp == 2 and person_inp == 0:
        print('You win')
    elif computer_inp == 0 and person_inp == 2:
        print('You loose')
    elif computer_inp < person_inp:
        print('You win')
    elif person_inp < computer_inp:
        print('You loose')
    else:
        print('You loose')
