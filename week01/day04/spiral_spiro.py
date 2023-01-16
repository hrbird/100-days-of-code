# Learning and playing with the Turtle graphics library.
# This program draws a green spiral spirograph image using Turtle.

import turtle

COLORS = ["green", "darkgreen"]

# Set the background color to black and hide the pointer.
turtle.bgcolor("black")
turtle.hideturtle()
turtle.speed(500)


t = turtle.Turtle()

# From the center, draw lines that are 1 degree off from being a right angle.
# The lines start at 1 px long and grow with each iteration to be longer.
# This forms a spiral shape pattern.
# Also, alternate each line between green and dark-green to emphasize the spiral.
for i in range(400):
    t.forward(i + 1)
    t.right(89)
    t.pencolor(COLORS[i % 2])


turtle.Screen().exitonclick()
