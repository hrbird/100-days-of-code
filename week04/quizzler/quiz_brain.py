# The QuizBrain class for the Quiz project.

class QuizBrain:
    """The QuizBrain class, which manages the quiz. 
    It handles the questions and checks if the user's answers are right. 
    When all of the questions have been asked, it calculates the final score."""
    def __init__(self, questions_list):
        self.questions_list = questions_list # List of Question objects.
        self.cur_index = 0      # Int current index in the question list.
        self.num_correct = 0    # Int number of correct answers.


    def is_quiz_done(self) -> bool:
        """Returns True if all the questions have been asked, False if there are
        still more questions to ask."""
        return (self.cur_index >= len(self.questions_list))


    def get_cur_question_num(self) -> int:
        """Returns the current question number (numbers start at 1, not 0)."""
        return self.cur_index + 1


    def get_cur_question(self) -> str:
        """Retrieves the current question text from the list."""
        cur_question = self.questions_list[self.cur_index]

        # Ask the user the current question.
        print(f"{self.cur_index + 1}. {cur_question.text}")

        return cur_question.text

    def go_to_next_question(self):
        """Move the question index to point to the next question in the list."""
        self.cur_index += 1

    def check_answer(self, user_answer: bool):
        """Check whether the user chose the correct answer for the correct question.

        Args:
            user_answer (bool): the answer the user clicked on (True or False)

        Returns True if the user answered correctly, or False if they answered wrong.
        """
        # Check if the answer is right.
        cur_question = self.questions_list[self.cur_index]

        if str(user_answer) == cur_question.answer:
            print("Correct!\n")
            self.num_correct += 1
            return True
        else:
            print("Incorrect!\n")
            return False
        

    def get_cur_score_str(self) -> str:
        """Returns the current quiz score as the number of correct questions 
        out of total questions."""
        return f"{self.num_correct} / {len(self.questions_list)}"


    def get_final_score_str(self) -> str:
        """Returns the current quiz score as the number of correct questions 
        out of total questions, as well as the percentage."""

        percentage = (self.num_correct / len(self.questions_list)) * 100
        score_str = f"Final Score:\n{self.num_correct} / {len(self.questions_list)} ({percentage} %)"

        return score_str


        