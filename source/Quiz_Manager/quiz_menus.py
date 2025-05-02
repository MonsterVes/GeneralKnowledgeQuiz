def main_menu():
    print("\nPlease choose one of the following options:\n"
            " 1. Take a quiz\n"
            " 2. Manage quiz\n"
            " 3. Quit\n")


def quiz_category_menu():
    category = input(
        "\nSelect your quiz preference:\n"
        "1. General knowledge quiz\n"
        "2. Natural sciences quiz\n"
        "3. Geography quiz\n"
        "4. Custom quiz\n" 
        "5. Back to Main Menu\n\n"
        "Your choice: ").strip()
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
    manage_action = input("Please chose one of the following options:\n" 
          "1. Add question\n"
          "2. Edit question\n" 
          "3. Delete question\n")
    return manage_action


