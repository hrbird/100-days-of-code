# Player class for turtle crossing game.

from turtle import Turtle

STARTING_X_POS = 0
STARTING_Y_POS = -280
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
DIR_NORTH = 90

class Player(Turtle):
    def __init__(self):
        """Class to control the player turtle character that
        the player moves across the street, dodging cars."""
        super().__init__()

        self.penup()
        self.shape("turtle")
        self.setheading(DIR_NORTH)

        self.reset_position()

    def reset_position(self):
        """Send the turtle back to its starting position."""
        self.goto(STARTING_X_POS, STARTING_Y_POS)

    def move(self):
        """Make the turtle walk up (across the street)."""
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def reached_finish_line(self):
        """Checks whether the player has reached the finish line (top edge)."""
        return (self.ycor() >= FINISH_LINE_Y)
        