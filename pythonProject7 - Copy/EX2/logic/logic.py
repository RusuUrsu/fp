from EX2.UI.console import get_user_choice
import random

def get_computer_choice():
    return str(random.randint(1,3))


def init_state():
    return [0,0]


def get_winner(a,b):
    if a == '1' and b == '2':
        return 'computer'
    if a == '2' and b == '1':
        return 'user'
    if a == '1' and b == '3':
        return 'user'
    if a == '3' and b == '1':
        return 'computer'
    if a == '2' and b == '3':
        return 'computer'
    if a == '3' and b == '2':
        return 'user'
    if a == b:
        return 'draw'

def update_state(state,outcome):
    if outcome == 'draw':
        return state
    elif outcome == 'user':
        state[0] += 1
    elif outcome == 'computer':
        state[1] += 1

def is_done(state):
    if state[1] + state[0] == 3:
        return True
    else:
        return False