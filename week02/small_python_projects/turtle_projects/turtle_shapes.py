# Draws a variety of overlapping shapes in Turtle.
from turtle import Turtle, Screen

SIDE_LENGTH = 100

# My favorite rainbow color scheme.
COLORS = [
    "firebrick", "orangered", "gold1", "darkolivegreen1", "seagreen1",
    "skyblue1", "royalblue1", "slateblue3", "deeppink4"
]

timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(3)

def draw_shape(num_sides):
    angle = 360 / num_sides

    for i in range(num_sides):
        timmy.forward(SIDE_LENGTH)
        timmy.left(angle)

# Draw every regular shape from the 3-sided triangle
# to the 10-sided decagon.
for shape_sides in range(3, 11):
    
    # Set the pen color so each shape stands out.
    timmy.color(COLORS[shape_sides - 3])

    # Draw the shape.
    draw_shape(shape_sides)


screen = Screen()
screen.exitonclick()