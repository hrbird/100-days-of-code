# Uses the Caesar Cipher mode of encryption to encode or decode secret messages.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

LOGO_ART = '''          
  ,adPPYba,  ,adPPYYba,   ,adPPYba,  ,adPPYba,  ,adPPYYba,  8b,dPPYba,  
 a8"     ""  ""     `Y8  a8P_____88  I8[    ""  ""     `Y8  88P'   "Y8  
 8b          ,adPPPPP88  8PP"""""""   `"Y8ba,   ,adPPPPP88  88          
 "8a,   ,aa  88,    ,88  "8b,   ,aa  aa    ]8I  88,    ,88  88          
  `"Ybbd8"'  `"8bbdP"Y8   `"Ybbd8"'  `"YbbdP"'  `"8bbdP"Y8  88   

                88               88                                 
                ""               88                                 
                                 88                                 
     ,adPPYba,  88  8b,dPPYba,   88,dPPYba,    ,adPPYba,  8b,dPPYba,  
    a8"     ""  88  88P'    "8a  88P'    "8a  a8P_____88  88P'   "Y8  
    8b          88  88       d8  88       88  8PP"""""""  88          
    "8a,   ,aa  88  88b,   ,a8"  88       88  "8b,   ,aa  88          
     `"Ybbd8"'  88  88`YbbdP"'   88       88   `"Ybbd8"'  88          
                    88                                             
                    88           
'''

# Ask the user for their choice.
# Parameters:
#   - low: integer of the lowest acceptable number
#   - high: integer of the highest acceptable number
# Returns an integer within the range.
def getNumberFromUser(low, high):
    while True:

        # Get input from user.
        choiceInput = input(f"> ").strip()

        # Validate that the input is a number within the range.
        if choiceInput.isnumeric() and int(choiceInput) >= low and int(choiceInput) <= high:

            # Return the choice as an int.
            return (int(choiceInput))

        else:
            # If the input is not acceptable, tell the player and keep looping.
            print(f"\nPlease enter a number between {low} and {high}.")

# Shifts each letter of the given 'text' forwards in the alphabet by the shift amount.
# parameters:
#   - text = the string message to encrypt
#   - shift = the integer amount to shift each letter
#   - direction = 1: encrypt message, 2: decrypt message
# Returns the encrypted text.
def cipher(text, shift, direction):
    
    new_text = ""

    # Loop through each character in the text.
    for t in text:
        
        # Check if the character is alphabetic.
        if t.isalpha():

            # Find the index of the letter in the alphabet list and add the shift amount.
            alphindex = alphabet.index(t)

            # If we're encrypting, shift forward. If we're decrypting, shift backward.
            # If the new index goes past z or before a, loop around to the other end of the alphabet.
            if direction == 1:
                alphindex += shift
                if alphindex > 25:
                    alphindex -= 26
            else:
                alphindex -= shift
                if alphindex < 0:
                    alphindex += 26


            # Add the new, encrypted letter to the new text.
            new_text += alphabet[alphindex]

        else:
            # If the character is not alphabetic, just add it as-is.
            new_text += t
    
    return new_text

# Main program
def main():
    print(LOGO_ART)
    
    print("What would you like to do?\nEnter a number from the menu:")
    print("  1. Encrypt a secret message")
    print("  2. Decrypt a secret message")
    direction = getNumberFromUser(low=1, high=2)

    text = input("\nType your message:\n> ").lower()

    print("\nEnter the shift number:")
    shift = getNumberFromUser(low=1, high=26)

    new_message = cipher(text=text, shift=shift, direction=direction)
    print(f"\nYour new message is:\n{new_message}\n")

main()

# =============
# SAMPLE OUTPUT
# =============
#
#   ,adPPYba,  ,adPPYYba,   ,adPPYba,  ,adPPYba,  ,adPPYYba,  8b,dPPYba,
#  a8"     ""  ""     `Y8  a8P_____88  I8[    ""  ""     `Y8  88P'   "Y8
#  8b          ,adPPPPP88  8PP"""""""   `"Y8ba,   ,adPPPPP88  88
#  "8a,   ,aa  88,    ,88  "8b,   ,aa  aa    ]8I  88,    ,88  88
#   `"Ybbd8"'  `"8bbdP"Y8   `"Ybbd8"'  `"YbbdP"'  `"8bbdP"Y8  88

#                 88               88
#                 ""               88
#                                  88
#      ,adPPYba,  88  8b,dPPYba,   88,dPPYba,    ,adPPYba,  8b,dPPYba,
#     a8"     ""  88  88P'    "8a  88P'    "8a  a8P_____88  88P'   "Y8
#     8b          88  88       d8  88       88  8PP"""""""  88
#     "8a,   ,aa  88  88b,   ,a8"  88       88  "8b,   ,aa  88
#      `"Ybbd8"'  88  88`YbbdP"'   88       88   `"Ybbd8"'  88
#                     88
#                     88

# What would you like to do?
# Enter a number from the menu:
#   1. Encrypt a secret message
#   2. Decrypt a secret message
# > 1
#
# Type your message:
# > hello world!
#
# Enter the shift number:
# > 15
#
# Your new message is:
# wtaad ldgas!