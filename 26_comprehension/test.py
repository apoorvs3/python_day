numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:

squared_numbers = [num ** 2 for num in numbers]
even_numbers = [num1 for num1 in numbers if num1 % 2 == 0]

# Write your code 👆 above:

print(squared_numbers)
print(even_numbers)