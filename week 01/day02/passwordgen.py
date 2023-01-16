# Generates a random, secure password with a given number of letters, symbols, and numbers.
# The specific characters and their order are randomized.

import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters= int(input("How many letters would you like in your password? > ")) 
num_symbols = int(input(f"How many symbols would you like? > "))
num_numbers = int(input(f"How many numbers would you like? > "))

password = []

# Get the given number of random letters and append them to the password.
for l in range(num_letters):
    randIndex = random.randint(0, len(letters) - 1)
    password.append(letters[randIndex])

# Get the given number of random symbols and append them to the password.
for s in range(num_symbols):
    randIndex = random.randint(0, len(symbols) - 1)
    password.append(symbols[randIndex])

# Get the given number of random numbers and append them to the password.
for s in range(num_numbers):
    randIndex = random.randint(0, len(numbers) - 1)
    password.append(numbers[randIndex])

# Shuffle the characters in the password list.
random.shuffle(password)

# Print the new password as a string.
print("\nYour new password is:")
print("".join(password))
