# Car class for turtle crossing game.

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

DIR_WEST = 90

PLAYER_COLLISION_DISTANCE = 25

class Car(Turtle):
    def __init__(self, move_speed):
        """Car class to handle each car that appears on the screen.
        Its color and starting y-position are randomly chosen.

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

    def drove_offscreen(self):
        """Check if the car has driven across the road and offscreen 
        (and therefore can be deleted)."""
        return (self.xcor() < CAR_ZONE_LEFT - OFFSCREEN_OFFSET)
