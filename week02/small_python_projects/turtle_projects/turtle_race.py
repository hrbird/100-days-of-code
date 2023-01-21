# Six turtles race across the screen, at random speeds.
from turtle import Turtle, Screen
import random

# My favorite rainbow color scheme.
COLORS = [
    "firebrick", "orangered", "gold1", 
    "green", "royalblue1", "slateblue3"
]

# Corresponding names for the turtles (basic colors)
TURTLE_NAMES = [
    "red", "orange", "yellow",
    "green", "blue", "purple"
]

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
TURTLE_WIDTH = 20
TURTLE_HEIGHT = 20

# Set up screen.
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

winning_color = ""

# Create the turtles.
turtles = []
for i in range(len(COLORS)):

    t = Turtle(shape="turtle")
    t.color(COLORS[i])
    t.penup()

    # Line up each turtle on the left edge
    turtle_spacing = TURTLE_HEIGHT + 30
    x_coord = -(SCREEN_WIDTH / 2) + TURTLE_WIDTH
    y_coord = (SCREEN_HEIGHT * 0.3) - (i * turtle_spacing)
    t.goto(x=x_coord, y=y_coord)

    turtles.append(t)

# Get the user's bet on the winner.
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (red, orange, yellow, green, blue, or purple): ")
print(f"You bet on the {user_bet} turtle.")

# If the user placed a bet, start the race.
if user_bet in TURTLE_NAMES:
    is_race_on = True
else:
    print(f"Sorry, there is no {user_bet} turtle in the race.")

# Start the turtle race.
while is_race_on:
    # Each turtle moves a random distance.
    for t in range(len(turtles)):
        rand_distance = random.randint(0, 10)
        turtles[t].forward(rand_distance)

        # When one of the turtles reaches the other side of the screen,
        # end the race and declare the winner.
        if turtles[t].xcor() >= (SCREEN_WIDTH/2) - TURTLE_WIDTH:
            is_race_on = False

            winning_color = TURTLE_NAMES[t]

            if winning_color == user_bet:
                print(f"Congrats!")
            else:
                print(f"Sorry, you've lost.")
            print(f"The {winning_color} turtle won the race!")

screen.exitonclick()