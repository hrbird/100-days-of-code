# Learning and playing with the Turtle graphics library.
# This program draws a rainbow spirograph image using Turtle.
# Tutorial: https://www.geeksforgeeks.org/print-a-spirograph-using-turtle-in-python/

import turtle
import math

# My favorite rainbow color scheme.
COLORS = [
    "firebrick", "orangered", "gold1", "darkolivegreen1", "seagreen1",
    "skyblue1", "royalblue1", "slateblue3", "deeppink4"
]

# How large to make the circles.
CIRCLE_RADIUS = 150

# The change in angle between each circle.
CIRCLE_ANGLE_CHANGE = 10

# The number of times to repeat all the colors so the entire spirograph is drawn.
# (If I have 9 colors, I should loop through them all 4 times at 10 degrees change,
# because 9 * 4 * 10 = 360 degrees.)
NUM_REPEATS = math.ceil(360 / CIRCLE_ANGLE_CHANGE / len(COLORS))

# Set the background color to black and hide the pointer.
turtle.bgcolor("black")
turtle.hideturtle()

# Set the pen size to 2 and pen speed to 10.
turtle.pensize(2)
turtle.speed(10)

# Draw the spirograph.
for i in range(NUM_REPEATS):

    # Loop through each color in the list.
    for col in COLORS:

        # Switch to that color and draw a circle.
        turtle.color(col)
        turtle.circle(CIRCLE_RADIUS)

        # Turn a set angle to the left to draw another circle.
        turtle.left(CIRCLE_ANGLE_CHANGE)


turtle.Screen().exitonclick()
