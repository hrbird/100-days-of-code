# Snake game.
from turtle import Turtle, Screen
from snake import Snake
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Turn off turtle animation so we can control when the screen is redrawn.
screen.tracer(0)

# Create a snake object.
snake = Snake()

# If the user presses the arrow keys, change the snake's direction.
screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")


# Game loop.
is_game_over = False
while not is_game_over:

    # Draw all objects on the screen.
    screen.update()

    # Pause for 0.1 seconds.
    time.sleep(0.1)

    # Move the snake forward.
    snake.move()
    
screen.exitonclick()
