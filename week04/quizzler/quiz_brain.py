# The Question class for the Quiz project.

class QuizBrain:
    """The QuizBrain class, which manages the quiz. 
    It asks the user the questions and checks if their answers are right.
    When all of the questions have been asked, it tells the user their score."""
    def __init__(self, questions_list):
        self.questions_list = questions_list # List of Question objects.
        self.cur_index = 0      # Int current index in the question list.
        self.num_correct = 0    # Int number of correct answers.

    def is_quiz_done(self):
        """Returns True if all the questions have been asked, False if there are
        still more questions to ask."""
        return (self.cur_index >= len(self.questions_list))

    def get_answer(self):
        """Asks user for an answer to a question and keeps looping until the user
        enters either T or F.
        Returns a string, either 'T" or 'F'."""
        ans = ""
        while True:
            ans = input("> ").upper().replace(" ", "")

            if len(ans) == 0 or not (ans[0] == "T" or ans[0] == "F"):
                print(f"Sorry, that is not an acceptable answer. Please enter either T or F.")
            else:
                return ans[0]
    
    def next_question(self):
        """Retrieves the current question from the list.
        Shows the question text and asks for the user's answer."""
        cur_question = self.questions_list[self.cur_index]

        # Ask the user the current question.
        print(f"{self.cur_index + 1}. {cur_question.text}")

        # Get their answer.
        ans = self.get_answer()

        # Check if the answer is right.
        if ans == cur_question.answer[0]:
            print("Correct!\n")
            self.num_correct += 1
        else:
            print("Incorrect!\n")

        # Move to the next question.
        self.cur_index += 1

    def show_quiz(self):
        """Gives the user the quiz and processes each answer."""
        print("\nPop Quiz!\nPlease answer either T or F for each question.\n")

        # Keep asking the user questions until the quiz is finished.
        while not self.is_quiz_done():
            self.next_question()

        # Calculate the final score.
        percent_correct = (self.num_correct / len(self.questions_list)) * 100
        print(f"You got {self.num_correct} out of {len(self.questions_list)} questions correct.")
        print(f"Score: {percent_correct:.2f}%\n\n")

        