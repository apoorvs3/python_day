size = input(
    'What size of Pizza are you looking for small "S", medium "M" or large "L": ')
add_pepperoni = input('Would you like to add pepperoni "Y" or "N": ')
add_cheese = input('Would you like some extra cheese "Y" or "N": ')
bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3
if add_cheese == 'Y':
    bill += 1

print(f'Your final bill is: ${bill}')