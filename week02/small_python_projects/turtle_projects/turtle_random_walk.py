# Draws a random path, switching colors and changing speeds randomly.
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
timmy.pensize(10)

color_index = 0
for i in range(30):
    for j in range(10):
        timmy.color(COLORS[color_index])
        
        # Walk in a random direction a random number of steps.
        timmy.setheading(random.choice(DIRECTIONS))
        timmy.forward(random.randint(30, 50))
        timmy.speed(random.randint(5, 10))

    # Switch to the next color.
    color_index += 1
    if color_index >= len(COLORS):
        color_index = 0

screen = Screen()
screen.exitonclick()