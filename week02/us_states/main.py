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
TEXT_ALIGNMENT = "center"
FONT = ("Courier New", 10)
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

# Keep track of the states correctly guessed so far in a list of state names.
guessed_states = []

def get_guess_from_player():
    """Prompt the user to type and enter a state's name."""

    prompt_text = "Enter a state's name:"
    guess_state = screen.textinput(title="Guess the State", prompt=prompt_text)

    # Clean the guess text of whitespace and convert it to title case.
    guess_state = str(guess_state).strip().title()
    print(f"Player guessed: {guess_state}")

    return guess_state

def is_guess_correct(guess_state):
    """Check if the guessed state is a correct US state."""
    return (guess_state in ALL_STATES and guess_state not in guessed_states)

def write_state_on_map(state_name):

    # Get the data row for the given state.
    s = STATES_DATA[STATES_DATA["state"] == state_name]

    if len(s) > 0:
        # Get the x and y coordinates of the state on the map.
        x = int(s["x"])
        y = int(s["y"])
        print(f"x = {x}, y = {y}")

        # Write the name of the state on the map.
        writer.goto(x=x, y=y)
        writer.write(arg=state_name, align=TEXT_ALIGNMENT, font=FONT)

def play_game():

    is_game_over = False
    while not is_game_over:

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

    # If player guessed all 50 states, they win!
    if len(guessed_states) == 50:
        print("\nWow, you guessed all 50 states!\n")
        is_game_over = True


play_game()

def get_mouse_click_coor(x, y):
    """"""
    print(x, y)

# Event listener for the mouse clicking on the screen.
turtle.onscreenclick(get_mouse_click_coor)

# Keep the game running.
turtle.mainloop()