# A turtle walks forward ten steps every time the user presses the space bar.
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.pensize(3)

screen = Screen()

def move_forward():
    timmy.forward(10)

# When the user presses "space", the turtle walks forward.
screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()

