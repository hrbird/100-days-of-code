# Paddle for pong game.
from turtle import Turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVE_DISTANCE = 20

class Paddle(Turtle):
    """Class to handle the paddles on either side of the screen."""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,  stretch_len=1)
        self.penup()
        self.goto(SCREEN_WIDTH/2 - 50, 0)

    def go_up(self):
        """Move the paddle upward."""
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def go_down(self):
        """Move the paddle downward."""
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
