# Turtle crossing game

import time
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

def play_game():
    print("Starting new game.")
    # Game loop.
    is_game_over = False
    while not is_game_over:

        # Pause in each loop to keep game running smoothly.
        time.sleep(0.1)

        # Draw all objects on the screen.
        screen.update()

def main():
    play_game()

if __name__ == "__main__":
    main()

screen.exitonclick()