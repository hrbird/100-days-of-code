# The QuizInterface class creates a GUI for the Quizzler program.

from os.path import dirname, join
import tkinter as tk

#=========================================
# CONSTANTS
#=========================================

# Constants
THEME_COLOR = "#375362"
WHITE_COLOR = "white"

# Minimum window dimensions
MIN_WIDTH = 300
MIN_HEIGHT = 300

# Dimensions of question area
Q_WIDTH = 300
Q_HEIGHT = 250

# Padding inside widgets
PAD_X = 20
PAD_Y = 20

# Fonts
SCORE_FONT = ("Arial", 16, "bold")
QUESTION_FONT = ("Arial", 20, "italic")

# Image file paths
CURRENT_DIR = dirname(__file__)
TRUE_IMG_FILE_PATH = join(CURRENT_DIR, "./images/true.png")
FALSE_IMG_FILE_PATH = join(CURRENT_DIR, "./images/false.png")

#=========================================
# QUIZINTERFACE CLASS
#=========================================

class QuizInterface:
    """The QuizInterface class """
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=MIN_WIDTH, height=MIN_HEIGHT)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Create a "Score" label.
        self.score_label = tk.Label(
            fg=WHITE_COLOR, 
            bg=THEME_COLOR, 
            font=SCORE_FONT, 
            text="Score: 0",
            justify="right"
        )
        self.score_label.grid(row=0, column=1)

        # Show the current question on a white canvas background.
        self.canvas = tk.Canvas(
            width=Q_WIDTH, 
            height=Q_HEIGHT, 
            bg=WHITE_COLOR, 
            highlightthickness=0
        )
        self.question_text = self.canvas.create_text(
            Q_WIDTH/2, 
            Q_HEIGHT/2, 
            text="Lorem ispsum", 
            fill=THEME_COLOR, 
            font=QUESTION_FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=PAD_Y)

        # Create the green checkmark button for the user to choose "True".
        self.true_img = tk.PhotoImage(file=TRUE_IMG_FILE_PATH)
        self.true_button = tk.Button(
            image=self.true_img, 
            highlightthickness=0,
            command=self.answer_true
        )
        self.true_button.grid(row=2, column=0)

        # Create the red X button for the user to choose "False".
        self.false_img = tk.PhotoImage(file=FALSE_IMG_FILE_PATH)
        self.false_button = tk.Button(
            image=self.false_img, 
            highlightthickness=0,
            command=self.answer_false
        )
        self.false_button.grid(row=2, column=1)

        # Keep the window open.
        self.window.mainloop()

    def answer_true(self):
        print("Clicked true!")

    def answer_false(self):
        print("Clicked false!")