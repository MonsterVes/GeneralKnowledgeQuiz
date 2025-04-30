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
                " 1. General\n"
                " 2. Science\n" 
                " 3. Geography\n" 
                "Your choice (1, 2 or 3): ").strip()
            if category not in ["1", "2", "3"]:
                print("Invalid category choice. Please try again.")
                return
            
            question_type = input(
                "What type of question would you like to add?\n"
                " 1. True/False\n"
                " 2. Multiple Choice\n" 
                " 3. Fill in the blank\n" 
                " 4. Short Answer\n"
                "Your choice(1, 2, 3 or 4): ").strip()
            if question_type not in ["1", "2", "3", "4"]:
                print("Invalid question type choice. Please try again.")
                return
            new_question_text = input("Please enter Question text: ").strip()
            if not new_question_text:
                print("Question text cannot be empty")
                return
            new_question = db.QuestionDB(question_text = new_question_text, question_type = question_type, category = category)
            
            self.session.add(new_question)
            self.session.commit()


            if question_type == "1":
                answer = input("Please enter correct answer (True/False): ").strip().lower()
                if answer not in ["true", "false"]:
                    print("Answer must be True or False")
                    return
                question = db.TrueFalseQuestionDB(answer=answer, question=new_question)

            elif question_type == "2":
                options = []
                for letter in ["A", "B", "C", "D"]:
                    option = input(f"Option {letter}: ").strip()
                    if not option:
                        print("Option cannot be empty")
                        return
                    options.append(option)

                answer = input("Please enter correct Option (A, B, C or D): ").strip().lower()
                if answer not in ["A", "B", "C", "D"]:
                    print("Answer must be A, B, C or D")
                    return
                question = db.MultipleChoiceQuestionDB(                    
                    a = options[0],
                    b = options[1],
                    c = options[2],
                    d = options[3],
                    answer = answer,
                    question = new_question
                )
            elif question_type == "3":
                answer = input("Please enter correct answer: ")
                if not answer:
                    print("Answer cannot be empty")
                    return
                question = db.FillInQuestionDB(answer = answer, question = new_question)
            
            elif question_type == "4":
                answer = input("Please enter correct answer: ")
                if not answer:
                    print("Answer cannot be empty")
                    return
                question = db.ShortAnswerQuestionDB(
                    answer = answer, question = new_question)
            else:
                raise ValueError("Unsupported question type")

            self.session.add(new_question)
            self.session.add(question)
            self.session.commit()
            print("Question added successfully!")
        except Exception as e:
            self.session.rollback()
            print(f"Error adding question.{e}")
            self.session.close()
        finally:
            self.session.close()



