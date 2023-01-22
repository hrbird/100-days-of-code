# Player class for turtle crossing game.

from turtle import Turtle

STARTING_X_POS = 0
STARTING_Y_POS = -280
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        """Class to control the player turtle character that
        the player moves across the street, dodging cars."""
        super().__init__()

        self.penup()
        self.shape("turtle")

        self.reset_position()

    def reset_position(self):
        self.goto(STARTING_X_POS, STARTING_Y_POS)
