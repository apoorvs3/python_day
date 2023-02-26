# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

BMI = int(round((weight/height**2), 0))
if BMI<18.5:
    print(f'Your BMI is {BMI}, you are '+'\033[1m'+'underweight.')
elif BMI < 25:
    print(f'Your BMI is {BMI}, you have a '+'\033[1m'+'normal weight.')
elif BMI <30:
    print(f'Your BMI is {BMI}, you are '+'\033[1m'+'overweight.')
elif BMI < 35:
    print(f'Your BMI is {BMI}, you are '+'\033[1m'+'obese.')
else:
    print(f'Your BMI is {BMI}, you are '+'\033[1m'+'clinically obese.')





#Write your code below this line 👇
