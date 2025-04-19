import time
import user_actions as ua

def main():

    print("Welcome to QuizUp!")
    time.sleep(0.6)

call_main_menu = True
while call_main_menu:
    main_menu_action = input("Your choice: ")
    ua.main_menu_action()



if __name__ == "__main__":
    main()