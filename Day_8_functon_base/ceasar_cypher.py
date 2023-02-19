alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    message = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount

        if new_position > len(alphabet) - 1:  # exception case
            new_position = shift - (len(alphabet) - position)

        new_letter = alphabet[new_position]
        message += new_letter
    print(f'The encoded text is {message}')


def decrypt(cipher_text, shift_amount):
    message = ''
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        message += new_letter
    print(f'The decoded message is: {message}')


if direction == 'encode':
    encrypt(text, shift)
else:
    decrypt(text, shift)
