# Program that shows flashcards to study the most common words in Esperanto.

# It shows 

from os.path import dirname, join
import random
import tkinter as tk

#=========================================
# CONSTANTS
#=========================================

# Color constants
BACKGROUND_COLOR = "#B1DDC6"

# data = read_csv(csv_path, sep=';')

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
word_front = "bela"
word_back = "lovely, beautiful"

#=========================================
# SET UP UI AND WIDGETS
#=========================================

# Create a window.
window = tk.Tk()
window.title("Flash Cards")
window.minsize(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Get the flashcard images.
flashcard_front_img = tk.PhotoImage(file=FLASHCARD_FRONT_IMG_FILE_PATH)
flashcard_back_img = tk.PhotoImage(file=FLASHCARD_BACK_IMG_FILE_PATH)

# Add the flashcard image to the center of the window.
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(FLASHCARD_IMG_X, FLASHCARD_IMG_Y, image=flashcard_front_img)
canvas.grid(row=0, column=0, columnspan=2)

# Write the current language over the card.
lang_text = canvas.create_text(LANG_LABEL_X, LANG_LABEL_Y, text=LANG_FRONT, fill="black", font=FONT_LANG_LABEL)

# Write the current word over the card.
lang_text = canvas.create_text(WORD_LABEL_X, WORD_LABEL_Y, text=word_front, fill="black", font=FONT_WORD_LABEL)

# Add the canvas to the grid.
canvas.grid(row=0, column=0, columnspan=2)


#=========================================
# MAIN LOOP
#=========================================

# Keep the window and code running.
window.mainloop()
