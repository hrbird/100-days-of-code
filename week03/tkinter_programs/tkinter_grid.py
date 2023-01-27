# Demonstrates several types of tkinter widgets you can create,
# including labels, buttons, single-line and multi-line text entry boxes, 
# spinboxes, scales, checkbuttons, radiobuttons, and listboxes.
# Also demonstrates how to bind functions to widgets and get
# each kind of widget's current value.

import tkinter as tk

# The number of pixels to pad each widget.
PAD_X = 5
PAD_Y = 5

# Light blue button background color.
BUTTON_COLOR = "#add8e6"

# Create a new window.
window = tk.Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

#=========================================
# BUTTON
#=========================================

# Create a label.
button_label = tk.Label(text="Button:", fg="blue")
button_label.grid(row=0, column=0)

# When the "Click Me" button is clicked, print to console.
def button_action():
    print("You clicked the button!")

# Button that calls button_action() when pressed.
button = tk.Button(text="Click Me", command=button_action, bg=BUTTON_COLOR)
button.grid(row=0, column=1, ipadx=3, ipady=3, padx=PAD_X, pady=PAD_Y)

#=========================================
# SPINBOX
#=========================================

# Create a label for the spinbox.
spinbox_label = tk.Label(text="Spinbox:", fg="blue")
spinbox_label.grid(row=1, column=0)

# Create a spinbox.
spinbox = tk.Spinbox(from_=0, to=10, width=5)
spinbox.grid(row=1, column=1, padx=PAD_X, pady=PAD_Y)

#=========================================
# SCALE
#=========================================

# Create a label for the scale.
scale_label = tk.Label(text="Scale:", fg="blue")
scale_label.grid(row=2, column=0)

# Create a scale.
scale = tk.Scale(from_=0, to=5)
scale.grid(row=2, column=1, padx=PAD_X, pady=PAD_Y)

#=========================================
# CHECKBUTTON
#=========================================

# Create a label for the checkbutton.
checkbutton_label = tk.Label(text="Checkbutton:", fg="blue")
checkbutton_label.grid(row=3, column=0)

# Create a checkbutton.
# When it is checked or unchecked, store its current value in the checked_state variable.
# (0 = off/unchecked, 1 = on/checked)
checked_state = tk.IntVar()
checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state)
checkbutton.grid(row=3, column=1, padx=PAD_X, pady=PAD_Y)

#=========================================
# RADIOBUTTON
#=========================================

# Create a label for the radiobutton.
radiobutton_label = tk.Label(text="Radiobutton:", fg="blue")
radiobutton_label.grid(row=4, column=0)

# Create a radiobutton.
# When one of the options is selected, store that option's value in the radio_state variable.
radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state)
radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state)
radiobutton1.grid(row=4, column=1)
radiobutton2.grid(row=5, column=1)

#=========================================
# LISTBOX
#=========================================

# Create a label for the listbox.
listbox_label = tk.Label(text="Listbox:", fg="blue")
listbox_label.grid(row=6, column=0)

# Function for the listbox prints the current selection.
def listbox_action(event):
    print(f"\nYou selected: {listbox.get(listbox.curselection())}")

# Create a listbox and populate it with types of fruit.
listbox = tk.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

# Listboxes don't have the standard command= parameter to tie it to a function.
# Therefore, we need to bind the function to the listbox.
listbox.bind("<<ListboxSelect>>", listbox_action)
listbox.grid(row=6, column=1, padx=PAD_X, pady=PAD_Y)

#=========================================
# SINGLE-LINE TEXT ENTRY BOX
#=========================================

# Create a label for the text entry box.
entry_label = tk.Label(text="Single-Line Entry Box:", fg="blue")
entry_label.grid(row=7, column=0)

# Create a single-line text entry box.
entry = tk.Entry(width=30)
entry.insert(tk.END, string="Hello, world!")
entry.grid(row=7, column=1, padx=PAD_X, pady=PAD_Y)

#=========================================
# MULTI-LINE TEXT ENTRY BOX
#=========================================

# Create a label for the text entry box.
text_label = tk.Label(text="Multi-Line Entry Box:", fg="blue")
text_label.grid(row=8, column=0)

# Create a multi-line text entry box.
text = tk.Text(height=5, width=30)
text.focus() # Put the cursor in the box
text.insert(tk.END, "This is a multi-line text\nentry box with placeholder\ntext.")
text.grid(row=8, column=1, padx=PAD_X, pady=PAD_Y)

#=========================================
# GETTING VALUES
#=========================================

# When the "Get Values" button is clicked, 
# the value in each widget is printed to the console.
def values_button_action():
    print("\nVALUES:\n")

    print(f"The spinbox's value is: {spinbox.get()}")
    print(f"The scale's value is: {scale.get()}")

    print(f"The checkbutton's state is: {checked_state.get()}")
    print(f"The radiobutton's state is: {radio_state.get()}")

    if listbox.curselection():
        print(f"The listbox's current selection is: {listbox.get(listbox.curselection())}")
    else:
        print(f"The listbox's current selection is: No Value")

    print(f"\nThe single-line text entry box contains:\n{entry.get()}")
    print(f"\nThe multi-line text entry box contains:\n{text.get('1.0', tk.END)}")

# Button that calls button_action() when pressed.
values_button = tk.Button(text="Get Values", command=values_button_action, bg=BUTTON_COLOR)
values_button.grid(row=9, column=1, ipadx=3, ipady=3, padx=PAD_X*2, pady=PAD_Y*2)

#=========================================
# MAIN LOOP
#=========================================

# Keep the window and code running.
window.mainloop()