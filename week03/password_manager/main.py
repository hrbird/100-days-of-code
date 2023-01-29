# Program that stores usernames and passwords for various sites. 

# It shows a form for the user to enter a new set of account information: 
# the name of the website, the email/username, and the password. 
# There is a button to generate a random secure password, if needed. 

# If the user clicks the Add button at the bottom, this account information 
# is written to a text file.

from os.path import dirname, join
import random
import tkinter as tk

#=========================================
# CONSTANTS
#=========================================

# Color constants
RED = "#cc4c35"
GREEN = "#9ebd75"

# Font constants
FONT_NAME = "Arial"
FONT_SIZE_LABEL = 10

# Canvas size constants
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 200

# The number of pixels to pad each widget
PAD_X = 10
PAD_Y = 10
IPAD_X = 3
IPAD_Y = 3

# MyPass image file path constants
CURRENT_DIR = dirname(__file__)
MYPASS_IMG_FILE_PATH = join(CURRENT_DIR, "./logo.png")

# Account data text file path
DATA_TXT_FILE_PATH = join(CURRENT_DIR, "./data.txt")

# X and Y positions for items on the canvas
MYPASS_IMG_X = CANVAS_WIDTH/2
MYPASS_IMG_Y = CANVAS_HEIGHT/2

#=========================================
# PASSWORD GENERATOR
#=========================================

def generate_password():
    """Generates a random password."""
    pass

#=========================================
# SAVE PASSWORD
#=========================================

def add_info():
    """Adds the information entered in the form to a text file."""

    # Get the data from the entry widgets.
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Format the data into a string.
    data_str = f"{website}, {username}, {password}"

    # Open the data txt file and write the string to it.
    with open(DATA_TXT_FILE_PATH, "a") as f:
        f.write(data_str)

    # Clear the text entry forms.
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    # Put the cursor back in website_entry.
    website_entry.focus()

#=========================================
# SET UP UI AND WIDGETS
#=========================================

# Create a window.
window = tk.Tk()
window.title("Pomodoro Timer")
window.minsize(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
window.config(padx=50, pady=50, bg="white")

# Get the MyPass image.
mypass_img = tk.PhotoImage(file=MYPASS_IMG_FILE_PATH)

# Add the MyPass image in the center of the window.
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white", highlightthickness=0)
canvas.create_image(MYPASS_IMG_X, MYPASS_IMG_Y, image=mypass_img)
canvas.grid(row=0, column=1)

# Create a "Website" label.
website_label = tk.Label(text="Website:", fg="black", bg="white")
website_label.grid(row=1, column=0)

# Create a website entry box.
website_entry = tk.Entry(width=50)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

# Create an "Email/Username" label.
username_label = tk.Label(text="Email/Username:", fg="black", bg="white")
username_label.grid(row=2, column=0)

# Create a username entry box.
username_entry = tk.Entry(width=50)
username_entry.grid(row=2, column=1, columnspan=2)

# Create a "Password" label.
password_label = tk.Label(text="Password:", fg="black", bg="white")
password_label.grid(row=3, column=0)

# Create a password entry box.
password_entry = tk.Entry(width=32)
password_entry.grid(row=3, column=1)

# Create a "Generate Password" button that calls generate_password() when pressed.
generate_password_button = tk.Button(text="Generate Password", command=generate_password, bg="white")
generate_password_button.grid(row=3, column=2) 

# Create an "Add" button that calls add_info() when pressed.
add_button = tk.Button(text="Add", command=add_info, bg=GREEN, width=43)
add_button.grid(row=4, column=1, columnspan=2) 


#=========================================
# MAIN LOOP
#=========================================

# Keep the window and code running.
window.mainloop()
