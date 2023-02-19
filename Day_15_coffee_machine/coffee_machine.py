"""
1. make 3 hot flavours - espresso(50W, 18C) , latte (200W, 24C, 150M), cappuccino (250M, 24C, 100M)
2. Coin Operated (penny 1c, dime 10c, nickel 5c, quarter 25c)


prog req
1. Print report
2. Check resources are sufficient?
3. Process coins Check coins are sufficient?
4. make coffee
"""
from data import MENU

DIME_VALUE = 0.1
PENNY_VALUE = 0.01
QUARTER_VALUE = 0.25
NICKEL_VALUE = 0.05

water_ = 300
milk_ = 200
coffee_ = 100
money = 0

# TODO 2 : Turn off the Coffee Machine by entering “off” to the prompt.
machine_on = True


# TODO 3: Print report.
def get_report():
    print(f'Water: {water_}\nMilk: {milk_}\nCoffee:{coffee_}\n')


# TODO 4 : Check resources sufficient?
def check_resource_sufficient(type_of_coffee):
    global water_, coffee_, milk_, machine_on
    if type_of_coffee == 'espresso':
        if water_ < 50 or coffee_ < 18:
            print('Ingredients not enough')
            machine_on = False
            return False
    elif type_of_coffee == 'latte':
        if water_ < 250 or coffee_ < 24 or milk_ < 150:
            print('Ingredients not enough')
            machine_on = False
            return False
    elif type_of_coffee == 'cappuccino':
        if water_ < 250 or coffee_ < 24 or milk_ < 150:
            print('Ingredients not enough')
            machine_on = False
            return False
    return True


# TODO 5 : Process coins.
def process_coins(quarter, dime, nickel, penny):
    return quarter * 0.25 + dime * 0.1 + nickel * 0.05 + penny * 0.01


# TODO 6 : Check transaction successful?
def process_transaction(quarter, dime, nickel, penny, type_of_coffee):
    global money
    money_received = process_coins(quarter, dime, nickel, penny)
    price = MENU[type_of_coffee]['cost']
    if money_received >= price:
        money += price
        if money_received > price:
            print(f'Here is your change of {money_received - price}')
    else:
        print('Not enough money inserted')


# TODO 7 : Make Coffee

def process_ingredients(type_of_coffee):
    global water_, coffee_, milk_
    if check_resource_sufficient(type_of_coffee) is True:
        if type_of_coffee == 'espresso':
            water_ -= 50
            coffee_ -= 18
            return '☕ enjoy you espresso! '
        elif type_of_coffee == 'latte':
            water_ -= 200
            coffee_ -= 24
            milk_ -= 150
            return '☕ enjoy you Latte! '
        elif type_of_coffee == 'cappuccino':
            water_ -= 250
            coffee_ -= 24
            milk_ -= 100
            return '☕ enjoy you cappuccino! '


# TODO 1 : Prompt user by asking “What would you like? (espresso/latte/cappuccino)
while machine_on is True:
    coffee = input(
        'What would you like? \n'
        'For a strong espresso Type "e"\n'
        'For a mild latte Type "l"\n'
        'For a light cappuccino Type "c"\n').lower()
    while coffee not in ('c', 'l', 'e'):
        if coffee == 'report':
            get_report()
            coffee = ''  # in order to not prepare coffee with previous data
            break
        elif coffee == 'off':
            machine_on = False
            break
        else:
            coffee = input('That\'s not a valid choice please try again\n')

    quarters = int(input('How many Quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickels = int(input('How many nickels?: '))
    pennies = int(input('How many pennies?: '))

    if coffee == 'e':
        coffee = 'espresso'
    elif coffee == 'l':
        coffee = 'latte'
    elif coffee == 'c':
        coffee = 'cappuccino'

    process_transaction(quarters, dimes, nickels, pennies, coffee)
    process_ingredients(coffee)
