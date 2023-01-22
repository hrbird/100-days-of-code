# Pong game.

# The classic game of Pong, in two players control paddles to hit a ball 
# back and forth across the screen. When the ball hits a paddle, it bounces 
# in the opposite direction and its speed increases. If the ball hits the 
# top or bottom edge, it bounces. If a player misses the ball and it goes 
# off the left or right edge, their score increases by 1 and the ball 
# returns to the center of the screen. Whoever has the lowest score wins.

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COLLISION_DISTANCE = 30

# Boundaries of the screen.
WALL_X_RIGHT = SCREEN_WIDTH/2
WALL_X_LEFT = -SCREEN_WIDTH/2
WALL_Y_TOP = SCREEN_HEIGHT/2 - 20
WALL_Y_BOTTOM = -SCREEN_HEIGHT/2 + 20

# Paddle positions.
LEFT_PADDLE_X = -(SCREEN_WIDTH/2) + 50
RIGHT_PADDLE_X = SCREEN_WIDTH/2 - 50

# Set up the screen.
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")

# Turn off turtle animation so we can control when the screen is redrawn.
screen.tracer(0)

# Create custom objects.
left_paddle = Paddle(x_cor=LEFT_PADDLE_X, y_cor=0)
right_paddle = Paddle(x_cor=RIGHT_PADDLE_X, y_cor=0)
ball = Ball()
scoreboard = Scoreboard()

# If the user presses the W/S keys, move the left paddle.
screen.listen()
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

# If the user presses the arrow keys, move the right paddle.
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

def detect_collision():
    # Detect collision for the ball.
    if ball.ycor() > WALL_Y_TOP or ball.ycor() < WALL_Y_BOTTOM:
        # Collision with top or bottom walls.
        ball.bounce_y()

    elif ball.distance(left_paddle) < 50 and ball.xcor() < left_paddle.xcor() + COLLISION_DISTANCE and ball.x_move < 0:
        # Collision with left paddle.
        ball.bounce_x()

    elif ball.distance(right_paddle) < 50 and ball.xcor() > right_paddle.xcor() - COLLISION_DISTANCE and ball.x_move > 0:
        # Collision with right paddle.
        ball.bounce_x()

    elif ball.xcor() < WALL_X_LEFT:
        # Collision with left wall (left player missed).
        ball.reset_position()
        scoreboard.l_point()

    elif ball.xcor() > WALL_X_RIGHT:
        # Collision with right wall (right player missed).
        ball.reset_position()
        scoreboard.r_point()

def play_game():
    print("Starting new game.")
    # Game loop.
    is_game_over = False
    while not is_game_over:

        # Pause in each loop to keep game running smoothly.
        time.sleep(ball.move_speed)

        # Draw all objects on the screen.
        screen.update()

        # Move the ball in its current direction.
        ball.move()

        # Detect collision for the ball.
        detect_collision()

def main():
    play_game()

if __name__ == "__main__":
    main()

screen.exitonclick()