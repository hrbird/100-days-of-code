# Scoreboard class for the pong game project.

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier New", 48, "bold")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        """A class to keep track of the scores and display them on the screen."""
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()

        # Track the players' scores.
        self.left_score = 0
        self.right_score = 0

        # Positions
        self.LEFT_X_POS = -100
        self.RIGHT_X_POS = 100
        self.Y_POS = 200

        self.draw_scores()

    def l_point(self):
        """Increase the left player's score by 1."""
        self.left_score += 1
        self.draw_scores()

    def r_point(self):
        """Increase the right player's score by 1."""
        self.right_score += 1
        self.draw_scores()

    def draw_scores(self):
        """Draw the current scores on the screen."""
        self.clear()

        # Left score.
        self.goto(self.LEFT_X_POS, self.Y_POS)
        self.write(arg=self.left_score, align=ALIGNMENT, font=FONT)

        # Right score.
        self.goto(self.RIGHT_X_POS, self.Y_POS)
        self.write(arg=self.right_score, align=ALIGNMENT, font=FONT)

    def show_game_over(self):
        """Tell the user the game is over."""
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
