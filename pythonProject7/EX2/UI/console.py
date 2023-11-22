


def show_score(state):
    print(f'user: {state[0]}  ------  {state[1]} :computer')
def show_menu():
    print("""
        make your choice:
           1 -> Rock
           2 -> Paper
           3 -> Scissors
    """)

def show_final_winner(state):
    if state[0] > state[1]:
        print("User Has Won It All")
    elif state[1] > state[0]:
        print("GAME OVER -> Computer Won")

def show_winner(winner):
    if winner != 'draw':
        print(f'{winner} has won')
    else:
        print('It is a draw, choose again')
def show_choice(choice):
    #Rock
    if choice == '1':
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    #Paper
    elif choice == '2':
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
    #Scissors
    elif choice == '3':
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)

def get_user_choice():
    choice = input("1, 2 , 3: ")
    return choice

