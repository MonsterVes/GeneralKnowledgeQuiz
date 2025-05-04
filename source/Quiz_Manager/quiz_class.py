import random
from source.Database import quiz_db as qdb
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func


Session = sessionmaker(bind = qdb.engine)


class Quiz:
    def __init__(self, category, difficulty, question_limit):
        self.session = Session()
        self.category = category
        self.difficulty = difficulty
        self.question_limit = question_limit
        self.questions = []
        self.score = 0

    def load_questions(self):
        try:
            questions_per_type = self.question_limit // 4
            all_questions = []

            if self.category == 0:
                for question_type in ["1", "2", "3", "4"]:
                    questions = (
                        self.session.query(qdb.QuestionDB)
                        .filter_by(difficulty = self.difficulty,question_type = question_type)
                        .order_by(func.random())
                        .limit(questions_per_type)
                        .all()
                        )
                    all_questions.extend(questions)
            else:
                for question_type in ["1", "2", "3", "4"]:
                    questions = (
                        self.session.query(qdb.QuestionDB)
                        .filter_by(
                            category_id = self.category, 
                            difficulty = self.difficulty, 
                            question_type=question_type)
                        .order_by(func.random())
                        .limit(questions_per_type)
                        .all()
                        )
                    all_questions.extend(questions)

            if len(all_questions) < self.question_limit:
                print(f"Not enough questions in the database. Only {len(all_questions)} questions found.")
                return False
        
            selected_questions = random.sample(all_questions, self.question_limit)
            self.questions = sorted(selected_questions, key = lambda q: q.question_type)
            return True
        except Exception as e:
            print(f"Error loading questions:\n{e}")
            return False     
               

    def print_questions(self, question):
        print("~-"*6)
        print(f"{question.question_text}")
        if question.question_type == "1":
            while True:
                user_answer = input("Enter True or False: ").strip().lower()
                if user_answer in ["true", "false"]:
                    break
                print("Answer must be True or False. Please try again.")
            correct_answer = question.true_false.answer.lower()
            return user_answer == correct_answer
        elif question.question_type == "2":
            print(f"A. {question.multiple_choice.a}") 
            print(f"B. {question.multiple_choice.b}") 
            print(f"C. {question.multiple_choice.c}") 
            print(f"D. {question.multiple_choice.d}") 
            while True:
                user_answer = input("Enter A, B, C, or D: ").strip().lower()
                if user_answer in ["a", "b", "c", "d"]:
                    break
                print("Answer must be A, B, C, or D. Please try again.")
            correct_answer = question.multiple_choice.answer.lower()
            return user_answer == correct_answer
        elif question.question_type == "3":
            user_answer = input("Fill in the blank: ").strip().lower()
            correct_answer = question.fill_in.answer.lower()
            return user_answer == correct_answer
        elif question.question_type == "4": 
            user_answer = input("Enter your answer: ").strip().lower()
            correct_answer = question.short_answer.answer.lower()
            return user_answer == correct_answer
        
    def start_quiz(self):
        try:
            for index, question in enumerate(self.questions, start = 1):
                print(f"\nQuestion No. {index}")
                correct_answer = self.print_questions(question)
                if correct_answer:
                    self.score +=1
                    print(f"Correct! Your score: {self.score}.")
                    print("~-"*6)
                else:
                    if question.question_type == "1":
                        correct_answer = question.true_false.answer
                    elif question.question_type == "2":
                        correct_answer = question.multiple_choice.answer.upper()
                    elif question.question_type == "3":
                        correct_answer = question.fill_in.answer
                    elif question.question_type == "4":
                        correct_answer = question.short_answer.answer
                    print(f"Wrong! The correct answer is: {correct_answer.title()}")
                    print("~-"*6)

            print(  "\nYou have answered all questions!\n"
                    f"Your final score is {self.score} out of {self.question_limit}."
                    )
            self.session.close()

        except Exception as e:
            print(f"Error starting quiz! {e}")
            self.session.close()
        
        
