# Snake game.
from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Turn off turtle animation so we can control when the screen is redrawn.
screen.tracer(0)

# The height/width of each square segment of the snake's body
SEGMENT_SIZE = 20

# The number of pixels to move at a time.
STEP_DISTANCE = 20

# A list to hold each turtle segment of the snake's body
segments = []

# Create the 3 starting body segments.
for i in range(3):
    t = Turtle(shape="square")
    t.color("white")
    t.width(SEGMENT_SIZE)
    t.penup()
    t.goto(x=(i * -SEGMENT_SIZE), y=0)

    segments.append(t)

is_game_over = False
while not is_game_over:

    # Draw all objects on the screen.
    screen.update()

    # Pause for 0.1 seconds.
    time.sleep(0.1)

    # Starting with the tail tip, move each segment 
    # to where the segment in front of it is.
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    
    # Move the first segment forward.
    segments[0].forward(STEP_DISTANCE)

    


screen.exitonclick()
