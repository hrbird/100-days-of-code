# Turtle crossing game

import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

# Turn off turtle animation so we can control when the screen is redrawn.
screen.tracer(0)

# Custom classes.
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


# If the user presses the Up key, move the turtle up/forward.
screen.listen()
screen.onkeypress(player.move, "Up")


def play_game():
    print("Starting new game.")
    # Game loop.
    is_game_over = False
    while not is_game_over:

        # Pause in each loop to keep game running smoothly.
        time.sleep(0.1)

        # Move all of the cars on the screen.
        car_manager.update()
        
        # Draw all objects on the screen.
        screen.update()

        # Add a new car randomly.
        if random.randint(0, 5) == 0:
            car_manager.create_car()

        # If the turtle reaches the top edge of the screen:
        #   The player levels up.
        #   The turtle is sent back to the bottom again.
        #   The cars speed up a bit.
        if player.reached_finish_line():
            scoreboard.level_up()
            player.reset_position()
            car_manager.increase_car_speed()
            print("You reached the finish line!")
            print(f"You are now level {scoreboard.level} and cars are moving at a speed of {car_manager.car_move_speed}.")

        # If the player collides with a car, it's game over.
        if car_manager.detect_collision(player.xcor(), player.ycor()):
            print("Uh oh! You got hit by a car!\nGAME OVER\n")
            is_game_over = True
            scoreboard.show_game_over()

def main():
    play_game()

if __name__ == "__main__":
    main()

screen.exitonclick()