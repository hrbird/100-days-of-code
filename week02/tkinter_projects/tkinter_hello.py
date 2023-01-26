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

# Create a button.
button = tkinter.Button(
    text="Click me!",
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