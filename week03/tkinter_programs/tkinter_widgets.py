# Demonstrates several types of tkinter widgets you can create,
# including labels, buttons, single-line and multi-line text entry boxes, 
# spinboxes, scales, checkbuttons, radiobuttons, and listboxes.
# Also demonstrates how to bind functions to widgets and get
# each kind of widget's current value.

import tkinter as tk

# Create a new window.
window = tk.Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#=========================================
# BUTTON
#=========================================

# When the "Click Me" button is clicked, the label below it changes.
def button_action():
    button_label.config(text="You clicked the button!")

# Button that calls button_action() when pressed.
button = tk.Button(text="Click Me", command=button_action)
button.pack()

# Create a label.
button_label = tk.Label(text="This is a label", fg="blue")
button_label.pack()

#=========================================
# TEXT ENTRY BOXES
#=========================================

# Create a single-line text entry box.
entry = tk.Entry(width=50)
entry.insert(tk.END, string="This is a single-line text entry box.")
entry.pack()

# Create a multi-line text entry box.
text = tk.Text(height=5, width=30)
text.focus() # Put the cursor in the box
text.insert(tk.END, "This is a multi-line text\nentry box with placeholder\ntext.")
text.pack()

#=========================================
# SPINBOX
#=========================================

# Create a label for the spinbox.
spinbox_label = tk.Label(text="Spinbox:", fg="blue")
spinbox_label.pack()

# Create a spinbox.
spinbox = tk.Spinbox(from_=0, to=10, width=5)
spinbox.pack()

#=========================================
# SCALE
#=========================================

# Create a label for the scale.
scale_label = tk.Label(text="Scale:", fg="blue")
scale_label.pack()

# Create a scale.
scale = tk.Scale(from_=0, to=5)
scale.pack()

#=========================================
# CHECKBUTTON
#=========================================

# Create a label for the checkbutton.
checkbutton_label = tk.Label(text="Checkbutton:", fg="blue")
checkbutton_label.pack()

# Create a checkbutton.
# When it is checked or unchecked, store its current value in the checked_state variable.
# (0 = off/unchecked, 1 = on/checked)
checked_state = tk.IntVar()
checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state)
checkbutton.pack()

#=========================================
# RADIOBUTTON
#=========================================

# Create a label for the radiobutton.
radiobutton_label = tk.Label(text="Radiobutton:", fg="blue")
radiobutton_label.pack()

# Create a radiobutton.
# When one of the options is selected, store that option's value in the radio_state variable.
radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state)
radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state)
radiobutton1.pack()
radiobutton2.pack()

#=========================================
# LISTBOX
#=========================================

# Create a label for the listbox.
listbox_label = tk.Label(text="Listbox:", fg="blue")
listbox_label.pack()

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
listbox.pack()


#=========================================
# GETTING VALUES
#=========================================

# When the "Get Values" button is clicked, 
# the value in each widget is printed to the console.
def values_button_action():
    print("\nVALUES:\n")

    print(f"The single-line text entry box contains:\n{entry.get()}")
    print(f"The multi-line text entry box contains:\n{text.get('1.0', tk.END)}")

    print(f"The spinbox's value is: {spinbox.get()}")
    print(f"The scale's value is: {scale.get()}")

    print(f"The checkbutton's state is: {checked_state.get()}")
    print(f"The radiobutton's state is: {radio_state.get()}")

    if listbox.curselection():
        print(f"The listbox's current selection is: {listbox.get(listbox.curselection())}")
    else:
        print(f"The listbox's current selection is: No Value")



# Button that calls button_action() when pressed.
values_button = tk.Button(text="Get Values", command=values_button_action)
values_button.pack()


#=========================================
# MAIN LOOP
#=========================================

# Keep the window and code running.
window.mainloop()