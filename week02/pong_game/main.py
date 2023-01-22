# Pong game.
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COLLISION_DISTANCE = 30

# Boundaries of the screen.
WALL_X_RIGHT = SCREEN_WIDTH/2 - 20
WALL_X_LEFT = -SCREEN_WIDTH/2 + 20
WALL_Y_TOP = SCREEN_HEIGHT/2 - 20
WALL_Y_BOTTOM = -SCREEN_HEIGHT/2 + 20

# Paddle positions.
RIGHT_PADDLE_X = SCREEN_WIDTH/2 - 50
LEFT_PADDLE_X = -(SCREEN_WIDTH/2) + 50

# Set up the screen.
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")

# Turn off turtle animation so we can control when the screen is redrawn.
screen.tracer(0)

# Create custom objects.
right_paddle = Paddle(x_cor=RIGHT_PADDLE_X, y_cor=0)
left_paddle = Paddle(x_cor=LEFT_PADDLE_X, y_cor=0)
ball = Ball()

# If the user presses the arrow keys, move the right paddle.
screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

# If the user presses the W/S keys, move the left paddle.
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

def play_game():
    print("Starting new game.")
    # Game loop.
    is_game_over = False
    while not is_game_over:

        # Pause for 0.1 seconds.
        time.sleep(0.1)

        
        # Draw all objects on the screen.
        screen.update()

        # Move the ball.
        ball.move()

        # Detect collision between the ball and top or bottom walls.
        if ball.ycor() > WALL_Y_TOP or ball.ycor() < WALL_Y_BOTTOM:
            ball.bounce_y()

        # Detect collision between the ball and the right paddle.
        if ball.distance(right_paddle) < 50 and ball.xcor() > RIGHT_PADDLE_X - COLLISION_DISTANCE:
            ball.bounce_x()

        # Detect collision between the ball and the left paddle.
        if ball.distance(left_paddle) < 50 and ball.xcor() < LEFT_PADDLE_X + COLLISION_DISTANCE:
            ball.bounce_x()


def main():
    play_game()

if __name__ == "__main__":
    main()

screen.exitonclick()