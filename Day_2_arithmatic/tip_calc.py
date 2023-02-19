print('Welcome to the tip calculator!')
food_bill = float(input('What was the total bill? $'))
tip_percent = int(input('How much tip would you like to give? 10, 12, or 15? '))

total_bill = food_bill * (1+tip_percent/100)
num_people = int(input('How many people to split the bill?'))
bill_per_person = "%0.2f" %(total_bill/num_people)
print(f'Each person should pay: ${bill_per_person}')