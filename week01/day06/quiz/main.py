from question import Question
from data import question_data
from quiz_brain import QuizBrain

# Fill the question_bank with Question objects using question_data.
question_bank = []
for q in question_data:
    new_q = Question(q["text"], q["answer"])
    question_bank.append(new_q)

# Create a QuizBrain object and pass it the question bank.
quiz = QuizBrain(question_bank)

quiz.next_question()
