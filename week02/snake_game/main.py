# Snake game.
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# The height/width of each square segment of the snake's body
SEGMENT_SIZE = 20

snake_body = []

for i in range(3):

    t = Turtle(shape="square")
    t.color("white")
    t.width(SEGMENT_SIZE)
    t.penup()
    t.goto(x=(i * -20), y=0)

    snake_body.append(t)




screen.exitonclick()