# 100 Days Of Code - Week 3
### [Link to Week 3 Files](https://github.com/hrbird/100-days-of-code-2023/tree/master/week03)

-----

## Day X. Daily Template
### February X, 2023

**Today's Progress**: 
- 

**Programs**:
- **x.py**: X.<br />
  ![img](/screenshots/.jpg)

**Thoughts:** 

-----

## Day 21. APIs
### February 1, 2023

**Today's Progress**: 
- "100 Days of Python" Udemy class: completed day 33.
- Learned about APIs (Application Programming Interfaces) and how to use API requests to get live data from external systems, such as the current location of the International Space Station or the Sunrise/Sunset times for a given location and date.
- Installed and learned how to use the Requests library in Python to handle API requests.
- Also installed the Geopy library to get longitude and latitude coordinates from city names.

**Programs**:
- **api_programs/iss.py**: X.<br />
  ![img](/screenshots/.jpg)
- **api_programs/sunrise_sunset.py**: Shows today's sunrise and sunset times for the given location, as well as the day length in hours.<br />
  ![img](/screenshots/021_sun0.jpg) ![img](/screenshots/021_sun1.jpg)

**Thoughts:** 

-----

## Day 20. React and JSX Libraries
### January 31, 2023

**Today's Progress**: 
- Started the "Learn React for Free" course on Scrimba. Completed Section 1, lessons 1 through 29.
- Learned the basics of how to create HTML elements and add them to the page using React and JSX. Also reviewed HTML elements and CSS styling.
- (Note: Learned about Netlify, a free site to deploy and show React projects on the web. Look into this later.)

**Projects**:
- **react/hello/\***: A simple web page that uses React and JSX to create some HTML elements.<br />
  ![img](/screenshots/020_react_hello.jpg)
- **react/react_facts/\***: A page that shows some facts about React, with some basic CSS styling.<br />
  ![img](/screenshots/020_react_facts.jpg)

**Thoughts:** I decided to spend today looking into React out of curiosity, since I've seen it's a very popular cross-platform library right now. Thankfully, it wasn't as difficult to start getting into as I had feared, and I found a nice free course. It's nice to be able to easily create HTML elements inside different functions and add them to the page without all of the messy node.appendChild() calls in standard JavaScript.

-----

## Day 19. Flash Card Capstone Project
### January 30, 2023

**Today's Progress**: 
- "100 Days of Python" Udemy class: completed day 31.
- Created the Flash Cards Project using pandas and tkinter.

**Flash Cards Project**:<br />A program that shows flashcards to study the most common words in a different language (in this case, Esperanto).<br /><br />It first shows the front of a flashcard with a random word in the language to study. After 3 seconds, it flips to show the back of the card, with the translation of the word in English. The user can click the green checkmark button if they knew the answer, or the red X button if they didn't know it.<br /><br />The words that the user didn't know or didn't see yet are saved to a new file called "words_to_learn.csv". The next time the user runs this program, this file will be used for the flashcards, so the user will only be tested on unknown/unfamiliar words.<br /><br />**Files**:
- **flash_cards/main.py**: The main program
- **flash_cards/images/\***: Folder containing images for the front and back of the flashcard, as well as a green checkmark for right answers and a red X for wrong answers.
- **flash_cards/data/esperanto.csv**: A CSV file containing the full list of Esperanto words and their English translations
- **flash_cards/data/words_to_learn.csv**: A CSV file containing the list of words that the user either didn't know or hasn't seen yet<br />
  ![img](/screenshots/019_flash0.jpg) ![img](/screenshots/019_flash1.jpg)<br />
  ![img](/screenshots/019_flash2.jpg) ![img](/screenshots/019_flash3.jpg)<br />
  ![img](/screenshots/019_flash4.jpg) ![img](/screenshots/019_flash5.jpg)


**Thoughts:** This was a fun one! I was able to do 95% of the code myself before watching the walkthrough videos. I had to search how to get pandas to output data to a CSV file without creating an index column, as well as how to get the window.after() timer working correctly, but other than that I had no issues.

-----

## Day 18. Exception Handling and JSON
### January 29, 2023

**Today's Progress**: 
- "100 Days of Python" Udemy class: completed day 30.
- Learned about error handling and catching exceptions in Python with the try-except-else-finally clause. 
- Went back to the Nato Alphabet program from week 2 to add exception handling.
- Updated yesterday's Password Manager program to use a JSON file for data storage, exception handling, and a website Search button.

**Programs**:
- **small_python_projects/exception_handling.py**: A program that demonstrates how to handle FileNotFound exceptions/errors whenever you open a file in Python.<br />
  ![img](/screenshots/018_filenotfound0.jpg) ![img](/screenshots/018_filenotfound1.jpg)
- **small_python_projects/index_error.py**: A program that demonstrates how to handle IndexError exceptions/errors.
- **week02/nato_alphabet/main.py**: Went back to the nato_alphabet project from week 2 and added exception handling for FileNotFoundError exceptions (when opening the nato_alphabet.csv file) and KeyError exceptions (if a given alphabetic letter was not found in the dictionary, such as letters with accent symbols).<br />
  ![img](/screenshots/018_nato.jpg)

**Password Manager Project**:
- **password_manager/main.py**: Updated the program to store the account data in a JSON file, instead of a txt file. Also added exception handling when reading and writing from the file so there will be no FileNotFoundErrors. I also added a Search button that will search the data file to see if the user has already stored a password for a website. If so, it shows a message with the saved account information.
- **password_manager/logo.png**: "MyPass" image that is displayed on the screen.
- **password_manager/data.txt**: Stores the saved account data. Each line is comma-delineated and has the website name, email/username, and password for each account.<br />
  ![img](/screenshots/018_password0.jpg) ![img](/screenshots/018_password1.jpg)

**Thoughts:** I had been using my own ways of trying to catch and prevent errors by cleaning/validating input, but using a try-except clause is so much better. I will try my best to use this in all projects from now on!

-----

## Day 17. Tkinter and Pandas: Storm Events and Password Manager Projects
### January 28, 2023

**Today's Progress**: 
- "100 Days of Python" Udemy class: completed day 29.
- Continued playing around with using pandas and dictionaries to group and summarize the data in StormEvents_2022.csv.

**Storm and Extreme Weather Events Project**:
- **weather_events/storms_2022.py**: A program that shows storm and extreme weather event data for 2022. It groups the data by the event type (such as Tornado, Excessive Heat, Flood, Wildfire, Tsunami, etc.), then by state. For each event type, it displays a table showing each state's total number of events, injuries, and deaths for 2022. The rows are sorted from the most events to the fewest events.<br />
  ![img](/screenshots/017_storms0.jpg) ![img](/screenshots/017_storms1.jpg)<br /> 
  ![img](/screenshots/017_storms2.jpg) ![img](/screenshots/017_storms3.jpg)

**Password Manager Project**:
- **password_manager/main.py**: Program that stores usernames and passwords for various sites. It shows a form for the user to enter a new set of account information: the name of the website, the email/username, and the password. There is a button to generate a random secure password, if needed. If the user clicks the Add button at the bottom, this account information is written to a text file.
- **password_manager/logo.png**: "MyPass" image that is displayed on the screen.
- **password_manager/data.txt**: Stores the saved account data. Each line is comma-delineated and has the website name, email/username, and password for each account.<br />
  ![img](/screenshots/017_password0.jpg) ![img](/screenshots/017_password1.jpg)<br />
  ![img](/screenshots/017_password2.jpg) ![img](/screenshots/017_password3.jpg)<br />
  ![img](/screenshots/017_password4.jpg) ![img](/screenshots/017_password5.jpg) 

**Thoughts:** Getting faster and more comfortable with these libraries with every project!

-----

## Day 16. Tkinter and Pandas: Pomodoro Timer and Tornado Data Projects
### January 27, 2023

**Today's Progress**: 
- "100 Days of Python" Udemy class: completed day 28.
- Learned more about the tkinter library, including how to create canvas widgets to display images and write text. Also learned how to create a countdown mechanism that updates a timer on the screen every second.

**Pomodoro Project**: A program that shows a Pomodoro Timer. (The pomodoro method is helpful for working on long projects. It breaks up the day into 25-minute periods of work, followed by a short 5-minute break.)
- **main.py**: This program uses the tkinter library to create a GUI. It counts down the time left in the current pomodoro or break. It also shows a checkmark at the bottom for each completed pomodoro.<br />
- **tomato.png**: Tomato image to display on the screen.<br />
  ![img](/screenshots/016_pomo0.jpg) ![img](/screenshots/016_pomo1.jpg)<br />
  ![img](/screenshots/016_pomo2.jpg) ![img](/screenshots/016_pomo3.jpg)<br />

**Tornado Data Project**: A program that uses pandas to read a very large dataset of the extreme weather events in the US in 2022. This program creates a data showing the summary data for tornadoes that happened in each US state in 2022.
- **weather_events/tornadoes_2022.py**:The main program, which reads in data from a CSV, and selects specific rows for tornado events. For each state, it counts the total number of tornadoes, the number of tornadoes for each Fujita Scale category, the total injuries (direct and indirect), and the total deaths (direct and indirect). This data is displayed in a neat table, with rows sorted from the states with the highest number of tornadoes to the lowest.<br />
- **weather_events/StormEvents_2022.csv**: Storm event data for 2022 in the United States.<br />
  ![img](/screenshots/016_tornadoes.jpg)

**Thoughts:** Getting more familiar with both tkinter and pandas. The pomodoro project was an exercise from the Udemy class, but the tornado project was something I came up with, just out of curiosity. I might see if I can play with this more tomorrow.

-----

## Day 15. Tkinter Widgets and Grid Layout
### January 26, 2023

**Today's Progress**: 
- "100 Days of Python" Udemy class: completed day 27.
- Continued learning how to create many different kinds of widgets in the tkinter library and how to get/set values for each type. I also learned how to use the grid layout (instead of the pack layout) to better control where each widget will appear on the screen.

**Programs**:
- **tkinter_programs/tkinter_widgets.py**: Demonstrates several types of tkinter widgets you can create, including labels, buttons, single-line and multi-line text entry boxes, spinboxes, scales, checkbuttons, radiobuttons, and listboxes. Also demonstrates how to bind functions to widgets and get each kind of widget's current value.<br />
  ![img](/screenshots/015_widgets.jpg)
- **tkinter_programs/tkinter_grid.py**: This program is mostly the same as tkinter_widgets, except it uses the grid layout, instead of simply packing all of the widgets onto the screen.<br />
  ![img](/screenshots/015_grid.jpg)
- **tkinter_programs/tkinter_miles_km.py**: This program converts miles to kilometers. When the user enters a float number of miles into a text entry box and clicks the Calculate button, the equivalent number of kilometers is written in the km label.<br />
  ![img](/screenshots/015_miles_km.jpg)

**Thoughts:** I'm enjoying being able to create simple GUI applications, though I do agree that the default appearance of the window/widgets are a little outdated. I like that the grid layout makes it easier to create rows and columns of widgets that automatically resize themselves and line up neatly. Looking forward to learning more!
