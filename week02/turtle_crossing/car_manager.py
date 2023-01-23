# CarManager class for turtle crossing game.

from turtle import Turtle
import random

COLORS = [
    "firebrick", "orangered", "gold1", "darkolivegreen1", "seagreen1",
    "skyblue1", "royalblue1", "slateblue3", "deeppink4"
]

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WALL_X_RIGHT = SCREEN_WIDTH/2
WALL_X_LEFT = -SCREEN_WIDTH/2
WALL_Y_TOP = SCREEN_HEIGHT/2 - 20
WALL_Y_BOTTOM = -SCREEN_HEIGHT/2 + 20

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT_SLOW = 8
MOVE_INCREMENT_FAST = 12
DIR_WEST = 90


class Car(Turtle):
    def __init__(self):
        """Car class to handle each car that appears on the screen.
        Its color, speed, and starting y-position are randomly chosen."""
        super().__init__()

        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.setheading(DIR_WEST)

        # Set random attributes.
        x_pos = SCREEN_WIDTH/2 + 30
        y_pos = random.randint(WALL_Y_BOTTOM, WALL_Y_TOP)
        self.goto(x_pos, y_pos)
        self.color(random.choice(COLORS))
        self.move_speed = random.randint(MOVE_INCREMENT_SLOW, MOVE_INCREMENT_FAST)

    def move(self):
        new_x = self.xcor() - self.move_speed
        self.goto(new_x, self.ycor())


class CarManager:
    def __init__(self):
        """CarManager class to handle all of the cars together."""
        self.cars = []

    def create_car(self):
        """Creates a car with a random color, starting position, and speed."""
        self.cars.append(Car())

    def move_cars(self):
        """Move all cars forward."""
        for c in self.cars:
            c.move()

    def delete_old_cars(self):
        """Delete any cars that have moved off-screen."""
        num_cars = len(self.cars)

        # Go through the cars list backwards and delete cars beyond the left edge.
        for c in range(num_cars - 1, -1, -1):
            if self.cars[c].xcor() < WALL_X_LEFT - 30:
                #print(f"Deleting car #{c} since its xcor is {self.cars[c].xcor()}")
                self.cars.pop(c)

    def update(self):
        """Update the cars by moving the cars and deleting old cars."""

        self.move_cars()
        self.delete_old_cars()
