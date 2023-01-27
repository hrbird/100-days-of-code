# Program that converts miles to kilometers.
# When the user enters a float number of miles into 
# a text entry box and clicks the Calculate button, 
# the equivalent number of kilometers is written in the km label.
# Uses the tkinter library to create a GUI.

import tkinter as tk

# The number of pixels to pad each widget.
PAD_X = 10
PAD_Y = 10

# Light blue button background color.
BUTTON_COLOR = "#add8e6"

# Create a new window.
window = tk.Tk()
window.title("Miles - Kilometers Converter")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

#=========================================
# MILES
#=========================================

# Text entry box for the user to enter the number of miles.
miles_entry = tk.Entry(width=10, bg="white")
miles_entry.focus()
miles_entry.grid(row=0, column=0, padx=PAD_X, pady=PAD_Y, ipadx=3, ipady=3)

# Create a "miles" label after the text entry box.
miles_label = tk.Label(text="miles")
miles_label.grid(row=0, column=1)

#=========================================
# IS EQUAL TO
#=========================================

# Create an "is equal to" label.
equal_to_label = tk.Label(text="is equal to")
equal_to_label.grid(row=1, column=0, columnspan=2)

#=========================================
# KILOMETERS
#=========================================

# Text entry box for the user to enter the number of km.
km_num_label = tk.Label(width=10, bg="white", justify="left")
km_num_label.grid(row=2, column=0, padx=PAD_X, pady=PAD_Y, ipadx=3, ipady=3)

# Create a "km" label after the text entry box.
km_label = tk.Label(text="km")
km_label.grid(row=2, column=1)

#=========================================
# CALCULATE BUTTON
#=========================================

# When the "Calculate" button is clicked, convert from either miles to km or km to miles.
def button_action():
    
    # Get the values inside both text entry boxes.
    miles_val = miles_entry.get()

    if len(miles_val) > 0:
        miles_float = float(miles_val)

        num_km = miles_float * 1.60934

        km_num_label.config(text=f"{num_km:.2f}")
    
        print(f"You entered {miles_float} miles.")

# Button that calls button_action() when pressed.
calculate_button = tk.Button(text="Calculate", command=button_action, bg=BUTTON_COLOR)
calculate_button.grid(row=3, column=0, columnspan=2, ipadx=3, ipady=3, padx=PAD_X, pady=PAD_Y)

#=========================================
# MAIN LOOP
#=========================================

# Keep the window and code running.
window.mainloop()