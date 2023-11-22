from EX2.UI.console import *
from EX2.logic.logic import *
def main():
    show_menu()
    state = init_state()

    while True:
        user_choice = get_user_choice()
        show_choice(user_choice)
        computer_choice = get_computer_choice()
        show_choice(computer_choice)

        show_winner(get_winner(user_choice,computer_choice))
        outcome = get_winner(user_choice,computer_choice)
        update_state(state,outcome)
        show_score(state)

        if is_done(state):
            show_final_winner(state)
            return




main()