# CarManager class for turtle crossing game.

from turtle import Turtle
import random

COLORS = [
    "firebrick", "orangered", "gold1", "darkolivegreen1", "seagreen1",
    "skyblue1", "royalblue1", "slateblue3", "deeppink4"
]

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CAR_ZONE_RIGHT = SCREEN_WIDTH/2
CAR_ZONE_LEFT = -SCREEN_WIDTH/2
CAR_ZONE_TOP = SCREEN_HEIGHT/2 - 50
CAR_ZONE_BOTTOM = -SCREEN_HEIGHT/2 + 50
OFFSCREEN_OFFSET = 30

STARTING_MOVE_SPEED = 5
LEVEL_UP_SPEED_INCREASE = 1.2
DIR_WEST = 90

PLAYER_COLLISION_DISTANCE = 25


class Car(Turtle):
    def __init__(self, move_speed):
        """Car class to handle each car that appears on the screen.
        Its color, speed, and starting y-position are randomly chosen.

        Args:
            move_speed (int): the movement speed of the car
        """
        super().__init__()

        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.setheading(DIR_WEST)

        # Set random attributes.
        x_pos = CAR_ZONE_RIGHT + OFFSCREEN_OFFSET
        y_pos = random.randint(CAR_ZONE_BOTTOM, CAR_ZONE_TOP)
        self.goto(x_pos, y_pos)
        self.color(random.choice(COLORS))
        self.move_speed = move_speed

    def move(self):
        new_x = self.xcor() - self.move_speed
        self.goto(new_x, self.ycor())

    def detect_collision(self, player_x, player_y):
        """Check if the player has been hit by a car.

        Args:
            player_x (int): the player's x-position
            player_y (int): the player's y-position
        """
        return (self.distance(player_x, player_y) <= PLAYER_COLLISION_DISTANCE)
        


class CarManager:
    def __init__(self):
        """CarManager class to handle all of the cars together."""
        self.cars = []
        self.car_move_speed = STARTING_MOVE_SPEED

    def create_car(self):
        """Creates a car with a random color, starting position, and speed."""
        self.cars.append(Car(self.car_move_speed))

    def move_cars(self):
        """Move all cars forward."""
        for c in self.cars:
            c.move()

    def delete_old_cars(self):
        """Delete any cars that have moved off-screen."""
        num_cars = len(self.cars)

        # Go through the cars list backwards and delete cars beyond the left edge.
        for c in range(num_cars - 1, -1, -1):
            if self.cars[c].xcor() < CAR_ZONE_LEFT - OFFSCREEN_OFFSET:
                #print(f"Deleting car #{c} since its xcor is {self.cars[c].xcor()}")
                self.cars.pop(c)

    def update(self):
        """Update the cars by moving the cars and deleting old cars."""

        self.move_cars()
        self.delete_old_cars()

    def increase_car_speed(self):
        """Each time the player levels up, increase the speed of the new cars."""
        self.car_move_speed *= LEVEL_UP_SPEED_INCREASE

    def detect_collision(self, player_x, player_y):
        """Check if the player has been hit by a car.

        Args:
            player_x (int): the player's x-position
            player_y (int): the player's y-position
        """
        for c in self.cars:
            if c.detect_collision(player_x, player_y):
                return True
            
        return False
