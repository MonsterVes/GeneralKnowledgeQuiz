import quiz_menus as menu
import question_manager as manager


def main_menu_action(action):
    if action == "1":
        menu.take_a_quiz_menu()
    elif action == "2":
        menu.manage_quiz_menu()
    else:
        print(f"{action} is not a valid option. Please try again")


def take_a_quiz_action(quiz_action):
    while True:
        if quiz_action == "1":
            print("Start a General knowledge quiz (NOT READY)")
            break
        elif quiz_action == "2":
            print("Start a Natural sciences quiz (NOT READY)")
            break
        elif quiz_action == "3":
            print("Start a Geography quiz (NOT READY)")
            break
        elif quiz_action == "4":
            print("Start a Custom quiz (NOT READY)")
            break
        elif quiz_action == "5":
            menu.main_menu()
            break
        else:
            print(f"{quiz_action} is not a valid choice. Please try again\n")
            menu.take_a_quiz_menu()
            quiz_action = input("Your choice: ")

question_manager = manager.QuestionManager()

def manage_quiz_action(manage_action):
    while True:
        if manage_action == "1":
            question_manager.add_question()
            break
        elif manage_action == "2":
            print("Edit question (NOT READY)")
            break
        elif manage_action == "3":
            print("Delete question (NOT READY)")
            break
        else:
            print(f"{manage_action} is not a valid choice. Please try again\n")
            menu.manage_quiz_menu()  
            manage_action = input("Your choice: ")