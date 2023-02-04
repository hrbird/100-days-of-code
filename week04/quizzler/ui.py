# The QuizInterface class creates a GUI for the Quizzler program.

from os.path import dirname, join
import tkinter as tk
import quiz_brain

#=========================================
# CONSTANTS
#=========================================

# Constants
THEME_COLOR = "#375362"
WHITE_COLOR = "white"
GREEN_COLOR = "#9ebd75"
RED_COLOR = "#cc4c35"

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

# Time to flash feedback color, in milliseconds
FEEDBACK_TIME = 3000

#=========================================
# QUIZINTERFACE CLASS
#=========================================

class QuizInterface:
    """The QuizInterface class creates a graphical user interface for the quiz.
    It receives a QuizBrain object."""
    def __init__(self, quiz_brain: quiz_brain.QuizBrain):
        
        # QuizBrain object to control the quiz
        self.quiz_brain = quiz_brain

        # Create a tkinter window for the UI.
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=MIN_WIDTH, height=MIN_HEIGHT)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Create a "Q #" label to show the current question number.
        self.qnum_label = tk.Label(
            fg=WHITE_COLOR, 
            bg=THEME_COLOR, 
            font=SCORE_FONT, 
            text="Q #1",
            justify="left"
        )
        self.qnum_label.grid(row=0, column=0)

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
            width=Q_WIDTH-PAD_X,
            text="", 
            fill=THEME_COLOR, 
            font=QUESTION_FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=PAD_Y)

        # Create the green checkmark button for the user to choose "True".
        self.true_img = tk.PhotoImage(file=TRUE_IMG_FILE_PATH)
        self.true_button = tk.Button(
            image=self.true_img, 
            highlightthickness=0,
            command=self.clicked_true
        )
        self.true_button.grid(row=2, column=0)

        # Create the red X button for the user to choose "False".
        self.false_img = tk.PhotoImage(file=FALSE_IMG_FILE_PATH)
        self.false_button = tk.Button(
            image=self.false_img, 
            highlightthickness=0,
            command=self.clicked_false
        )
        self.false_button.grid(row=2, column=1)

        # Show the first question.
        self.show_next_question()

        # Keep the window open.
        self.window.mainloop()

    def show_next_question(self):
        """Show the next quiz question on the screen."""

        # Reset the background color behind the question text to white.
        self.canvas.config(bg=WHITE_COLOR)

        # Check if the quiz is finished.
        if self.quiz_brain.is_quiz_done():
            self.end_quiz()
            
        else:
            # Update the question number.
            qnum_str = f"Q #{self.quiz_brain.get_cur_question_num()}"
            self.qnum_label.config(text=qnum_str)

            # Get the next question.
            q_text = self.quiz_brain.get_cur_question()
            self.canvas.itemconfig(self.question_text, text=q_text)


    def clicked_true(self):
        """
        Triggered when the user clicks the True button.
        Checks whether this answer is correct or not.
        """
        is_correct = self.quiz_brain.check_answer(True)
        self.give_feedback(is_correct)


    def clicked_false(self):
        """
        Triggered when the user clicks the False button.
        Checks whether this answer is correct or not.
        """
        is_correct = self.quiz_brain.check_answer(False)
        self.give_feedback(is_correct)


    def give_feedback(self, is_answer_correct: bool):
        """Updates the score and makes the screen briefly flash:
            - Green if the user answers a question correctly
            - Red if the user answers a question incorrectly

        Args:
            is_answer_correct (bool): whether or not the user correctly answered a question
        """

        # Update the score.
        score_str = f"Score: {self.quiz_brain.num_correct}"
        self.score_label.config(text=score_str)

        # Make the screen flash green or red.
        if is_answer_correct:
            self.canvas.config(bg=GREEN_COLOR)
        else:
            self.canvas.config(bg=RED_COLOR)

        # Go to the next question.
        self.quiz_brain.go_to_next_question()

        # After a second, reset the color to white.
        self.window.after(FEEDBACK_TIME, self.show_next_question)
       
    
    def end_quiz(self):
        """When the user finishes the quiz, show the final score."""

        # Show the final score.
        score_str = self.quiz_brain.get_final_score_str()
        self.canvas.itemconfig(self.question_text, text=score_str)

        # Reset the question number and score labels.
        self.qnum_label.config(text="")
        self.score_label.config(text="")

        # Disable the buttons.
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")