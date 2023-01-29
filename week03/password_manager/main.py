# Program that stores usernames and passwords for various sites.
# It can also generate random secure passwords.


from os.path import dirname, join
import random
import tkinter as tk


#=========================================
# CONSTANTS
#=========================================


# Color constants
PINK = "#e2979c"
RED = "#cc4c35"
GREEN = "#9ebd75"
YELLOW = "#ffdf91"

# Font constants
FONT_NAME = "Courier"

# Canvas size constants
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 200

# The number of pixels to pad each widget
PAD_X = 10
PAD_Y = 10

# MyPass image file path constants
CURRENT_DIR = dirname(__file__)
MYPASS_IMG_FILE_PATH = join(CURRENT_DIR, "./logo.png")

# X and Y positions for items on the canvas
MYPASS_IMG_X = CANVAS_WIDTH/2
MYPASS_IMG_Y = CANVAS_HEIGHT/2

#=========================================
# PASSWORD GENERATOR
#=========================================

#=========================================
# SAVE PASSWORD
#=========================================

#=========================================
# SET UP UI AND WIDGETS
#=========================================

# Create a window.
window = tk.Tk()
window.title("Pomodoro Timer")
window.minsize(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
window.config(padx=20, pady=20, bg="white")

# Get the MyPass image.
mypass_img = tk.PhotoImage(file=MYPASS_IMG_FILE_PATH)

# Add the MyPass image in the center of the window.
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white", highlightthickness=0)
canvas.create_image(MYPASS_IMG_X, MYPASS_IMG_Y, image=mypass_img)
canvas.grid(row=1, column=1)

#=========================================
# MAIN LOOP
#=========================================

# Keep the window and code running.
window.mainloop()
