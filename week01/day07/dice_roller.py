# This program simulates rolling dice for table-top roleplaying games, 
# like DND or Pathfinder.
# It can roll dice with 4, 6, 8, 10, 12, 20, or 100 sides.

import math
import random

# Art by Joan G. Stark, from: https://www.asciiart.eu/miscellaneous/dice
DICE_ART = """
   .-------.    ______
  /   o   /|   /\     \\          _ _          
 /_______/o|  /o \  o  \\      __| (_) ___ ___ 
 | o     | | /   o\_____\\    / _` | |/ __/ _ \\
 |   o   |o/ \o   /o    /   | (_| | | (_|  __/
 |     o |/   \ o/  o  /     \__,_|_|\___\___|
 '-------'     \/____o/
"""

MENU_STR = """
Welcome to the Dice Roller!

Please enter the dice you would like to roll, in dice format.

For example, if you enter:
    2d4         I will roll 2 4-sided dice.
    3d6+1       I will roll 3 6-sided dice and add 1.
    4d10-2      I will roll 4 10-sided dice and subtract 2.
    1d100       I will roll 1 100-sided die.
    Q           I will quit the program."""


def roll_dice(num_dice, num_sides, mod_amount = 0):
    """Simulates rolling dice.

    Args:
        num_dice (int): the number of dice to roll
        num_sides (int): the number of sides on the dice
        mod_amount (int): the modifier amount to add or subtract
    """
    
    # Roll the dice and store them in a list.
    rolls = []
    for d in range(num_dice):
        rolls.append(random.randint(1, num_sides))

    # Modifier string.
    mod_str = ""
    if mod_amount > 0:
        mod_str = f"+{mod_amount}"
    elif mod_amount < 0:
        mod_str = mod_amount

    # Display the individual rolls.
    roll_str = ""
    for r in rolls:
        roll_str += f"{r} "

    print(f"I rolled: {roll_str} {mod_str}")
    print(f"Total: {sum(rolls) + mod_amount}")


def parse_dice(dice_str):
    """Parses dice notation, rolls the dice, and returns the result.

    Args:
        dice_str (string): A string in dice notation (EG "3d6")

    Returns the integer result of the dice roll, or -1 for bad input.
    """

    # Clean up the string.
    dice_str = dice_str.lower().replace(" ","")

    # Find the index of the "d" in the string.
    d_index = dice_str.find("d")
    if d_index == -1:
        # If "d" is not found, return False to signify bad input.
        return False

    # Find whether there is a + or - modifier at the end.
    mod_index = dice_str.find("+")
    if mod_index == -1:
        mod_index = dice_str.find("-")

    # Get the number of dice to roll.
    num_dice_str = dice_str[:d_index]
    if not num_dice_str.isdecimal():
        # If the characters before "d" aren't all digits, return False.
        return False
    num_dice = int(num_dice_str)

    # Get the type of dice to roll.
    num_sides_str = ""
    if mod_index == -1:
        # If there's no + or - modifier, the dice type should be at the end.
        num_sides_str = dice_str[(d_index + 1) :]
    else:
        num_sides_str = dice_str[(d_index + 1) : mod_index]

    if not num_sides_str.isdecimal():
        # If the characters aren't all digits, return False.
        return False
    num_sides = int(num_sides_str)

    # Find the modifier amount to add or subtract.
    mod_amount = 0
    if mod_index != -1:
        mod_str = dice_str[mod_index + 1 :]

        if not mod_str.isdecimal():
            return False
        mod_amount = int(mod_str)

        if dice_str[mod_index] == "-":
            mod_amount = -mod_amount

    # Roll the dice.
    print(f"\nRolling {dice_str}...")
    roll_dice(num_dice=num_dice, num_sides=num_sides, mod_amount=mod_amount)

    # Return True for a successful roll.
    return True

def show_menu():
    """Shows the main menu and gets dice input from the user.
    Keeps looping until the user quits the program.
    """
    print(DICE_ART)
    print(MENU_STR)

    quit_program = False
    while not quit_program:

        # Get input from user.
        input_str = input("\n> ")

        if len(input_str) > 0 and input_str[0].upper() == "Q":
            print("\nGoodbye!\n")
            quit_program = True

        else:
            roll_success = parse_dice(input_str)
            if roll_success:
                print("\nPlease enter another roll, or Q to quit.")
            else:
                print(f"\nSorry, I couldn't understand: {input_str}")
                print("Please use the correct dice notation.")

def main():
    show_menu()
    
if __name__ == "__main__":
    main()
