import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import time
import question_manager as manager
from source.Quiz_Manager import quiz_menus as qm
from source.Quiz_Manager.quiz_class import Quiz


def main():
    print("~-"*16)
    print("~-~-   Welcome to QuizUp!   ~-~-")
    print("~-"*16,"\n")
    time.sleep(0.5)


    while True:
        main_menu_action = qm.main_menu()
        if main_menu_action == "1":       
            quiz = Quiz(qm.quiz_category_menu(), qm.quiz_difficulty_menu(), qm.question_limit() )
            quiz.load_questions()
            quiz.start_quiz()
            break
        elif main_menu_action == "2":
            question_manager = manager.QuestionManager()
            manage_action = qm.manage_quiz_menu()
            if manage_action == "1":
                question_manager.add_question()
            elif manage_action == "2":
                question_manager.edit_question()
            elif manage_action == "3":
                question_manager.delete_question()
            else:
                print(f"\n{manage_action} is not a valid choice. Please try again.\n")
        elif main_menu_action == "3":
            sys.exit("Thank you for visiting QuizUp! Goodbye!")
        else: 
            print(f"\n{main_menu_action} is not a valid choice. Please try again.\n")



if __name__ == "__main__":
    main()