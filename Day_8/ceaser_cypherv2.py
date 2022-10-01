from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(logo)


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caesar_function(plain_text, shift_amount, direction_shift):
    message = ''
    position = new_position = 0
    for letter in plain_text:
        if letter not in alphabet:
            message += letter
            continue
        position = alphabet.index(letter)
        if direction_shift == 'encode':
            new_position = position + shift_amount
            if new_position > len(alphabet) - 1:  # exception case
                new_position = shift - (len(alphabet) - position)
        else:
            new_position = position - shift_amount
        new_letter = alphabet[new_position]
        message += new_letter

    print(f'{direction_shift}d text is {message}')
    input('Do you want to replay the game? yes or No: ').lower()


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_function(text, shift, direction)

    result = input('Type yes if you want to go again... ')
    if result == 'no':
        should_continue = False
        print('GoodBye! ')

