# Scoreboard class for the snake game project.

from turtle import Turtle

SCREEN_HEIGHT = 600
ALIGNMENT = "center"
FONT = ("Courier New", 20, "bold")

class Scoreboard(Turtle):
    """A class to keep track of the score 
    and display it on the screen."""
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, SCREEN_HEIGHT/2 - 40)

        self.score = 0
        self.draw_score()

    def increase_score(self):
        """Increase the score by 1."""
        self.score += 1
        self.draw_score()

    def draw_score(self):
        """Draw the current score on the screen."""
        score_str = f"Score: {self.score}"
        self.clear()
        self.write(arg=score_str, align=ALIGNMENT, font=FONT)

    def show_game_over(self):
        """Tell the user the game is over."""
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
