import quiz_menus as qm


def main_menu_action(action):
    if action == "1":
        qm.take_a_quiz_menu()
    elif action == "2":
        qm.manage_quiz_menu()
    else:
        print(f"{action} is not a valid option. Please try again")


def take_a_quiz_action(action):
    if action == "1":
        print("Start a General knowledge quiz (NOT READY)")
    elif action == "2":
        print("Start a History quiz (NOT READY)")
    elif action == "3":
        print("Start a Natural sciences quiz (NOT READY)")
    elif action == "4":
        print("Start a Geography quiz (NOT READY)")
    elif action == "5":
        print("Start an Art quiz (NOT READY)")
    elif action == "6":
        print("Start a Custom quiz (NOT READY)")
    else:
        print(f"{action} is not a valid option. Please try again")


def manage_quiz_action(action):
    if action == "1":
        print("Add question (NOT READY)")
    elif action == "2":
        print("Edit question (NOT READY)")
    elif action == "3":
        print("Delete question (NOT READY)")
    else:
        print(f"{action} is not a valid option. Please try again")
