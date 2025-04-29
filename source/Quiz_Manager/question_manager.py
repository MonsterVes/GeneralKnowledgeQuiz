from Database import quiz_db as db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db.engine)

class QuestionManager:
    def __init__(self):
        self.session = Session()

    def add_question(self, question_type, question_text, answer, options=None):
        question_type = input("What type of question would you like to add? \n 1. True/False\n 2. Multiple Choice\n 3. Fill in the blank\n 4. Short Answer")
        question_text = input("Please enter Question text: ")
        if question_type == "1":
            answer = input("Please enter correct answer: ")
            question = db.TrueFalseQuestionDB(text=question_text, answer=answer)
        elif question_type == "2":
            options = list(input("Please enter 4 options separated by a comma: ").split())
            answer = input("Please enter correct answer: ")
            question = db.MultipleChoiceQuestionDB(
                text=question_text, options=options, answer=answer
            )
        elif question_type == "3":
            answer = input("Please enter correct answer: ")
            question = db.FillInQuestionDB(text=question_text, answer=answer)
        elif question_type == "4":
            answer = input("Please enter correct answer: ")
            question = db.ShortAnswerQuestionDB(text=question_text, answer=answer)
        else:
            raise ValueError("Unsupported question type")
        
        self.session.add(question)
        self.session.commit()
        self.session.close()



