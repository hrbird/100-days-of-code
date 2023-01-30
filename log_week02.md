# 100 Days Of Code - Week 2
### [Link to Week 2 Files](https://github.com/hrbird/100-days-of-code-2023/tree/master/week02)

-----

## Day 14. Tkinter Library, *Args, and **Kwargs
### January 25, 2023

**Today's Progress**: 
- "100 Days of Python" Udemy class: started day 27.
- Learned about the built-in tkinter library, which can create GUI applications that work on Windows, MacOS, and Linux. Today, I learned how to create a window, set basic properties, create labels, add widgets to the screen, create buttons, and have buttons trigger a function when clicked.
- Also learned about default arguments, positional arguments, \*args (allows any number of positional arguments), and \*\*kwargs.

**Programs**:
- **small_python_projects/args_kwargs.py**: Demonstrates how to use \*args and \*\*kwargs function arguments.<br />
  ![img](/screenshots/014_args_kwargs.jpg)
- **small_python_projects/tkinter_hello.py**: First tkinter program that displays a "Hello, world." label and a "Click me!" button.<br />
  ![img](/screenshots/014_tkinter_hello.jpg) ![img](/screenshots/014_tkinter_hello2.jpg)

**Thoughts:** Took a daytrip to spend the day hiking up sand dunes, so I didn't do much coding today. I'll get back on it tomorrow!

-----

## Day 13. List and Dictionary Comprehension
### January 24, 2023

**Today's Progress**: 
- "100 Days of Python" Udemy class: completed day 26.
- Learned list comprehension syntax for lists, strings, and ranges. Also learned dictionary comprehension syntax.

**Programs**:
- **list_comprehension.py**: Demonstrates list comprehension syntax for lists, strings, and ranges, and dictionaries.<br />
  ![img](/screenshots/013_list_comp.jpg)
- **dict_comprehension.py**: Demonstrates dictionary comprehension syntax. Creates a dictionary of students and generates random test scores for them. Then gets a dictionary of the students with passing scores.<br />
  ![img](/screenshots/013_dict_comp.jpg)

**NATO Alphabet Project**: Spells out a given word or message in NATO Alphabet codewords.
- **main.py**: Program that prompts the user to enter a word or message in English. The program loads NATO codewords for each letter from a CSV file into a pandas dataframe. Then it converts each letter in the user's message into NATO codewords and prints the final message.
- **nato_alphabet.csv**: CSV file with a row for each alphabetic letter and its corresponding NATO phonetic alphabet word.<br />
  ![img](/screenshots/013_nato.jpg)

**Thoughts:** I will have to practice more to get comfortable with this syntax, since it is very dense compared to using other methods. It is nice, however, to be able to do several steps in one line of code, instead of 5.

-----

## Day 12. Reading CSV Files and Pandas Library
### January 23, 2023

**Today's Progress**: 
- "100 Days of Python" Udemy class: completed day 25.
- Learned how to set up and activate a virtual environment in VS Code so I can install and use different Python packages. (If I have to do it again, the first commands were "python3 -m venv venv" and "venv\Scripts\activate". Then, to install a specific package, use pip like so: "pip3 install pandas".)
- Started learning how to use the pandas library for reading, storing, and working with data in DataFrames and Series. Learned how to find the min/max/sum/count/average of values, how to group data, how to select rows based on conditions, and how to read CSV files into DataFrames (and vice versa).

**Weather Data**:
- **weather/weather.csv**: A CSV file with one row per date. Columns: date, day, avg_temp, and condition.
- **weather/csv_reader.py**: Opens the weather.csv file and reads the data into the program using the csv library. Specifically, this program gets the average temperature for each day in the file and calculates the overall average temperature.
- **weather/pandas_csv.py**: A program that uses the pandas library to read data from the weather.csv file. It demonstrates a variety of ways you can use pandas for data manipulation.<br />
  ![img](/screenshots/012_weather.jpg)

**Squirrel Data Project**:
- **squirrel_census/squirrel_data.csv**: A CSV file with data from a census of squirrels in Central Park, New York City, in 2018. There is one row per squirrel sighting. Some columns: X and Y geographical coordinates, Unique Squirrel ID, Shift (AM/PM) Date, Age, and Primary Fur Color.
- **squirrel_census/squirrels.py**: Opens the squirrel_data.csv file and reads the data into the program using pandas. Specifically, this program counts the number of squirrels for each primary fur color.<br />
  ![img](/screenshots/012_squirrels.jpg)

**US States Guessing Game Project**: A game to guess the names of all 50 states in the US. Uses both the turtle graphics library and the pandas library.
- **us_states/50_states.csv**: A CSV file with data of the 50 US states and X, Y coordinates for the location of the state on the blank map image.
- **us_states/blank_states_img.gif**: A blank map of the 50 US states.
- **us_states/main.py**: Opens the 50_states.csv file and reads the data into the program using pandas. Then uses turtle to create a game for the player to guess the 50 state names. The game shows a blank map of the US and prompts the user to enter state names. Each time the player correctly guesses a state name, it appears on the map. The current score is shown at the top of the screen. The game congratulates the player if they guess all 50 states.<br />
  ![img](/screenshots/012_states0.jpg) ![img](/screenshots/012_states1.jpg) ![img](/screenshots/012_states3.jpg)

**Thoughts:** The pandas library is a little intimidating, but playing around with it while reading the documentation helped me start to understand how to use it. It's definitely a lot easier than trying to use the basic csv_reader in Python!

-----

## Day 11. Pong Game and Turtle Crossing Game Projects
### January 22, 2023

**Today's Progress**: 
- "100 Days of Python" Udemy class: completed days 22-24.
- Gained more experience with using the Turtle library to make games by creating Pong and a Turtle Crossing game in Python.

**Pong Game Project**: The classic game of Pong, in two players control paddles to hit a ball back and forth across the screen.
- **main.py**: Main program. Creates the custom objects and handles event listeners for the user pressing the keys. The left paddle is controlled by the W/S keys, and the right paddle is controlled by the up/down arrow keys. The main function also runs the main game loop and detects collision between the ball and the paddles or the edges of the screen.
- **paddle.py**: Paddle class to handle the paddles on either side of the screen.
- **ball.py**: Ball class to handle the ball that moves across the screen.
- **scoreboard.py**: A class to keep track of the left and right players' scores and display them on the screen.<br />
![img](/screenshots/011_pong1.jpg) ![img](/screenshots/011_pong2.jpg)<br />
![img](/screenshots/011_pong3.jpg) ![img](/screenshots/011_pong4.jpg)

**Turtle Crossing Game Project**: A game in which the player controls a turtle that is trying to cross a road and dodge the moving cars.
- **main.py**: Main program. Creates the custom objects and handles event listeners for the user pressing the Up key to move the turtle. The main function also runs the main game loop and detects collision between the turtle and the cars or the edges of the screen. When the turtle reaches the other side, it goes to the next level, in which the cars move even faster.
- **player.py**: Player class to control the player turtle character that the player moves across the street
- **car.py**: Car class to handle each car that appears on the screen. Its color and starting y-position are randomly chosen.
- **car_manager.py**: CarManager class to create and handle all of the cars together.
- **scoreboard.py**: Scoreboard class to keep track of the current level and display it on the screen.<br />
![img](/screenshots/011_crossing0.jpg) ![img](/screenshots/011_crossing1.jpg)<br />
![img](/screenshots/011_crossing2.jpg) ![img](/screenshots/011_crossing3.jpg)

**Thoughts:** Two more recreations of classic video games. It's amazing to be able to make these with just a few hours of work. I feel like I'm getting the hang of using Turtle and custom classes to implement game logic.

-----

## Day 10. Turtle Graphics and Snake Game Project
### January 21, 2023

**Today's Progress**: 
- Continued working through "100 Days of Python" Udemy class. Completed days 19-21.
- Learned more about the Turtle library, including using keypress event listeners, multiple turtle instances, the turtle XY coordinate system, prompting for user input, and writing text to the screen.
- Also learned about class inheritance in Python.
- Started working on the project to make a Snake game in Turtle.

**Programs**:
- **inheritance.py**: A quick program exploring how class inheritance works in Python.
- **turtle_listen.py**: A turtle walks forward ten steps every time the user presses the space bar.
- **turtle_sketch.py**: Lets the user draw an image on the screen by pressing the WASD keys, like an etch-a-sketch.<br />
  ![img](/screenshots/010_sketch.jpg)
- **turtle_race.py**: Six turtles race across the screen, at random speeds.<br />
  ![img](/screenshots/010_race.jpg)<br />
  ![img](/screenshots/010_race_3.jpg)

**Snake Game Project**:
- **main.py**: Main function. Creates the snake object and handles event listeners for the user pressing arrow keys. It also runs the main game loop and detects collision between the snake head and food, the edges of the screen, and its own tail.
- **snake.py**: A class to handle the snake object in the game, including creating its body segments, handling its movement, and changing its direction.
- **food.py**: A class to handle the food that the snake eats. The food appears in a random location on the screen, and if the head of the snake eats it, the food moves to a different random location.
- **scoreboard.py**: A class to keep track of the score and display it on the screen. It also displays "GAME OVER" when the player loses.<br />
  ![img](/screenshots/010_snake_0.jpg) ![img](/screenshots/010_snake_1.jpg)<br />![img](/screenshots/010_snake_2.jpg) ![img](/screenshots/010_snake_3.jpg)

**Thoughts:** This was a really, really fun project! I'm excited to be able to fully recreate such a well-known game with just a few Python classes.

-----

## Day 9. Numeral Systems, String Formatting, Turtle Graphics
### January 20, 2023

**Today's Progress**: 
- Continued working through "100 Days of Python" Udemy class. Completed day 18.
- Learned conversion into different numeral systems (binary, hex, octal) and more f-string formatting (alignment, padding). Also learned more about using the Turtle library.

**Programs**:
- **numeral_systems.py**: Counts to a given number in different numeral systems: decimal (base 10), hexadecimal (base 16), and binary (base 2).<br />
  ![img](/screenshots/009_numeral.jpg)
- **blackjack.py**: I went back to day 3's blackjack program and changed the way the cards are presented so they look more like cards. I also added docstrings for the classes and functions.<br />
  ![img](/screenshots/009_blackjack_1.jpg)
- **turtle_square.py**: Draws a basic square in Turtle.<br />
  ![img](/screenshots/009_turtle_square.jpg)
- **turtle_dashed.py**: Draws a dashed line in Turtle.<br />
  ![img](/screenshots/009_turtle_dashed.jpg)
- **turtle_shapes.py**: Draws a variety of overlapping shapes in turtle. Draws every regular shape from the 3-sided triangle to the 10-sided decagon.<br />
  ![img](/screenshots/009_turtle_shapes.jpg)
- **turtle_random_walk.py**: Draws a random path, switching colors and changing speeds randomly.<br />
  ![img](/screenshots/009_turtle_random_1.jpg)

**Thoughts:** Decided to reformat this log to put the days in reverse-chronological order. I also added screenshots of each project. Having fun with Turtle!

-----

## Day 8. Reading From Text Files, String Formatting
### January 19, 2023

**Today's Progress**: 
- Did a project from the "Big Book of Small Python Projects" by Al Sweigart. I tried to play around with the code by creating a class and moving the game logic into smaller encapsulated functions, instead of long, global functions. I also added input validation.
- Learned how to open txt files and read their contents into a list in Python. Also learned some more complicated string formatting and new randomization functions (choice, sample, etc.).

**Programs**:
- **hacking_game.py**: Hacking game inspired by the computer-hacking minigame in Fallout: New Vegas.<br />
  ![img](/screenshots/008_hack_1.JPG)

**Thoughts:** The hacking game was my favorite minigame in FNV, so it was a lot of fun to be able to mimic it in Python. I'm learning that there's a lot you can do just with ASCII in the terminal.