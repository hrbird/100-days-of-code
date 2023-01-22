# Pong game.
from turtle import Turtle, Screen
from paddle import Paddle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COLLISION_DISTANCE = 20

# Boundaries of the screen.
WALL_X_RIGHT = SCREEN_WIDTH/2 - 20
WALL_X_LEFT = -SCREEN_WIDTH/2 + 20
WALL_Y_UP = SCREEN_HEIGHT/2 - 20
WALL_Y_DOWN = -SCREEN_HEIGHT/2 + 20

# Set up the screen.
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")

# Turn off turtle animation so we can control when the screen is redrawn.
screen.tracer(0)

# Create custom objects.
player_paddle = Paddle()


# If the user presses the arrow keys, move the player paddle.
screen.listen()
screen.onkeypress(player_paddle.go_up, "Up")
screen.onkeypress(player_paddle.go_down, "Down")

def play_game():
    print("Starting new game.")
    # Game loop.
    is_game_over = False
    while not is_game_over:

        # Draw all objects on the screen.
        screen.update()

def main():
    play_game()

if __name__ == "__main__":
    main()

screen.exitonclick()