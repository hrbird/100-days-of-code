# CarManager class for turtle crossing game.

from car import Car

STARTING_MOVE_SPEED = 5
LEVEL_UP_SPEED_INCREASE = 1.2

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
            if self.cars[c].drove_offscreen():
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
