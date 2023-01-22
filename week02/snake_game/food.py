# Food class for the snake game project.

from turtle import Turtle
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Boundaries of the screen where the Food can be placed.
SCREEN_BOUND_X_RIGHT = SCREEN_WIDTH/2 - 20
SCREEN_BOUND_X_LEFT = -SCREEN_BOUND_X_RIGHT
SCREEN_BOUND_Y_UP = SCREEN_HEIGHT/2 - 20
SCREEN_BOUND_Y_DOWN = -SCREEN_BOUND_Y_UP

class Food(Turtle):
    """A class to handle the food that the snake eats. 
    The food appears in a random location on the screen, 
    and if the head of the snake eats it, the food moves 
    to a different random location."""

    def __init__(self):
        super().__init__()

        # Make the food a small, blue circle that does not draw a path.
        self.shape("circle")
        self.color("turquoise3")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")

        self.go_to_random_spot()
        
    def go_to_random_spot(self):
        """Move the food to a random location on the screen."""
        random_x = random.randint(SCREEN_BOUND_X_LEFT, SCREEN_BOUND_X_RIGHT)
        random_y = random.randint(SCREEN_BOUND_Y_DOWN, SCREEN_BOUND_Y_UP)
        self.goto(random_x, random_y)