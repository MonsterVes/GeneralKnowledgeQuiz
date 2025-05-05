from source.Database import quiz_db as qdb
from sqlalchemy.orm import Session
import question_manager as manager
import sys


session = Session(bind = qdb.engine)

def main_menu():
    main_menu_action = input(
        "\nPlease choose one of the following options:\n"
        " 1. Take a quiz\n"
        " 2. Manage quiz\n"
        " 3. Quit\n\n"
        "Your choice: ").strip()
    return main_menu_action


def quiz_category_menu():
    """
    Displays question categories menu and returns user's choice.
    """
    try:
        categories = session.query(qdb.CategoryDB).all()
        print("\nSelect your quiz preference:\n")
        for cat in categories:
            print(f"{cat.id}. {cat.name.capitalize()}")
        print("0. Random Categories\n"
              "Or type 'exit' to exit the Quiz.\n")

        while True:
            category = input("Your choice: ").strip()
            if category == "0":
                return int(category)
            elif any(cat.id == int(category) for cat in categories):
                return int(category)
            elif category == "exit":
                sys.exit("\nThank you for visiting QuizUp! Goodbye!")
            else:
                print(f"{category} is not a valid choice. Please try again.")
    except Exception as e:
        print(f"Error loading Categories:\n{e}")
        

def quiz_difficulty_menu():
    """
    Displays difficulty menu and returns user's choice.
    """
    while True:
        difficulty = input("\nSelect difficulty:\n"
            " 1. Easy\n"
            " 2. Medium\n"
            " 3. Hard\n"
            " Or type 'exit' to exit the Quiz.\n\n"
            "Your choice: ").strip()
        if difficulty in ["1", "2", "3"]:
            return difficulty
        elif difficulty == "exit":
            sys.exit("\nThank you for visiting QuizUp! Goodbye!")
        else:
            print(f"{difficulty} is not a valid choice. Please try again.")


def question_limit():
    """
    Displays questions limit and returns user's choice.
    """
    while True:
        question_limit = input(
            "\nSelect the total number of questions: 8, 12, 16, 20 or 24\n\n"
            "Or type 'exit' to exit the Quiz.\n"
            "Your choice: ").strip().lower()
        if question_limit in ["8", "12", "16", "20", "24"]:
            return int(question_limit)
        elif question_limit == "exit":
            sys.exit("\nThank you for visiting QuizUp! Goodbye!")
        else:
            print(f"{question_limit} is not a valid choice. Please try again.")


def manage_quiz_menu():
    """
    Displays quiz management menu and returns user's choice.
    """
    while True:
        manage_action = input("\nPlease choоse one of the following options:\n" 
            " 1. Add question\n"
            " 2. Edit question\n" 
            " 3. Delete question\n"
            " 4. Add category\n"
            " 5. Delete category\n"
            " Or type 'exit' to exit the Quiz.\n\n"
            "Your choice: ").strip().lower()
        if manage_action in ["1", "2", "3", "4", "5", "exit"]:
            return manage_action
        else: 
            print(f"\n{manage_action} is not a valid choice. Please try again.")


def handle_manage_quiz_menu():
    """
    Handles the quiz management actions (add, edit, delete questions/categories).
    """
    question_manager = manager.QuestionManager()
    manage_action = manage_quiz_menu()

    if manage_action == "1":
        question_manager.add_question()
    elif manage_action == "2":
        question_manager.edit_question()
    elif manage_action == "3":
        question_manager.delete_question()
    elif manage_action == "4":
        question_manager.add_category()
    elif manage_action == "5":
        question_manager.delete_category()
    elif manage_action == "exit":
        sys.exit("\nThank you for visiting QuizUp! Goodbye!")       
    else:
        print(f"\n{manage_action} is not a valid choice. Please try again.\n")


