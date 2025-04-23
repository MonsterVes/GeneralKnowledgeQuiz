class Question:
    def __init__(self, question_text):
        self.question_text = question_text

    def __str__(self):
        return f"{self.question_text}"

class TrueFalseQuestion(Question):
    def __init__(self, question_text, answer):
        super().__init__(question_text)
        self.answer = answer

class MultipleChoiceQuestion(Question):
    def __init__(self, question_text, options, answer):
        super().__init__(question_text)
        self.options = options
        self.answer = answer

class FillInQuestion(Question):
    def __init__(self, question_text, answer):
        super().__init__(question_text)
        self.answer = answer

class ShortAnswerQuestion(Question):
    def __init__(self, question_text, answer):
        super().__init__(question_text)
        self.answer = answer


