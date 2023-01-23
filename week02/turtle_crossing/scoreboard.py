# Scoreboard class for the turtle crossing game project.

from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier New", 24, "bold")

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Scoreboard(Turtle):
    def __init__(self):
        """A class to keep track of the level and display it on the screen."""
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()

        # Track the player's level.
        self.level = 0

        # Positions
        X_POS = -(SCREEN_WIDTH/2) + 30
        Y_POS = SCREEN_HEIGHT/2 - 50
        self.goto(X_POS, Y_POS)

        self.draw_level()

    def level_up(self):
        """Increase the level by 1."""
        self.level += 1
        self.draw_level()

    def draw_level(self):
        """Draw the current level on the screen."""
        self.clear()
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def show_game_over(self):
        """Tell the user the game is over."""
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
