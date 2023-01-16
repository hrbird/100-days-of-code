import math
print("Let's do some basic math!\n")

# Get two numbers from the user.
numA = input("Please enter a number: ")
numB = input("Please enter another number: ")

# Check that the user entered numbers, not strings.
try:
    a = float(numA)
    b = float(numB)
    
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} ^ {b} = {a ** b}")

    print(f"\n{a} / {b} = {(a / b):.2f}")
    print(f"{a} / {b} rounded down: {math.floor(a / b)}")
    print(f"{a} / {b} rounded up: {math.ceil(a / b)}")
    print(f"{a} / {b} rounded to nearest whole number: {round(a / b)}")

except ValueError:
    print(f"Oops, you did not enter two numbers!")


# -----------------
# - SAMPLE OUTPUT -
# -----------------
# Let's do some basic math!
# 
# Please enter a number: 15
# Please enter another number: 4
# 15.0 + 4.0 = 19.0
# 15.0 - 4.0 = 11.0
# 15.0 * 4.0 = 60.0
# 15.0 ^ 4.0 = 50625.0
# 
# 15.0 / 4.0 = 3.75
# 15.0 / 4.0 rounded down: 3
# 15.0 / 4.0 rounded up: 4
# 15.0 / 4.0 rounded to nearest whole number: 4
