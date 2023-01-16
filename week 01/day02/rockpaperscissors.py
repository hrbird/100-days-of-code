# A simple Rock, Paper, Scissors game. 
# The player enters their choice while the computer picks a random choice. 
# Then the program shows ASCII art of each choice and determines the winner.

import random

CHOICES = ["Rock", "Paper", "Scissors"]

# ASCII Art
# Art source: https://www.asciiart.eu/people/body-parts/hand-gestures

art_rock_player = '''
    _______
---'   ____)
      (_____)   PLAYER
      (_____)   CHOOSES
      (____)    ROCK!
---.__(___)
'''

art_paper_player = '''
    _______
---'   ____)____
          ______)   PLAYER
          _______)  CHOOSES
         _______)   PAPER!
---.__________)
'''

art_scissors_player = '''
    _______
---'   ____)____
          ______)   PLAYER
       __________)  CHOOSES
      (____)        SCISSORS!
---.__(___)
'''

art_rock_computer = '''
             _______
            (____   '---
COMPUTER   (_____)
CHOOSES    (_____)
ROCK!       (____)
             (__ )__'---
'''

art_paper_computer = '''
                 _______
            ____(____   '---
COMPUTER   (______
CHOOSES   (_______
PAPER!     (_______
             (__________'---
'''

art_scissors_computer = '''
                 _______
            ____(____   '---
COMPUTER  (______
CHOOSES   (__________
SCISSORS!       (____)
                 (___)__.---
'''

player_art = [
    art_rock_player,
    art_paper_player,
    art_scissors_player
]

computer_art = [
    art_rock_computer,
    art_paper_computer,
    art_scissors_computer
]

# =======

# Ask the user for their choice.
# Returns an integer (0, 1, or 2) to use as an int index of the CHOICES array.
def getChoice():
    while True:

        # Get input from user.
        choiceInput = input(f"\n> ").strip()

        # Validate that the input is a number within the range.
        if choiceInput.isnumeric() and int(choiceInput) >= 1 and int(choiceInput) <= 3:

            # Return the choice as an int index of the CHOICES array.
            return (int(choiceInput) - 1)

        else:
            # If the input is not acceptable, tell the player and keep looping.
            print(f"\nPlease enter a number from 1-3 for your choice.")


# Play a game of Rock, Paper, Scissors.
def playGame():

    # Show menu.
    print("\nLet's play Rock, Paper, Scissors!")
    print("\nEnter your choice:")
    print("  1. Rock")
    print("  2. Paper")
    print("  3. Scissors")

    # Get user's choice and validate it.
    playerChoiceIndex = getChoice()
    playerChoiceStr = CHOICES[playerChoiceIndex]

    # Choose a random choice for the computer to play.
    compChoiceIndex = random.randint(0,2)
    compChoiceStr = CHOICES[compChoiceIndex]

    # Print ASCII art of the hands and choices.
    print(player_art[playerChoiceIndex])
    print(computer_art[compChoiceIndex])

    # See if it's a tie.
    if playerChoiceStr == compChoiceStr:
        print("It's a draw!\n")

    else:
        # Bool flag for player win/loss.
        didPlayerWin = False
        
        # If not a tie, determine the winner.
        if playerChoiceStr == "Rock":
            didPlayerWin = (compChoiceStr == "Scissors")
        elif playerChoiceStr == "Scissors":
            didPlayerWin = (compChoiceStr == "Paper")
        else:
            didPlayerWin = (compChoiceStr == "Rock")

        if didPlayerWin:
            print("You win!\n")
        else:
            print("The computer wins!\n")
        

playGame()


# TEST OUTPUT
# ===========

# Let's play Rock, Paper, Scissors!
#
# Enter your choice:
#   1. Rock
#   2. Paper
#   3. Scissors
#
# > 1
#
#     _______
# ---'   ____)
#       (_____)   PLAYER
#       (_____)   CHOOSES
#       (____)    ROCK!
# ---.__(___)
#
#
#                  _______
#             ____(____   '---
# COMPUTER  (______
# CHOOSES   (__________
# SCISSORS!       (____)
#                  (___)__.---
#
# You win!