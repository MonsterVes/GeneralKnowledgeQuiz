from source.Database import quiz_db as qdb
from sqlalchemy.orm import Session

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
    categories = session.query(qdb.CategoryDB).all()
    print("\nSelect your quiz preference:\n")
    for cat in categories:
        print(f"{cat.id}. {cat.name.capitalize()}")
    print("or type 0 to take a Random Categories Quiz")

    while True:
        category = int(input("\nYour choice: ").strip())
        return category


def quiz_difficulty_menu():
    difficulty = input("\nSelect difficulty:\n"
        " 1. Easy\n"
        " 2. Medium\n"
        " 3. Hard\n\n"
        "Your choice: ").strip()
    return difficulty


def question_limit():
    question_limit = int(input(
        "\nSelect the total number of questions: 8, 12, 16, 20 or 24\n\n"
        "Your choice: ").strip())
    return question_limit


def manage_quiz_menu():
    manage_action = input("\nPlease choоse one of the following options:\n" 
          " 1. Add question\n"
          " 2. Edit question\n" 
          " 3. Delete question\n"
          " 4. Add category\n"
          " 5. Delete category\n\n"
          "Your choice: ").strip()
    return manage_action


