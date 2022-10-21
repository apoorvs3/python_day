# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def read_letter(main_contentz_loc, string_to_replace_loc):
    with open(main_contentz_loc, mode='r') as file:
        main_content = file.read()

    with open(string_to_replace_loc, mode='r') as file:
        names = file.read()
        string_to_replace = names.split()
    return main_content, string_to_replace


def write_letters(content_, name_):
    with open(f'./Output/ReadyToSend/{name_}.txt', mode='w') as file_:
        file_.write(content_)


content, name_list = read_letter(main_contentz_loc='./Input/Letters/starting_letter.txt',
                                 string_to_replace_loc='./Input/Names/invited_names.txt')
for name in name_list:
    new_letter = content.replace('[name]', name.strip())
    write_letters(new_letter, name)
