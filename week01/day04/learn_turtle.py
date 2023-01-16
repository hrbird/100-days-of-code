# Learning and playing with the Turtle graphics library.
# Simple program that creates a green turtle and has it create 
# an original modern art piece by walking in a random direction
# for a random number of steps.

import turtle
import random

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.shapesize(2, 2)
timmy.color("DarkSeaGreen")

directions = [0, 45, 90, 135, 180, 225, 270, 315]

screen_width = 300
screen_height = 300

for i in range(50):
    # Check if Timmy has walked off-screen. If so, point him back to the center.
    x_cor = timmy.xcor()
    y_cor = timmy.ycor()
    if x_cor < -screen_width or x_cor > screen_width or y_cor < -screen_height or y_cor > screen_height:
        timmy.home()
    else:
        # Have Timmy walk a random number of steps in a random direction.
        timmy.setheading(directions[random.randint(0, len(directions) - 1)])

    timmy.forward(random.randint(50, 100))

my_screen = turtle.Screen()
my_screen.exitonclick()
my_screen.screensize(300, 300)
