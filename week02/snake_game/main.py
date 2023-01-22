# Snake game.
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FOOD_COLLISION_DISTANCE = 20
TAIL_COLLISION_DISTANCE = 10

# Boundaries of the screen where the Snake is allowed.
WALL_X_RIGHT = SCREEN_WIDTH/2 - 20
WALL_X_LEFT = -SCREEN_WIDTH/2 + 20
WALL_Y_UP = SCREEN_HEIGHT/2 - 20
WALL_Y_DOWN = -SCREEN_HEIGHT/2 + 20

# Set up the screen.
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
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

def play_game():

    # Game loop.
    is_game_over = False
    while not is_game_over:

        # Pause for 0.1 seconds.
        time.sleep(0.1)

        # Move the snake forward.
        snake.move()

        # Draw all objects on the screen.
        screen.update()

        # Detect collision between snake head and food.
        if snake.head.distance(food) < FOOD_COLLISION_DISTANCE:
            food.go_to_random_spot()
            snake.extend()
            scoreboard.increase_score()
            
        # Detect collision between snake head and wall.
        if snake.head.xcor() > WALL_X_RIGHT or snake.head.xcor() < WALL_X_LEFT or snake.head.ycor() > WALL_Y_UP or snake.head.ycor() < WALL_Y_DOWN:
            is_game_over = True
            scoreboard.show_game_over()
        
        # Detect collision between snake head and any segment in the tail.
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < TAIL_COLLISION_DISTANCE:
                is_game_over = True
                scoreboard.show_game_over()

def main():
    play_game()

if __name__ == "__main__":
    main()

screen.exitonclick()
