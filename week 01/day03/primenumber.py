# Checks whether or not a given number is a prime number.
# Receives parameter:
#   - number: integer to check
# Returns:
#   - True if the number is prime
#   - False if the number is not prime
def prime_checker(number):

    # A number is prime if it is only divisible by 1 and itself.
    # Loop through each integer from 2 to the number to check whether
    # the number is divisible by any other number.
    for x in range(2, number):
        if number % x == 0:
            return False

    return True
    

num = int(input("Enter an integer number: "))

if prime_checker(number = num):
    print(f"{num} is prime!")
else:
    print(f"{num} is not prime.")