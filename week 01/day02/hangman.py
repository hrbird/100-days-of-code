# A classic game in which the computer chooses a random word, and the player guesses which letters are in it. 
# If they guess all the letters in the word without too many mistakes, they win. 
# If they make too many wrong guesses, they hang.

import random
from hangman_art import HANGMAN_ART
from hangman_art import HAPPYMAN_ART
from hangman_art import LOGO_ART
from hangman_words import WORD_LIST

MAX_WRONG_GUESSES = 6

# Ask the user for their next guessed letter.
# Returns a single character.
def getLetter():
    while True:

        # Get input from user.
        # Strip it of whitespace and grab the first character.
        print("\nGuess a letter:")
        guess = input(f"> ").strip()

        if len(guess) == 0:
           print(f"Oops, you did not enter a letter. Please guess again...")

        elif guess[0].isalpha():
            return guess[0].lower()

        else:
            # If the input is not acceptable, tell the player and keep looping.
            print(f"Oops, {guess} is not a letter. Please guess again...")

# Gets either "Y" or "N" from the user and validates the answer.
# Returns either True for Y or False for N.
def getYN():
    while True:

        # Get input from user.
        # Strip it of whitespace and grab the first character.
        ans = input(f"\n> ").strip()

        if len(ans) == 0:
           print(f"Oops, you did not enter a letter. Please enter Y or N...")

        elif ans[0].upper() == "Y":
            return True

        elif ans[0].upper() == "N":
            return False

        else:
            # If the input is not acceptable, tell the player and keep looping.
            print(f"Oops, I can't accept {ans}. Please enter Y or N...")

def playGame():

    print(LOGO_ART)

    # Pick a random word.
    chosen_word = random.choice(WORD_LIST)

    # Initialize variables.
    keepPlaying = True
    num_wrong_guesses = 0
    letters_guessed = []
    areAllLettersGuessed = False

    # Start the game loop.
    while keepPlaying:

        # Print the word with blanks for unguessed letters.
        # If a letter has been guessed, show it.
        blank_word = ""
        for i in range(len(chosen_word)):
            cur_letter = chosen_word[i]
            if letters_guessed.count(cur_letter) > 0:
                blank_word += cur_letter
            else:
                blank_word += "_"

        print(f"\nWord: {blank_word}")

        # Show the hangman.
        print(HANGMAN_ART[num_wrong_guesses])

        # Show all the letters the player has guessed, both correct and incorrect.
        print(f"Letters you have guessed: {' '.join(letters_guessed)}")
        
        # Get a letter from the user.
        letter = getLetter()

        # Check if the letter has already been guessed.
        if letters_guessed.count(letter) > 0:
            print(f"Oops, you already guessed {letter}!\nGuess another letter...\n")

        else:
            # Add the letter to the guessed letters.
            letters_guessed.append(letter)
            
            # If the letter is not in the chosen word, add another part to the hanged man.
            if chosen_word.count(letter) == 0:
                num_wrong_guesses += 1

        # Check if the player won the game.
        # Set a bool flag to true to see if all the blanks are filled.
        areAllLettersGuessed = True
        for i in range(len(chosen_word)):
            cur_letter = chosen_word[i]
            if letters_guessed.count(cur_letter) == 0:
                areAllLettersGuessed = False
        
        # If the player wins, congratulate them.
        if areAllLettersGuessed:
            print("\n-----------------------------------------------\n")
            print(f"Congratulations! The word was '{chosen_word}'!\n\n")
            print(HAPPYMAN_ART)
            keepPlaying = False

        # Check if the player lost the game (the hangman is done).
        if num_wrong_guesses >= MAX_WRONG_GUESSES:
            
            # If the player loses, tell them what the word was.
            print("\n-----------------------------------------------\n")
            print(f"Sorry, the word was '{chosen_word}'.\n")
            print("You lose...")
            print(HANGMAN_ART[MAX_WRONG_GUESSES])
            keepPlaying = False

        print("-----------------------------------------------\n")

        
# Main program loop.
quit_program = False
while not quit_program:

    playGame()

    print(f"\nWould you like to play again? [Y/N]")

    if getYN():
        print("All right! Let's play again...")
    else:
        print("Thanks for playing, and goodbye!\n")
        quit_program = True
