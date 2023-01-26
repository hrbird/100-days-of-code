# Use the Tkinter library to create a GUI application.

import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=400)

# Create a label with blue Arial font.
my_label = tkinter.Label(
    text="Hello, world.", 
    font=("Arial", 16, "bold"), 
    fg="blue"
)

# Add the label to the window.
my_label.pack(expand=5)

# This function will be called when the button is clicked.
def button_clicked():
    print("I got clicked!")

    # Change the label to say that user clicked the button.
    my_label.config(text="You clicked the button!")

# Create a button.
button = tkinter.Button(
    text="Click me!",
    command=button_clicked,
    font=("Arial", 16, "bold"), 
    width=15,
    height=3,
    bg="blue",
    fg="white",
)

# Add the button to the bottom side of the window.
button.pack(side="bottom")

# Keep the program running until the user exits.
window.mainloop()