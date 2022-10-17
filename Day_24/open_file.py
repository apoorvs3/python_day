# with open('my_fil.txt') as file:   # doesn't require to manually close file
#     contents = file.read()
#     print(contents)


# with open('my_fil.txt', mode='w') as file:   # doesn't require to manually close file
#     contents = file.write('new text')


# with open('new_fil.txt', mode='a') as file:   # doesn't require to manually close file
#     contents = file.write('\nnew text')


with open('new_fil.txt', mode='w') as file:   # doesn't require to manually close file
    contents = file.write('new text')