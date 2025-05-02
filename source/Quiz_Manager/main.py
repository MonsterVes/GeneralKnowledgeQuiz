import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import time
import question_manager as manager
from source.Quiz_Manager import quiz_menus as qm
from source.Quiz_Manager.quiz_class import Quiz


def main():

    print("Welcome to QuizUp!")
    time.sleep(0.6)


    while True:
        main_menu_action = qm.main_menu()
        if main_menu_action == "1":       
            quiz = Quiz(qm.quiz_category_menu(), qm.quiz_difficulty_menu(), qm.question_limit() )
            quiz.load_questions()
            quiz.start_quiz()

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
                print(f"{manage_action} is not a valid choice. Please try again")
        elif main_menu_action == "3":
            sys.exit("Thank you for visiting QuizUp! Goodbye!")
        else: 
            print(f"{main_menu_action} is not a valid choice. Please try again.\n")



if __name__ == "__main__":
    main()