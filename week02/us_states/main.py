# Game to guess the names of all the 50 states in the US.
# Each time the player correctly guesses a state name, it appears on the map.
# Uses both the turtle graphics library and the pandas library.

import turtle
from os.path import dirname, join
import pandas

# Set up the screen.
screen = turtle.Screen()
screen.title("US States Game")

# Get the US States data from the 50_states.csv file and load it into a pandas DataFrame.
CURRENT_DIR = dirname(__file__)
DATA_FILE_PATH = join(CURRENT_DIR, "./50_states.csv")
STATES_DATA = pandas.read_csv(DATA_FILE_PATH)

# Get a list of all the states.
ALL_STATES = STATES_DATA["state"].to_list()

# Get the file path of the blank US states image and show it on the screen.
IMG_FILE_PATH = join(CURRENT_DIR, "./blank_states_img.gif")
screen.addshape(IMG_FILE_PATH)
turtle.shape(IMG_FILE_PATH)

# Create a Turtle writer to write correctly-guessed state names on the map.
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

# Create a Turtle score writer to draw the current score on the map.
score_writer = turtle.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(-350,250)

# Keep track of the states correctly guessed so far in a list of state names.
guessed_states = []

def get_guess_from_player():
    """Prompt the user to type and enter a state's name.
    Returns a string of the guessed state."""

    prompt_text = "Enter a state's name:"
    guess_state = screen.textinput(title="Guess the State", prompt=prompt_text)

    # Clean the guess text of whitespace and convert it to title case.
    guess_state = str(guess_state).strip().title()
    print(f"Player guessed: {guess_state}")

    return guess_state

def is_guess_correct(guess_state):
    """Check if the guessed state is a correct US state.
    Returns True if the state is correct and has not been guessed yet.
    Else, returns False."""
    return (guess_state in ALL_STATES and guess_state not in guessed_states)

def write_state_on_map(state_name):
    """Write the given state name in the correct place on the map."""
    # Get the data row for the given state.
    s = STATES_DATA[STATES_DATA["state"] == state_name]

    if len(s) > 0:
        # Get the x and y coordinates of the state on the map.
        x = int(s["x"])
        y = int(s["y"])
        print(f"x = {x}, y = {y}")

        # Write the name of the state on the map.
        writer.goto(x=x, y=y)
        writer.write(arg=state_name, align="center", font=("Courier New", 10))

def write_score():
    """Write the current score on the map."""
    score_writer.clear()

    num_states = len(guessed_states)
    score_str = f"SCORE: {num_states} / 50"
    if num_states == 50:
        score_str += "  Great job, you got them all!"

    score_writer.write(arg=score_str, align="left", font=("Courier New", 16, "bold"))

def play_game():
    """Start the game and control the game loop."""

    write_score()

    is_game_over = False
    while not is_game_over:

        # If player guessed all 50 states, they win!
        if len(guessed_states) == 50:
            print("\nWow, you guessed all 50 states!\nGreat job!")
            is_game_over = True

        else:
            # Get a guess from the player.
            new_guess = get_guess_from_player()

            # If the player enters "Q" or "Quit", quit the game.
            if new_guess in ["Q", "Quit"]:
                is_game_over = True

            # Else, check if the guess is correct.
            elif is_guess_correct(new_guess):

                # If so, write the name of the state on the map.
                write_state_on_map(new_guess)

                # Add the state to the list of guessed states.
                guessed_states.append(new_guess)

                # Update the score.
                write_score()


play_game()

# Keep the game running.
turtle.mainloop()