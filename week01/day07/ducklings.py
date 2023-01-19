# This program creates a randomized field of ASCII ducklings.
# Inspired by project #22 in the Big Book of Small Python Projects.

import random, shutil, sys, time
from enum import Enum

# Constants
PAUSE = 0.5         # The time in seconds to pause between printing each line
DUCK_DENSITY = 0.05 # The density of ducks on the screen
DUCKLING_WIDTH = 5  # The number of characters each duckling is wide
DUCKLING_HEIGHT = 3 # The number of lines each duckling is tall
NUM_DUCKLINGS_IN_ROW = 10 # The number of ducklings to print on the initial row
LANES_HEIGHT = 100  # How many lines to print for the scrolling duckling lanes

# Get the size of the terminal window.
WINDOW_WIDTH = shutil.get_terminal_size()[0] - 10

# Enums for random duckling features.
class Direction(Enum):
    LEFT = 0
    RIGHT = 1

class Body(Enum):
    CHUBBY = 0
    VERY_CHUBBY = 1

class Mouth(Enum):
    OPEN = 0
    CLOSED = 1

class Wings(Enum):
    OUT = 0
    UP = 1
    DOWN = 2

class Eyes(Enum):
    BEADY = 0
    WIDE = 1
    HAPPY = 2
    ALOOF = 3

class Parts(Enum):
    HEAD = 0
    BODY = 1
    FEET = 2

class Duckling:
    """This class models each duckling."""

    def __init__(self):
        """Create a new duckling with random features."""
        self.direction = random.choice(list(Direction))
        self.body = random.choice(list(Body))
        self.mouth = random.choice(list(Mouth))
        self.wings = random.choice(list(Wings))
        self.eyes = random.choice(list(Eyes))

        if self.body == Body.CHUBBY:
            # Chubby ducklings can only have beady eyes.
            self.eyes = Eyes.BEADY

        self.cur_part = Parts.HEAD

    def print_enums(self):
        """Print the randomly-chosen enum values, for testing."""
        print(f"Features: {self.direction} {self.body} {self.mouth} {self.wings} {self.eyes}")

    def get_eyes_str(self):
        """Returns the string of the duckling's eyes."""
        if self.eyes == Eyes.BEADY:
            if self.body == Body.CHUBBY:
                return '"'
            else:
                return '" '
        elif self.eyes == Eyes.WIDE:
            return "''"
        elif self.eyes == Eyes.HAPPY:
            return "^^"
        elif self.eyes == Eyes.ALOOF:
            return "``"
        else:
            return ""

    def get_mouth_str(self):
        """Returns the string of the duckling's mouth."""
        if self.mouth == Mouth.CLOSED:
            return "="
        else:
            if self.direction == Direction.LEFT:
                return ">"
            else:
                return "<"

    def get_head_str(self):
        """Returns the string of the duckling's entire head.
        Includes the eyes, mouth, and back of head."""
        head_str = ""

        # Get the eyes and mouth.
        eyes_str = self.get_eyes_str()
        mouth_str = self.get_mouth_str()

        # Show the head facing left or right.
        if self.direction == Direction.LEFT:
            head_str += mouth_str + eyes_str + ") "
        else:
            head_str += " (" + eyes_str + mouth_str

        # If the body is chubby, add an extra space so it's the
        # same width as the very chubby ducklings.
        if self.body == Body.CHUBBY:
            head_str += " "

        return head_str

    def get_wings_str(self):
        """Returns the string of the duckling's wings."""
        if self.wings == Wings.UP:
            return "^"
        elif self.wings == Wings.DOWN:
            return "v"
        elif self.wings == Wings.OUT:
            if self.direction == Direction.LEFT:
                return ">"
            else:
                return "<"
        else:
            return ""

    def get_body_space_str(self):
        """Returns the string of the duckling's interior body space."""
        if self.body == Body.CHUBBY:
            return " "
        elif self.body == Body.VERY_CHUBBY:
            return "  "

    def get_body_str(self):
        """Returns the string of the duckling's body.
        Includes the wings and body space."""
        body_str = "("

        wings_str = self.get_wings_str()
        body_space_str = self.get_body_space_str()

        if self.direction == Direction.LEFT:
            body_str += body_space_str + wings_str
        else:
            body_str += wings_str + body_space_str

        body_str += ")"

        # If the body is chubby, add an extra space so it's the
        # same width as the very chubby ducklings.
        if self.body == Body.CHUBBY:
            body_str += " "

        return body_str

    def get_feet_str(self):
        """Returns the string of the duckling's feet."""
        if self.body == Body.CHUBBY:
            return " ^^  "
        elif self.body == Body.VERY_CHUBBY:
            return " ^ ^ "

    def get_next_part(self):
        """Returns the string of the current part of the duckling to display.
        Also sets cur_part to the next body part."""
        if self.cur_part == Parts.HEAD:
            self.cur_part = Parts.BODY
            return self.get_head_str()
        elif self.cur_part == Parts.BODY:
            self.cur_part = Parts.FEET
            return self.get_body_str()
        elif self.cur_part == Parts.FEET:
            self.cur_part = None
            return self.get_feet_str()


def print_duckling_lanes():
    """Print a scrolling screen filled with ducklings."""
    print("Ducklings!\nPress Ctrl-C to quit...")
    time.sleep(2)

    duckling_lanes = [None] * (WINDOW_WIDTH // DUCKLING_WIDTH)

    for i in range(LANES_HEIGHT):

        for lane_num, duckling_obj in enumerate(duckling_lanes):
            
            # See if we should create a duckling in this lane.
            if (duckling_obj == None and random.random() <= DUCK_DENSITY):
                duckling_obj = Duckling()
                duckling_lanes[lane_num] = duckling_obj

            # Draw a duckling if there is one.
            if duckling_obj != None:
                print(duckling_obj.get_next_part(), end="")

                if duckling_obj.cur_part == None:
                    duckling_lanes[lane_num] = None

            else:
                # Draw empty spaces if there is no duckling.
                print(" " * DUCKLING_WIDTH, end="")

        print()
        sys.stdout.flush()
        time.sleep(PAUSE)


def print_duckling_line():
    """Print one row of random ducklings spaced evenly apart."""
    
    # Fill a list with duckling objects.
    ducklings = []
    for d in range(NUM_DUCKLINGS_IN_ROW):
        ducklings.append(Duckling())

    # for d in ducklings:
    #     d.print_enums()

    # Print each line of ducklings.
    space_between = "    "
    for i in range(DUCKLING_HEIGHT):
        row_str = ""
        for d in ducklings:
            row_str += d.get_next_part() + space_between

        print(row_str)


def main():
    print_duckling_line()
    print_duckling_lanes()
    
if __name__ == "__main__":
    main()
