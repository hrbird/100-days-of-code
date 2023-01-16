# Learning and playing with the Turtle graphics library.
# This program draws a green spiral spirograph image using Turtle.

import turtle

COLORS = ["green", "darkgreen"]

# Set the background color to black.
turtle.bgcolor("black")

# Increase the speed and hide the pointer.
t = turtle.Turtle()
t.speed(500)
t.hideturtle()

# From the center, draw lines that are 1 degree off from being a right angle.
# The lines start at 1 px long and grow with each iteration to be 1 px longer.
# This forms a spiral shape pattern.
# Also, alternate each line between green and dark-green to emphasize the spiral.
for i in range(400):
    t.forward(i + 1)
    t.right(89)
    t.pencolor(COLORS[i % 2])


turtle.Screen().exitonclick()
