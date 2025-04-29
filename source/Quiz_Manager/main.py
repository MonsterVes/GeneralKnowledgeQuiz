
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import time
from source.Quiz_Manager import quiz_menus as qm
from source.Quiz_Manager import user_actions as ua


# print(sys.path)
# cwd = os.getcwd()
# print (cwd)

def main():

    print("Welcome to QuizUp!")
    time.sleep(0.6)


    while True:
        qm.main_menu()
        main_menu_action = input("Your choice: ")
        if main_menu_action == "1":
            qm.take_a_quiz_menu()
            quiz_action = input ("Your choice: ")
            ua.take_a_quiz_action(quiz_action)
        elif main_menu_action == "2":
            qm.manage_quiz_menu()
            manage_action = input ("Your choice: ")
            ua.manage_quiz_action(manage_action)
        elif main_menu_action == "3":
            sys.exit("Thank you for visiting QuizUp! Goodbye!")
        else: 
            print(f"{main_menu_action} is not a valid choice. Please try again.\n")



if __name__ == "__main__":
    main()