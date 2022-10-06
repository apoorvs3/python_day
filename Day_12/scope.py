enemies = 1


def increase_enemies():
    # global enemies
    enemies = 2  # a new variable is created here
    print(f'enemies from inside the function {enemies}')


increase_enemies()
print(f'enemies  outside the function {enemies}')

'''
does python have block space, yes and no - when variable is in function then it has local scope for if,else,
for, while loops it's not the same

'''

game_level = 3
villains = ['Skeleton', 'Zombie', 'Alien']
if game_level < 5:
    new_enemy = villains[0]

print(new_enemy)

'''
modifying global scope
'''

supes = 1


def increase_supes():
    global supes  # not a good practice
    supes += 1
    print(f'supes inside america {supes}')


increase_supes()
print(f'supes inside russia {supes}')

supes1 = 1


def increase_supes1():
    print(f'supes1 inside america are {supes1}')
    return supes1 + 1


supes1 = increase_supes1()
print(f'supes1 inside russia {supes1}')
