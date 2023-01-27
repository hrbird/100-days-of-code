# Program that shows a Pomodoro Timer.

# (The pomodoro method is helpful for working on long projects.
# It breaks up the day into 25-minute periods of work, 
# followed by a short 5-minute break.)

# This program uses the tkinter library to create a GUI.
# It keeps track of the time spent on the current pomodoro/break,
# as well as how many total pomodoros have been completed.

from os.path import dirname, join
import tkinter as tk

#=========================================
# CONSTANTS
#=========================================

# Color constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#FFD56F"

# Font constants
FONT_NAME = "Courier"

# Canvas size constants
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 224

# The number of pixels to pad each widget
PAD_X = 10
PAD_Y = 10

# Time constants
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Tomato image file path constants
CURRENT_DIR = dirname(__file__)
TOMATO_IMG_FILE_PATH = join(CURRENT_DIR, "./tomato.png")

# X and Y positions for items on the canvas
TOMATO_IMG_X = CANVAS_WIDTH/2
TOMATO_IMG_Y = CANVAS_HEIGHT/2
TIME_X = CANVAS_WIDTH/2
TIME_Y = CANVAS_HEIGHT/2 + 15

#=========================================
# TIMER RESET
#=========================================

#=========================================
# COUNTDOWN MECHANISM 
#=========================================

#=========================================
# SET UP UI AND WIDGETS
#=========================================

# Create a window.
window = tk.Tk()
window.title("Pomodoro Timer")
window.minsize(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
window.config(padx=100, pady=50, bg=YELLOW)

# Get the tomato image.
tomato_img = tk.PhotoImage(file=TOMATO_IMG_FILE_PATH)

# Add the tomato image in the center of the window.
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=YELLOW, highlightthickness=0)
canvas.create_image(TOMATO_IMG_X, TOMATO_IMG_Y, image=tomato_img)

# 
canvas.create_text(TIME_X, TIME_Y, text="12:15", fill="white", font=(FONT_NAME, 24, "bold"))

canvas.pack()

#=========================================
# MAIN LOOP
#=========================================

# Keep the window and code running.
window.mainloop()