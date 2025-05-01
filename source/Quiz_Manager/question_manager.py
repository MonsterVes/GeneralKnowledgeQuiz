from source.Database import quiz_db as db
from sqlalchemy.orm import sessionmaker
import re


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
            
            difficulty = input(
                "What is the difficulty of the question?\n"
                " 1. Easy\n"
                " 2. Medium\n" 
                " 3. Hard\n" 
                "Your choice(1, 2 or 3): ").strip()
            if difficulty not in ["1", "2", "3"]:
                print("Invalid question difficulty. Please try again.")
                return           
            if question_type == "3":
                print("Question must contain 3 to 5 consecutive underscores (____) for the 'Fill in the blank' field\n")
            new_question_text = input("Please enter Question text: ").strip()
            if not new_question_text:
                print("Question text cannot be empty")
                return
            new_question = db.QuestionDB(question_text = new_question_text, question_type = question_type, category = category, difficulty = difficulty)
            
            self.session.add(new_question)
            self.session.commit()


            if question_type == "1":
                answer = input("Please enter correct answer (True/False): ").strip().lower()
                if answer not in ["true", "false"]:
                    print("Answer must be True or False")
                    self.session.delete(new_question)
                    self.session.commit()
                    return
                question = db.TrueFalseQuestionDB(answer=answer, question=new_question)

            elif question_type == "2":
                options = []
                for letter in ["A", "B", "C", "D"]:
                    option = input(f"Option {letter}: ").strip()
                    if not option:
                        print("Option cannot be empty")
                        self.session.delete(new_question)
                        self.session.commit()
                        return
                    options.append(option)

                answer = input("Please enter correct Option (A, B, C or D): ").strip().lower()
                if answer not in ["a", "b", "c", "d"]:
                    print("Answer must be A, B, C or D")
                    self.session.delete(new_question)
                    self.session.commit()                    
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
                if not re.search(r"_{3,5}", new_question_text):
                    print("Invalid fill-in-the-blank question. It must contain 3 to 5 consecutive underscores.")
                    self.session.delete(new_question)
                    self.session.commit()
                answer = input("Please enter correct answer: ").strip().lower()
                if not answer:
                    print("Answer cannot be empty")
                    self.session.delete(new_question)
                    self.session.commit()
                    return
                question = db.FillInQuestionDB(answer = answer, question = new_question)
            
            elif question_type == "4":
                answer = input("Please enter correct answer: ")
                if not answer:
                    print("Answer cannot be empty")
                    self.session.delete(new_question)
                    self.session.commit()                    
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



