# Program that shows a Pomodoro Timer, using tkinter.

# (The pomodoro method is helpful for working on long projects.
# It breaks up the day into 25-minute periods of work, 
# followed by a short 5-minute break.)

# It counts down the time left in the current pomodoro or break.
# It also shows a checkmark at the bottom for each completed pomodoro.

from os.path import dirname, join
import math
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
CANVAS_HEIGHT = 224

# The number of pixels to pad each widget
PAD_X = 10
PAD_Y = 10

# Time constants
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
WORK_SEC = WORK_MIN * 60
SHORT_BREAK_SEC = SHORT_BREAK_MIN * 60
LONG_BREAK_SEC = LONG_BREAK_MIN * 60

# Tomato image file path constants
CURRENT_DIR = dirname(__file__)
TOMATO_IMG_FILE_PATH = join(CURRENT_DIR, "./tomato.png")

# X and Y positions for items on the canvas
TOMATO_IMG_X = CANVAS_WIDTH/2
TOMATO_IMG_Y = CANVAS_HEIGHT/2
TIME_X = CANVAS_WIDTH/2 + 8
TIME_Y = CANVAS_HEIGHT/2 + 20

# Track how many repetitions of pomodoros have been completed.
pomos = 0       # Total number of pomos completed
breaks = 0      # Total number of breaks completed
is_work = True  # True = currently working, False = currently on break
timer = None    # Tracks the window.after() timer variable.

#=========================================
# TIMER MECHANISM
#=========================================

def start_work():
    """Start a new work pomodoro."""
    global pomos

    # Start working.
    header_label.config(text="Work Timer", fg=GREEN)
    count_down(WORK_SEC)

    # After working, increase the number of pomos and take a break.
    pomos += 1

def start_break():
    """Start a new short or long break."""
    global breaks

    # After 3 short breaks, take a long break.
    if breaks > 0 and breaks % 3 == 0:
        header_label.config(text="Long Break", fg=PINK)
        count_down(LONG_BREAK_SEC)
    else:
        header_label.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_SEC)
    
    # After the break, start working again.
    breaks += 1

def update_pomo_checkmarks():
    """Show the current number of completed pomos as checkmarks."""
    global pomos
    check_str = "✔" * pomos
    checkmarks_label.config(text=check_str)

def start_timer():
    """Start the Pomodoro timer.
    Called when the user clicks the Start button.
    Also called whenever the timer countdown reaches zero."""
    global is_work

    update_pomo_checkmarks()

    if is_work:
        start_work()
        is_work = False
    else:
        start_break()
        is_work = True
        

#=========================================
# COUNTDOWN MECHANISM 
#=========================================

def get_count_str(total_seconds):
    """Get a formatted string of the number of minutes and seconds left on the timer, 
    in MM:SS format. Adds leading zeros if they are needed, for example 05:03."""

    # Get the number of minutes and seconds in the current count.
    count_min = math.floor(total_seconds / 60)
    count_sec = total_seconds % 60

    # Format the minutes.
    min_str = str(count_min)
    if count_min < 10:
        min_str = f"0{count_min}"
    
    # Format the seconds.
    sec_str = str(count_sec)
    if count_sec < 10:
        sec_str = f"0{count_sec}"
    
    return f"{min_str}:{sec_str}"

def count_down(count):
    """Update screen every second to show the current time left on the timer."""
    global timer

    # Get the count in MM:SS format.
    count_str = get_count_str(count)

    # Update the screen.
    canvas.itemconfig(timer_text, text=count_str)

    # Continue counting down every second, until you run out of time.
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


#=========================================
# RESET ALL
#=========================================

def reset_all():
    """Resets the timer and all data.
    Called when the user clicks the Reset button."""
    global pomos, breaks, is_work

    window.after_cancel(timer)

    pomos = 0
    breaks = 0
    is_work = True

#=========================================
# SET UP UI AND WIDGETS
#=========================================

# Create a window.
window = tk.Tk()
window.title("Pomodoro Timer")
window.minsize(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
window.config(padx=50, pady=25, bg=YELLOW)

# Create a "Timer" header label.
header_label = tk.Label(text="Work Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36, "bold"))
header_label.grid(row=0, column=0, columnspan=3)

# Get the tomato image.
tomato_img = tk.PhotoImage(file=TOMATO_IMG_FILE_PATH)

# Add the tomato image in the center of the window.
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=YELLOW, highlightthickness=0)
canvas.create_image(TOMATO_IMG_X, TOMATO_IMG_Y, image=tomato_img)

# Write the text of the current time on the timer over the tomato.
timer_text = canvas.create_text(TIME_X, TIME_Y, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

# Create a "Start" button that calls start_timer() when pressed.
start_button = tk.Button(text="Start", command=start_timer, bg="white", font=(FONT_NAME, 12, "bold"))
start_button.grid(row=2, column=0, ipadx=3, ipady=3) 

# Create a "Reset" button that calls reset_action() when pressed.
reset_button = tk.Button(text="Reset", command=reset_all, bg="white", font=(FONT_NAME, 12, "bold"))
reset_button.grid(row=2, column=2, ipadx=3, ipady=3) 

# Create a label to show a checkmark for each completed pomodoro.
checkmarks_label = tk.Label(text=" ", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
checkmarks_label.grid(row=3, column=0, columnspan=3)

#=========================================
# MAIN LOOP
#=========================================

# Keep the window and code running.
window.mainloop()
