from question import Question, CATEGORY_DATA
from quiz_brain import QuizBrain
from ui import QuizInterface
import requests
import html

ASCII_ART = """
  ______      __    __   __   ________   ________   __       _______ .______      
 /  __  \    |  |  |  | |  | |       /  |       /  |  |     |   ____||   _  \     
|  |  |  |   |  |  |  | |  | `---/  /   `---/  /   |  |     |  |__   |  |_)  |    
|  |  |  |   |  |  |  | |  |    /  /       /  /    |  |     |   __|  |      /     
|  `--'  '--.|  `--'  | |  |   /  /----.  /  /----.|  `----.|  |____ |  |\  \----.
 \_____\_____\\______/  |__|  /________| /________||_______||_______|| _| `._____|
                                                                                  
"""

def get_questions():
    """Get trivia question data from the Open Trivia Database.
    Returns a list of Question objects."""

    # Parameters for the API.
    # Modify these if you would like longer/shorter quizzes in different categories.
    parameters = {
        "amount": 10,
        "type": "boolean",
        "category": CATEGORY_DATA["Science & Nature"]
    }

    # Send an API request to the Open Trivia Database for 10 True/False questions.
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)

    # If there was an API error, print it to the console.
    response.raise_for_status()

    # Make an empty question bank.
    question_bank = []

    # Fill the question bank with Question objects using the API data.
    data = response.json()["results"]
    for q in data:

        # Clean the questions so that quotations and special characters appear correctly.
        question = html.unescape(q["question"])
        answer = q["correct_answer"]
        
        question_bank.append(Question(question, answer))

    return question_bank

def main():
    print(ASCII_ART)

    # Get a new question bank of random trivia questions.
    question_bank = get_questions()

    # Create a QuizBrain object and pass it the question bank.
    quiz_brain = QuizBrain(question_bank)

    # Create the GUI.
    quiz_ui = QuizInterface(quiz_brain)

    # Give the user the quiz.
    #quiz.show_quiz()

if __name__ == "__main__":
    main()

