# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


T_counter = (name1+name2).lower().count('t')
R_counter = (name1+name2).lower().count('r')
U_counter = (name1+name2).lower().count('u')
E_counter = (name1+name2).lower().count('e')

first_dig = T_counter+R_counter+U_counter+E_counter

L_counter = (name1+name2).lower().count('l')
O_counter = (name1+name2).lower().count('o')
V_counter = (name1+name2).lower().count('v')
E_counter = (name1+name2).lower().count('e')

second_dig = L_counter+O_counter+V_counter+E_counter

result = int(str(first_dig)+ str(second_dig))

if result <10 or result > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result >=40 and result <=50:
    print(f'Your score is {result}, you are alright together.')
else:
    print(f'Your score is {result}.')
