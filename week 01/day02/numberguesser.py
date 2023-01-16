# A game that asks the player to guess a secret random number between 1 and 1000 within 10 guesses. 
# Incorporates a basic game loop and input validation.

import random

# Constants
MAX_GUESSES = 10
LOW_RANGE = 1
HIGH_RANGE = 1000

# Variables
keepPlaying = True

print("\nWelcome to Number Guesser!")

# Ask the user if they would like to play another game.
# Returns True for new game, or False to quit program.
def getNewGame():
    
    print(f"\nWould you like to play again? [Y/N]")

    while True:

        # Get input from the user and convert it to uppercase.
        replayInput = input(f"> ").strip().upper()

        # If the player entered anything that starts with "Y", keep playing.
        if replayInput[0] == "Y":
            
            print("\n---------------------")
            return True

        elif replayInput[0] == "N":
            # If the player entered "N", quit.
            print("\nThanks for playing, and goodbye!")
            return False

        else:
            print(f"Oops, {replayInput} is not an acceptable answer.")
            print("Please enter either Y or N.")

# Ask the user for their next guess.
# Parameter guessCount = the guess # of the current game.
# Returns an integer.
def getGuess(guessCount):
    while True:

        # Get input from user.
        guessInput = input(f"\nGuess #{guessCount}: ").strip()

        # Validate that the input is a number within the range.
        if guessInput.isnumeric() and int(guessInput) >= LOW_RANGE and int(guessInput) <= HIGH_RANGE:

            # If the input is acceptable, save it as the current guess and exit this loop.
            return int(guessInput)

        else:

            # If the input is not acceptable, tell the player and keep looping.
            print(f"Oops, {guessInput} is not a whole number between {LOW_RANGE} and {HIGH_RANGE}.")
            print("Please guess again...")


# Start the game loop.
while keepPlaying:

    # Reset variables.
    guessCount = 1
    curGuess = 0

    # Generate a random int between 1 and 1000.
    randNum = random.randint(LOW_RANGE, HIGH_RANGE)

    # Explain game rules.
    print(f"\n\nI am thinking of a number between {LOW_RANGE} and {HIGH_RANGE}.")
    print(f"You have {MAX_GUESSES} tries to guess my number.\nLet's begin!")

    # Start new game.
    curGameLoop = True
    while curGameLoop:

        if guessCount <= MAX_GUESSES:

            # Get guess from user.
            curGuess = getGuess(guessCount)

            # Check if the guess is correct, too high, or too low.
            if curGuess == randNum:
                print(f"Congratulations! {curGuess} is the number I was thinking of.")
                print(f"You won the game in {guessCount} guesses.")
                
                # End current game.
                curGameLoop = False
            
            elif curGuess < randNum:
                print("Too low!")
                guessCount += 1

            elif curGuess > randNum:
                print("Too high!")
                guessCount += 1

            else:
                print(f"Error: {curGuess} could not be compared.")

        else:
            print("\nSorry, you are out of guesses.")
            print(f"The number I was thinking of was {randNum}.")

            # End current game.
            curGameLoop = False

    # Ask if the user would like to play a new game. If not, quit program.
    if not getNewGame():
        keepPlaying = False
