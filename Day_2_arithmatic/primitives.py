# Type error - print(len(1234555))

from traceback import print_tb


print('Hello'[0], end = ' ')
print('Hello'[-1])

print(124_456_34 * 23_45.0)

x = 5
if x:
    print(type(x))

print(type(True))
print(float('34')+ 56)

num_char = len(input('What is your name?'))
print('Your name is : ' + str(num_char)+ ' Characters long')