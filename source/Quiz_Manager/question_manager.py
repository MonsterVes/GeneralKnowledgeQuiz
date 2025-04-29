from source.Database import quiz_db as db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db.engine)

class QuestionManager:
    def __init__(self):
        self.session = Session()

    def add_question(self):
        try:
            category = input(
                "Please enter category for the question\n"
                " 1. General knowledge\n"
                " 2. Natural sciences\n" 
                " 3. Geography\n" 
                "Your choice: ")
            question_type = input(
                "What type of question would you like to add?\n"
                " 1. True/False\n"
                " 2. Multiple Choice\n" 
                " 3. Fill in the blank\n" 
                " 4. Short Answer\n"
                "Your choice: ")
            question_text = input("Please enter Question text: ").strip()
            if not question_text:
                print("Question text cannot be empty")
                return
            if question_type == "1":
                answer = input("Please enter correct answer (True/False): ").strip()
                if answer not in ["true", "false"]:
                    print("Answer must be True or False")
                    return
                question = db.TrueFalseQuestionDB(
                    text=question_text, 
                    answer=answer, 
                    question_type = "TrueFalse", 
                    category = category)

            elif question_type == "2":
                options = []
                for letter in ["A", "B", "C", "D"]:
                    option = input(f"Oprion {letter}: ").strip()
                    if not option:
                        print("Option cannot be empty")
                        return
                options.append(option)

                answer = input("Please enter correct Option (A, B, C or D): ")
                if answer not in ["A", "B", "C", "D"]:
                    print("Answer must be A, B, C or D")
                    return
                question = db.MultipleChoiceQuestionDB(
                    text=question_text,                     
                    a=options[0],
                    b=options[1],
                    c=options[2],
                    d=options[3],
                    answer=answer,
                    question_type = "MultipleChice", 
                    category = category
                )
            elif question_type == "3":
                answer = input("Please enter correct answer: ")
                if not answer:
                    print("Answer cannot be empty")
                    return
                question = db.FillInQuestionDB(
                    text=question_text, 
                    answer=answer,
                    question_type = "FillIn", 
                    category = category)
            elif question_type == "4":
                answer = input("Please enter correct answer: ")
                if not answer:
                    print("Answer cannot be empty")
                    return
                question = db.ShortAnswerQuestionDB(
                    text=question_text, 
                    answer=answer,
                    question_type = "ShortAnswer", 
                    category = category)
            else:
                raise ValueError("Unsupported question type")

            self.session.add(question)
            self.session.commit()
            print("Question added successfully!")
        except Exception as e:
            self.session.rollback()
            print("Error adding question.")
        finally:
            self.session.close()



