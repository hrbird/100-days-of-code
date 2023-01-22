# Ball for pong game.
from turtle import Turtle

MOVE_DISTANCE = 10
MOVE_SPEED = 0.1

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

        # Movement directions.
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE

        # Movement speed.
        self.move_speed = MOVE_SPEED

    def move(self):
        """Move the ball upward."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    def bounce_y(self):
        """Make the ball bounce if it hits the top or bottom wall."""

        # If the ball hits the top wall, it bounces to move downward.
        # If the ball hits the bottom wall, it bounces to move upward.
        self.y_move *= -1

    def bounce_x(self):
        """Make the ball bounce if it hits the left or right paddle."""

        # If the ball hits the right paddle, it bounces left.
        # If the ball hits the left paddle, it bounces right.
        self.x_move *= -1

        # Speed the ball up a bit every time it bounces off a paddle.
        self.move_speed *= 0.9

    def reset_position(self):
        """Send the ball back to the center of the screen and
        make it move in the opposite direction."""
        self.goto(0, 0)
        self.bounce_x()

        # Reset ball speed.
        self.move_speed = MOVE_SPEED


