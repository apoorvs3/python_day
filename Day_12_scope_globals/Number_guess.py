ANSWER = 17


def choose_number(level):
    if level == 'easy':
        print(f'You have 10 attempts to guess the number\n')
        attempts = 10
    else:
        print(f'You have 5 attempts to guess the number\n')
        attempts = 5
    num = 1
    while attempts > 0:
        guess = int(input('Make a Guess! -- '))
        if guess < ANSWER:
            print(f'You are going cold')
        elif guess > ANSWER:
            print(f'You are getting too hot')
        else:
            print(f'You have guessed the {guess} correctly')
            break
        attempts -= 1
        if attempts == 0:
            print(f'You are unable to guess the number')


print(f'Welcome to the Number Guessing Game! ')
print(f'i\'m thinking of a number b/w 1 and 100.')
level_difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\'\n').lower()
choose_number(level_difficulty)
