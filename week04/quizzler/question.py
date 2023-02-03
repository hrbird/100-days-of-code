# The Question class for the Quiz project.

class Question:
    """The Question class, which models each quiz question."""
    def __init__(self, text, answer):
        self.text = text        # String question text
        self.answer = answer    # String answer (True or False)

