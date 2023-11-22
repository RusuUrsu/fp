from EX2.logic.logic import *

def test_winner():
    assert test_winner('1','2') == 'computer won'
    assert test_winner('3','2') == 'user won'

def test_exit():
    assert is_done('draw') == False
    assert is_done('computer won') == True