# The Question class for the Quiz project.

class QuizBrain:
    """The QuizBrain class, which manages the quiz. 
    It asks the user the questions, checks if their answers 
    are right, and checks if they reached the end of the quiz."""
    def __init__(self, questions_list):
        self.questions_list = questions_list # List of Question objects.
        self.cur_index = 0      # Int current index in the question list.
        self.num_correct = 0    # Int number of correct answers.
        self.num_incorrect = 0  # Int number of incorrect answers.

    def next_question(self):
        """Retrieves the current question from the list.
        Shows the question text and asks for the user's answer."""
        cur_question = self.questions_list[self.cur_index]

        # Ask the user the current question.
        print(f"{self.cur_index + 1}. {cur_question.text}")

        # Get their answer.
        ans = input("> ")

        # TODO: Validate that the answer is either T or F. If not,
        # loop until they enter T or F.

        # Check if the answer is right.
        if ans == cur_question.answer[0]:
            print("Correct!\n")
        else:
            print("Incorrect!\n")

        # Move to the next question.
        self.cur_index += 1