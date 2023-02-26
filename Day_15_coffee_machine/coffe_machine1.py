MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_transaction_successful(money_received, drink_cost):
    """
    return true when amount is accepted
    :param money_received:
    :param drink_cost:
    :return:
    """
    if money_received >= drink_cost:
        global profit
        change = round(money_received - drink_cost, 2)
        profit += drink_cost
        print(f"Here is {change} in change")
        return True
    else:
        print("Sorry that's not enough money refunded")
        return False


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry there is not enough water")
            return False
    return True


def process_coin():
    """
    return total calculated from coins
    :return:
    """
    print('Please insert coins')
    total = int(input('How manu quarters: ')) * 0.25
    total += int(input('How manu dimes: ')) * 0.1
    total += int(input('How manu nickels: ')) * 0.05
    total += int(input('How manu pennies: ')) * 0.01
    return total

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'This is your {drink_name}')


profit = 0
is_on = True
while is_on:
    choice = input('What would you like? espresso, latte, cappuccino: ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coin()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])