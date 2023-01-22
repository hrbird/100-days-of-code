# Paddle for pong game.
from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        """Class to handle the paddles on either side of the screen.
        
        Args:
            x_cor (int): x-coordinate of paddle position
            y_cor (int): y-coordinate of paddle position
        """
        super().__init__()

        # Make the paddle a tall white rectangle.
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,  stretch_len=1)

        # Move it to its given position without drawing a path.
        self.penup()
        self.goto(x_cor, y_cor)

    def go_up(self):
        """Move the paddle upward."""
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def go_down(self):
        """Move the paddle downward."""
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
