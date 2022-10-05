from operator import sub


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide

}


def calculator():
    num1 = float(input('What is the first number: '))
    continue_using = True
    for key in operations:
        print(key)
    while continue_using is True:
        operation_symbol = input('What operation do you want to do?: ')
        num2 = float(input('What is the second number: '))
        answer = operations[operation_symbol](num1, num2)
        print(f'{num1} {operation_symbol} {num2} gives {answer}')
        continue_using_calc = input(f'Do you want to reuse the calculator with {answer}? "yes" or "no"? or "quit" ').lower()
        num1 = answer
        if continue_using_calc == 'no':
            continue_using = False
            calculator()
        elif continue_using_calc == 'quit':
            break

calculator()
