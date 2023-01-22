# Snake game.
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time

FOOD_COLLISION_DISTANCE = 20

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Turn off turtle animation so we can control when the screen is redrawn.
screen.tracer(0)

# Create custom objects.
snake = Snake()             # Snake object
food = Food()               # Food object
scoreboard = Scoreboard()   # Scoreboard object

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

    # Detect collision between snake head and food.
    if snake.head.distance(food) < FOOD_COLLISION_DISTANCE:
        food.go_to_random_spot()
        scoreboard.increase_score()
    
screen.exitonclick()
