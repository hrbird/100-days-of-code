# 100 Days Of Code - Week 4
### [Link to Week 4 Files](https://github.com/hrbird/100-days-of-code-2023/tree/master/week04)

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

## Day 23. Upgrading Quizzler Project with Tkinter UI
### February 3, 2023

**Today's Progress**: 
- "100 Days of Python" Udemy class: completed day 34.
- Finished ugrading the Quiz Project from Week 1 to use APIs and a GUI.

**Quizzler Project**:<br />
An upgraded version of the Quiz Project from Week 1. It now gets random trivia questions from an API request to the Open Trivia Database, instead of a small data file. It also creates a GUI to show each question to the user, instead of relying on the console.
- **quizzler/main.py**: The main program that runs the quiz.
- **quizzler/question.py**: The Question class, which models each quiz question.
- **quizzler/quiz_brain.py**: The QuizBrain class, which manages the quiz. It handles the questions and checks if the user's answers are right. When all of the questions have been asked, it calculates the final score.
- **quizzler/ui.py**: The QuizInterface class creates a tkinter GUI for the user to see the questions and choose their answers.
  <br />![img](/screenshots/023_quiz0.jpg) ![img](/screenshots/023_quiz1.jpg)
  <br />![img](/screenshots/023_quiz2.jpg) ![img](/screenshots/023_quiz3.jpg)
  <br />![img](/screenshots/023_quiz4.jpg) ![img](/screenshots/023_quiz5.jpg)
  <br />![img](/screenshots/023_quiz6.jpg)

**Thoughts:** It was a very interesting task to upgrade a project from a few weeks ago and apply more advanced Python functionalities that I've learned recently. The quiz is definitely more fun to play with a GUI and a larger bank of random trivia questions. I also liked learning how to encapsulate the user interface and tkinter parts of the program into their own class, instead of dumping all of that into the main program.

-----

## Day 22. Upgrading Quizzler Project with API Requests
### February 2, 2023

**Today's Progress**: 
- "100 Days of Python" Udemy class: started day 34.
- Started ugrading the Quiz Project from Week 1 to use APIs and a GUI.
- Learned more about API requests, unescaping HTML entities.

**Quizzler Project**:<br />
An upgraded version of the Quiz Project from Week 1. It now gets random trivia questions from an API request to the Open Trivia Database, instead of a data file with only 10 possible questions.
- **quizzler/main.py**: The main program that runs the quiz.
- **quizzler/question.py**: The Question class, which models each quiz question.
- **quizzler/quiz_brain.py**: The QuizBrain class, which manages the quiz. It asks the user the questions and checks if their answers are right. When all of the questions have been asked, it tells the user their score.
  <br />![img](/screenshots/022_quiz0.jpg)
  <br />![img](/screenshots/022_quiz1.jpg)

**Thoughts:** I went on a long day trip to the McCall Winter Festival, so I regretfully did not get much coding done.
