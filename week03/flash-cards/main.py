# A program that shows flashcards to study the most common words 
# in a different language (in this case, Esperanto). 
# 
# It first shows the front of a flashcard with a random word 
# in the language in the language you are studying. 
# After 3 seconds, it flips to show the back of the card, 
# with the translation of the word in English. 
# 
# The user can click the green checkmark button if they knew the answer, 
# or the red X button if they didn't know it.
#
# The words that the user didn't know or didn't see yet are saved 
# to a new file called "words_to_learn.csv". The next time the user 
# runs this program, this file will be used for the flashcards, 
# so the user will only be tested on unknown/unfamiliar words.

from os.path import dirname, join
import random
import tkinter as tk
import pandas

#=========================================
# CONSTANTS
#=========================================

# Color constants
BACKGROUND_COLOR = "#B1DDC6"
TEXT_FRONT_COLOR = "black"
TEXT_BACK_COLOR = "white"

# Canvas size constants
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 530

# The number of pixels to pad each widget
PAD_X = 10
PAD_Y = 10

# Font constants
FONT_LANG_LABEL = ("Arial", 40, "italic")
FONT_WORD_LABEL = ("Arial", 60, "bold")

# X and Y positions for items on the canvas
FLASHCARD_IMG_X = CANVAS_WIDTH/2
FLASHCARD_IMG_Y = CANVAS_HEIGHT/2
LANG_LABEL_X = 400
LANG_LABEL_Y = 150
WORD_LABEL_X = 400
WORD_LABEL_Y = 260

# Image file paths
CURRENT_DIR = dirname(__file__)
FLASHCARD_FRONT_IMG_FILE_PATH = join(CURRENT_DIR, "./images/card_front.png")
FLASHCARD_BACK_IMG_FILE_PATH = join(CURRENT_DIR, "./images/card_back.png")
CORRECT_IMG_FILE_PATH = join(CURRENT_DIR, "./images/right.png")
WRONG_IMG_FILE_PATH = join(CURRENT_DIR, "./images/wrong.png")

# Text constants
LANG_FRONT = "Esperanto"
LANG_BACK = "English"

# Time constants
FLIP_TIME = 3000    # Flip the card after 3 seconds

# Language dictionary file path
# The data file is a CSV, but the data is separated by semicolons, 
# not commas, since the English translations include many commas.
DATA_FILE_PATH = join(CURRENT_DIR, "./data/esperanto.csv")

# This file will store the words that the user didn't know or didn't get tested on yet.
WORDS_TO_LEARN_FILE_PATH = join(CURRENT_DIR, "./data/words_to_learn.csv")

WORDS = {}

# First, try to open words_to_learn.csv, if it has been created.
try:
    WORDS = pandas.read_csv(WORDS_TO_LEARN_FILE_PATH, sep=';').to_dict(orient="records")
except:
    # Else, open the main data file with the full list of words.
    try:
        WORDS = pandas.read_csv(DATA_FILE_PATH, sep=';').to_dict(orient="records")
    except FileNotFoundError:
        print(f"\nError: Could not find data file at {DATA_FILE_PATH}.\n")
    else:
        print(f"\nGetting word data from file: {DATA_FILE_PATH}")
else:
    print(f"\nGetting word data from file: {WORDS_TO_LEARN_FILE_PATH}")

# Current random word and its translation.
# Making these global variables because it's tricky trying to send parameters 
# to repeating window.after() calls.
cur_word = {}

#=========================================
# DATA FUNCTIONS
#=========================================

def get_random_word():
    """Get a new random word from WORDS and show it on the flashcard."""
    global cur_word

    try:
        cur_word = random.choice(list(WORDS))

        print(f"\nNew word: {cur_word[LANG_FRONT]}, meaning: {cur_word[LANG_BACK]}")

        show_word()

    except IndexError:
        print(f"\nIndex Error: Could not get a new random {LANG_FRONT} word.")
        cur_word = {}

    except KeyError:
        print(f"\nKey Error: Could not get a new random {LANG_FRONT} word.")
        cur_word = {}

def remove_word():
    """If a user gets a word right, remove it from the WORDS dictionary."""
    WORDS.remove(cur_word)

    # Update the words_to_learn.csv file.
    try:
        pandas.DataFrame(WORDS).to_csv(WORDS_TO_LEARN_FILE_PATH, sep=";", index=False)
    except:
        print(f"Error: Could not write data to file: {WORDS_TO_LEARN_FILE_PATH}")

    # Go to the next card.
    get_random_word()


#=========================================
# UI FUNCTIONS
#=========================================

def show_word():
    """Show the current word and language on the front of the flashcard."""
    global cur_word, flip_timer

    # Cancel the old flip timer, if the user clicked to the next card before 
    # the previous one flipped.
    window.after_cancel(flip_timer)

    # Show the word to learn on the card.
    canvas.itemconfig(flashcard_canvas_img, image=flashcard_front_img)
    canvas.itemconfig(lang_text, text=LANG_FRONT, fill=TEXT_FRONT_COLOR)
    canvas.itemconfig(word_text, text=cur_word[LANG_FRONT], fill=TEXT_FRONT_COLOR)

    # Set a timer to flip the card after a short delay.
    flip_timer = window.after(FLIP_TIME, func=flip_card)


def flip_card():
    """After a short delay, flip the card and show the English translation."""
    global cur_word

    canvas.itemconfig(flashcard_canvas_img, image=flashcard_back_img)
    canvas.itemconfig(lang_text, text=LANG_BACK, fill=TEXT_BACK_COLOR)
    canvas.itemconfig(word_text, text=cur_word[LANG_BACK], fill=TEXT_BACK_COLOR)

#=========================================
# SET UP UI AND WIDGETS
#=========================================

# Create a window.
window = tk.Tk()
window.title("Flash Cards")
window.minsize(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Set a timer to flip the card after a short delay.
flip_timer = window.after(FLIP_TIME, func=flip_card)

# Get the flashcard images.
flashcard_front_img = tk.PhotoImage(file=FLASHCARD_FRONT_IMG_FILE_PATH)
flashcard_back_img = tk.PhotoImage(file=FLASHCARD_BACK_IMG_FILE_PATH)

# Add the flashcard image to the center of the window.
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_canvas_img = canvas.create_image(FLASHCARD_IMG_X, FLASHCARD_IMG_Y, image=flashcard_front_img)

# Write the current language over the card.
lang_text = canvas.create_text(LANG_LABEL_X, LANG_LABEL_Y, text="", fill=TEXT_FRONT_COLOR, font=FONT_LANG_LABEL)

# Write the current word over the card.
word_text = canvas.create_text(WORD_LABEL_X, WORD_LABEL_Y, text="", fill=TEXT_FRONT_COLOR, font=FONT_WORD_LABEL)

# Add the canvas to the grid.
canvas.grid(row=0, column=0, columnspan=2)

# Create the green checkmark button.
correct_img = tk.PhotoImage(file=CORRECT_IMG_FILE_PATH)
correct_button = tk.Button(image=correct_img, highlightthickness=0, command=remove_word)
correct_button.grid(row=1, column=0)

# Create the red X button.
wrong_img = tk.PhotoImage(file=WRONG_IMG_FILE_PATH)
wrong_button = tk.Button(image=wrong_img, highlightthickness=0, command=get_random_word)
wrong_button.grid(row=1, column=1)

#=========================================
# MAIN LOOP
#=========================================

get_random_word()

# Keep the window and code running.
window.mainloop()
