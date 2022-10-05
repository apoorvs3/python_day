

from operator import sub


def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide

}

continue_using = True
continue_using_calc = 'no'
while continue_using:
    num1 = int(input('What is the first number: '))
    if continue_using_calc == 'yes':
        num1 = answer
    else:
        continue_using = False

    for key in operations:
        print(key)
    operation_symbol = input('What operation do ypou want to do?: ')
    num2 = int(input('What is the second number: '))
    answer = operations[operation_symbol](num1, num2)

    print(f'{num1} {operation_symbol} {num2} gives {answer}')

    continue_using_calc = input('Do you want to resuse the calculator? "yes" or "no"? ').lower()
  


