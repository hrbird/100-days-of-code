# Snake class to manage the snake in the snake game.
from turtle import Turtle, Screen

class Snake:
    def __init__(self):
        # The height/width of each square segment of the snake's body
        self.SEGMENT_SIZE = 20

        # The number of pixels to move at a time.
        self.STEP_DISTANCE = 20

        # A list to hold each turtle segment of the snake's body
        self.segments = []
        self.create_body()

    def create_body(self):
        """Create the 3 starting body segments of the snake."""

        for i in range(3):
            t = Turtle(shape="square")
            t.color("white")
            t.width(self.SEGMENT_SIZE)
            t.penup()
            t.goto(x=(i * -self.SEGMENT_SIZE), y=0)

            self.segments.append(t)

    def move(self):
        """Move the snake forward in its current direction."""

        # Starting with the tail tip, move each segment of the
        # body to where the segment in front of it is.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        # Move the first segment forward.
        self.segments[0].forward(self.STEP_DISTANCE)
