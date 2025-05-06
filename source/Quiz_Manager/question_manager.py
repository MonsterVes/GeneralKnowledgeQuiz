from source.Database import quiz_db as db
from sqlalchemy.orm import sessionmaker
import re


Session = sessionmaker(bind=db.engine)

class QuestionManager:
    def __init__(self):
        self.session = Session()

    def add_question(self):
        """
        Adds a new question to the quiz database through interactive user input.
        The question and its answer are saved to appropriate database tables based on question type.
        Raises exception if there is an error during question addition, rolls back the transaction
        """
        try:
            while True:
                categories = self.session.query(db.CategoryDB).all()
                print("\nPlease enter category for the question:\n")
                for cat in categories:
                    print(f"{cat.id}. {cat.name.capitalize()}")
                while True:
                    category_id = int(input("\nYour choice: ").strip())
                    if any(cat.id == category_id for cat in categories):
                        break
                    else:
                        print("Invalid category. Please try again.")
                
                question_type = input(
                    "\nWhat type of question would you like to add?\n"
                    " 1. True/False\n"
                    " 2. Multiple Choice\n" 
                    " 3. Fill in the blank\n" 
                    " 4. Short Answer\n\n"
                    "Your choice(1, 2, 3 or 4): ").strip()
                if question_type not in ["1", "2", "3", "4"]:
                    print("\nInvalid question type choice. Please try again.")
                    continue
                
                difficulty = input(
                    "\nWhat is the difficulty of the question?\n"
                    " 1. Easy\n"
                    " 2. Medium\n" 
                    " 3. Hard\n\n" 
                    "Your choice(1, 2 or 3): ").strip()
                if difficulty not in ["1", "2", "3"]:
                    print("\nInvalid question difficulty. Please try again.")
                    continue    

                if question_type == "3":
                    print("Question must contain 3 to 5 consecutive underscores (____) for the 'Fill in the blank' field\n")

                new_question_text = input("\nPlease enter Question text: ").strip()
                if not new_question_text:
                    print("\nQuestion text cannot be empty.")
                    continue
                new_question = db.QuestionDB(question_text = new_question_text, question_type = question_type, category_id = category_id, difficulty = difficulty)
                
                self.session.add(new_question) # Adds the question in order to link its ID with the corresponding table.
                self.session.commit()

                if question_type == "1":
                    while True:
                        answer = input("Please enter correct answer (True/False): ").strip().lower()
                        if answer in ["true", "false"]:
                            break
                        else:
                            print(f"{answer} is not a valid answer. Answer must be True or False. Please provide a valid answer.")
                    question = db.TrueFalseQuestionDB(answer=answer, question=new_question)
                elif question_type == "2":
                    options = []
                    for letter in ["A", "B", "C", "D"]:
                        while True:
                            option = input(f"Option {letter}: ").strip().lower()
                            if option:
                                options.append(option)
                                break
                            else:
                                print(f"Option {letter} cannot be empty. Please provide a valid input.")
                    while True:
                        answer = input("Please enter correct Option (A, B, C or D): ").strip().lower()
                        if answer in ["a", "b", "c", "d"]:
                            break
                        else:
                            print(f"Option {letter} cannot be empty. Please provide a valid answer.")
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
                        print("\nInvalid fill-in-the-blank question. It must contain 3 to 5 consecutive underscores for BLANK visualisation.")
                        self.session.delete(new_question)
                        self.session.commit()
                        continue
                    while True:
                        answer = input("Please enter correct answer: ").strip().lower()
                        if answer:
                            break
                        else:
                            print("Answer cannot be empty. Please provide a valid answer.")
                    question = db.FillInQuestionDB(answer = answer, question = new_question)
                elif question_type == "4":
                    while True:
                        answer = input("Please enter correct answer: ").strip().lower()
                        if answer:
                            break
                        else:
                            print("Answer cannot be empty. Please provide a valid answer.")
                    question = db.ShortAnswerQuestionDB(
                        answer = answer, question = new_question)
                else:
                    print("Unsupported question type.")
                    continue

                self.session.add(question)
                self.session.commit()
                print("\nQuestion has been added successfully!\n")
                break
        except Exception as e:
            self.session.rollback()
            print(f"Error adding question.{e}")
        finally:
            self.session.close()

    
    def delete_question(self):
        """
        Deletes a question from the database based on user input. Handles the deletion of both the main question entry and its related
        type-specific details (True/False, Multiple Choice, etc.)
        """
        try:
            categories = self.session.query(db.CategoryDB).all()
            print("\nPlease enter category for the question you would like to delete:\n")
            
            for cat in categories:
                print(f"{cat.id}. {cat.name.capitalize()}")
            category_id = int(input("\nYour choice: ").strip())
            
            question_type = input(
                "\nPlease enter the type of the question you would like to delete:\n"
                " 1. True/False\n"
                " 2. Multiple Choice\n" 
                " 3. Fill in the blank\n" 
                " 4. Short Answer\n\n"
                "Your choice (1, 2, 3 or 4): ").strip()
            
            question_list = self.session.query(db.QuestionDB).filter_by(category_id = category_id, question_type = question_type).all()
            for question in question_list:
                print(question)

            question_id = int(input("\nPlease enter the ID of the question you would like to delete:\n"
                                "\nID: ").strip())
            
            question_to_del = self.session.query(db.QuestionDB).filter_by(id = question_id).first()
            if question_to_del.question_type == "1":
                related_row = self.session.query(db.TrueFalseQuestionDB).filter_by(question_id = question_id).first()
            elif question_to_del.question_type == "2":
                related_row = self.session.query(db.MultipleChoiceQuestionDB).filter_by(question_id = question_id).first()
            elif question_to_del.question_type == "3":
                related_row = self.session.query(db.FillInQuestionDB).filter_by(question_id = question_id).first()
            elif question_to_del.question_type == "4":
                related_row = self.session.query(db.ShortAnswerQuestionDB).filter_by(question_id = question_id).first()
            else:
                print(f"\nUnknown question type for question ID {question_id}.\n")
                return
            
            confirmation = input (f"\nAre you sure you want to delete question {question_id}? (Y/N):").strip().lower()
            if confirmation == "y":
                if related_row:
                    self.session.delete(related_row)
                self.session.delete(question_to_del)
                self.session.commit()
                print("\nQuestion has been deleted successfully!\n")
            else:
                print("\nDeletion canceled.\n")
            
        except Exception as e:
            print(f"\nError deleting question. {e}. Please try again.\n")
            self.session.rollback()

        finally:
            self.session.close()


    def edit_question(self):
        try:
            categories = self.session.query(db.CategoryDB).all()
            print("\nPlease enter category for the question you would like to edit:\n")
            
            for cat in categories:
                print(f"{cat.id}. {cat.name.capitalize()}")
            category_id = int(input("\nYour choice: ").strip())
            
            question_type = input(
                "\nPlease enter the type of the question you would like to edit:\n"
                " 1. True/False\n"
                " 2. Multiple Choice\n" 
                " 3. Fill in the blank\n" 
                " 4. Short Answer\n\n"
                "Your choice (1, 2, 3 or 4): ").strip()
            
            question_list = self.session.query(db.QuestionDB).filter_by(category_id = category_id, question_type = question_type).all()
            for question in question_list:
                print(question)

            question_id = int(input("\nPlease enter the ID of the question you would like to delete:\n"
                                "\nID: ").strip())
            question_to_edit = self.session.query(db.QuestionDB).filter_by(id = question_id).first()
            if not question_to_edit:
                print(f"\nQuestion with ID {question_id} not found.")
                return
            print(f"\nSelected Question:\n{question_to_edit.question_text}"
                  f"\nDifficulty: {question_to_edit.difficulty}"
                  f"\nCategory: {question_to_edit.category_id}")

            if question_to_edit.question_type == "1":
                related_row = self.session.query(db.TrueFalseQuestionDB).filter_by(question_id = question_id).first()
                print(f"Answer: {related_row.answer.capitalize()}")
            elif question_to_edit.question_type == "2":
                related_row = self.session.query(db.MultipleChoiceQuestionDB).filter_by(question_id = question_id).first()
                print(f"Options:\n A. {related_row.a}\n B. {related_row.b}\n C. {related_row.c}\n D. {related_row.d}")
                print(f"Correct Answer: {related_row.answer.upper()}")
            elif question_to_edit.question_type == "3":
                related_row = self.session.query(db.FillInQuestionDB).filter_by(question_id = question_id).first()
                print(f"Answer: {related_row.answer}")
            elif question_to_edit.question_type == "4":
                related_row = self.session.query(db.ShortAnswerQuestionDB).filter_by(question_id = question_id).first()
                print(f"Answer: {related_row.answer}")
            else:
                print(f"\nUnknown question type for question ID {question_id}.\n")
                return
            
            # Edit question text
            new_question_text = input(
                f"\nCurrent question text: {question_to_edit.question_text}"
                "\nEnter new question text (or press Enter to keep it unchanged): ").strip()
            if new_question_text:
                question_to_edit.question_text = new_question_text
            # Edit difficulty   
            new_difficulty = input("Enter new difficulty (1: Easy, 2: Medium, 3: Hard, or press Enter to keep it unchanged): ").strip()
            if new_difficulty in ["1", "2", "3"]:
                question_to_edit.difficulty = new_difficulty
            # Edit category    
            print("\nAvailable Categories:")
            for cat in categories:
                print(f"{cat.id}. {cat.name.capitalize()}")
            new_category_id = int(input("\nEnter new category ID (or press Enter to keep it unchanged): ").strip())
            if any(cat.id == new_category_id for cat in categories):
                question_to_edit.category_id = new_category_id
            # Edit question answers
            if question_type == "1":
                new_answer = input(
                    f"\nCurrent answer: {related_row.answer.capitalize()}\n"
                    "Enter new answer (True/False, or press Enter to keep it unchanged): ").strip().lower()
                if new_answer in ["true", "false"]:
                    related_row.answer = new_answer

            elif question_type == "2":
                for option in ["a", "b", "c", "d"]:
                    current_option = getattr(related_row, option)
                    new_option = input(
                        f"\nCurrent option {option.upper()}: {current_option}"
                        f"\nEnter new option {option.upper()} (or press Enter to keep it unchanged): ").strip()
                    if new_option:
                        setattr(related_row, option, new_option)
                new_answer = input(
                    f"\nCurrent correct answer: {related_row.answer.upper()}"
                    f"\nEnter new correct answer (A, B, C, or D, or press Enter to keep it unchanged): ").strip().lower()
                if new_answer in ["a", "b", "c", "d"]:
                    related_row.answer = new_answer

            elif question_type == "3":
                new_answer = input(
                    f"\nCurrent answer: {related_row.answer}"
                    f"\nEnter new answer (or press Enter to keep it unchanged): ").strip()
                if new_answer:
                    related_row.answer = new_answer

            elif question_type == "4":
                new_answer = input(
                    f"\nCurrent answer: {related_row.answer}"
                    f"\nEnter new answer (or press Enter to keep it unchanged): ").strip()
                if new_answer:
                    related_row.answer = new_answer

            self.session.commit()
            print("\nQuestion has been updated successfully!")

        except Exception as e:
            self.session.rollback()
            print(f"Error editting question:\n{e}")
        finally:
            self.session.close() 


    def add_category(self):
        """
        Adds a new category to the quiz database after validating user input.
        """
        try:
            while True:
                print("!!!You need to add at least 2 questions per question type in order to use this category in a quiz!!!")
                new_category = input("\nEnter the name of the new category: ").strip().lower()
                if not new_category:
                    print("Category name cannot be empty. Please input a category name:")
                    continue
                existing_category = self.session.query(db.CategoryDB).filter_by(name = new_category).first()
                if existing_category:
                    print(f"{new_category} already exists")
                    continue
                add_new_category = db.CategoryDB(name = new_category)
                self.session.add(add_new_category)
                self.session.commit()
                print(f"{new_category.capitalize()} has been added to Quiz categories.")
                print("Remember!\n"
                    "!!!You need to add at least 2 questions per question type in order to use this category in a quiz!!!\n")
                break
        except Exception as e:
            print(f"Error while adding {new_category.capitalize()} category:\n{e}")
            self.session.rollback()
        finally:
            self.session.close()


    def delete_category(self):
        """
        Deletes a category from the database if it has no associated questions.
        Checks if selected category has any questions. If yes, deletion is prevented..
        """
        try:
            print("!!!You can only delete a category if there are no questions associated with it!!!")
            categories = self.session.query(db.CategoryDB).all()
            for cat in categories:
                print(f"{cat.id}. {cat.name.capitalize()}")

            while True:
                category_id = int(input("\nEnter the ID of the category you would like to delete: ").strip())
                category_to_del = self.session.query(db.CategoryDB).filter_by(id = category_id).first()
                if category_to_del:
                    break
                else:
                    print("Invalid category ID. Please try again.")

            associated_questions = self.session.query(db.QuestionDB).filter_by(category_id = category_id).count()
            if associated_questions > 0:
                print(f"\n'{category_to_del.name.capitalize()}' cannot be deleted because it has {associated_questions} associated questions.\n"
                      "Please delete all question associated with this category first.\n")
                return
            
            self.session.delete(category_to_del)
            self.session.commit()
            print(f"\n'{category_to_del.name.capitalize()}' has been deleted successfully!")
        
        except Exception as e:
            self.session.rollback()
            print(f"\nError deleting category:\n {e}\n")
        finally:
            self.session.close()

