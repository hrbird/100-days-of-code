# Program that shows a Pomodoro Timer.

# (The pomodoro method is helpful for working on long projects.
# It breaks up the day into 25-minute periods of work, 
# followed by a short 5-minute break.)

# This program uses the tkinter library to create a GUI.
# It keeps track of the time spent on the current pomodoro/break,
# as well as how many total pomodoros have been completed.

import tkinter as tk

#=========================================
# CONSTANTS
#=========================================

# Color constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# Font constants
FONT_NAME = "Courier"

# The number of pixels to pad each widget
PAD_X = 10
PAD_Y = 10

# Time constants
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

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
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

#=========================================
# MAIN LOOP
#=========================================

# Keep the window and code running.
window.mainloop()