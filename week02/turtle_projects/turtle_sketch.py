# Lets the user draw an image on the screen by pressing the WASD keys, 
# like an etch-a-sketch.
from turtle import Turtle, Screen
import random

DIRECTIONS = [0, 90, 180, 270]

# My favorite rainbow color scheme.
COLORS = [
    "firebrick", "orangered", "gold1", "darkolivegreen1", "seagreen1",
    "skyblue1", "royalblue1", "slateblue3", "deeppink4"
]

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.pensize(3)

screen = Screen()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def turn_right():
    timmy.setheading(timmy.heading() - 10)

def turn_left():
    timmy.setheading(timmy.heading() + 10)

def clear_screen():
    timmy.home()
    timmy.clear()

# Add event listeners.
screen.listen()

# If the user presses certain keys, let them control the pen.
screen.onkeypress(key="w", fun=move_forward)    # W = walk forward
screen.onkeypress(key="s", fun=move_backward)   # S = walk backward
screen.onkeypress(key="a", fun=turn_left)       # A = turn left (counter-clockwise)
screen.onkeypress(key="d", fun=turn_right)      # D = turn right (clockwise)
screen.onkeypress(key="c", fun=clear_screen)      # C = clear the screen

# Quit if user clicks on the screen.
screen.exitonclick()

