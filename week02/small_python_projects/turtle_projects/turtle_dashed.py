# Draws a dashed line in Turtle.
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

# Draw a dashed line.
for i in range(20):
    # Show the line for 10 pixels.
    timmy.pendown()
    timmy.forward(10)

    # Hide the line for 10 pixels.
    timmy.penup()
    timmy.forward(10)

screen = Screen()
screen.exitonclick()