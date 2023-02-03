from question import Question
from data import question_data
from quiz_brain import QuizBrain
import requests

def get_questions():
    """Get trivia question data from the Open Trivia Database.
    Returns a list of Question objects."""

    # Send an API request to the Open Trivia Database for 10 True/False questions.
    response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")

    # If there was an API error, print it to the console.
    response.raise_for_status()

    # Make an empty question bank.
    question_bank = []

    # Fill the question bank with Question objects using the API data.
    data = response.json()["results"]
    for q in data:

        # Clean the questions so that quotations and special characters appear correctly.
        question = q["question"].replace("&quot;", "\"").replace("&#039;", "'").replace("&eacute;", "é")
        answer = q["correct_answer"]
        
        new_q = Question(question, answer)
        question_bank.append(new_q)

    return question_bank

def main():
    # Get a new question bank of random trivia questions.
    question_bank = get_questions()

    # Create a QuizBrain object and pass it the question bank.
    quiz = QuizBrain(question_bank)

    # Give the user the quiz.
    quiz.show_quiz()

if __name__ == "__main__":
    main()
