# Ball for pong game.
from turtle import Turtle

MOVE_DISTANCE = 10

class Ball(Turtle):
    def __init__(self):
        """Class to handle the ball that moves across the screen."""
        super().__init__()

        # Make the ball a white circle.
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1,  stretch_len=1)

        # Make sure it doesn't draw a path.
        self.penup()

    def move(self):
        """Move the ball upward."""
        new_x = self.xcor() + MOVE_DISTANCE
        new_y = self.ycor() + MOVE_DISTANCE

        self.goto(new_x, new_y)
