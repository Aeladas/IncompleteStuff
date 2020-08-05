import tkinter
import time
import random
import math
import turtle
import random

def str_abba():
    """
    The purpose of this function is to take in two user inputs.
        > Then convert them into strings for processing as we are telling the unassigned 8-bit int to represent a string
        > Wait for 2 seconds by using the sleep function of the time module
        > Print on a new line so that its readable and add spaces between each word
    """
    _a = str(input("1st Word: "))
    _b = str(input("2nd Word: "))
    sleep(2)
    _print("\n" +_a + "" + _b + "" +_b + "" + _a)

def compare_ages():
    _user = int(input("Your Age(1-100): "))
    _computer = int(random.choice(0, 100))
    _difference = _computer - _user
    _difference2 = _computer + _user

    if( _user > 0 & _user < 101 & _user < computer):
        print("You are younger than me by" + "" + difference + "Year(s)")
    elif( _user > 0 & _user < 101 & _user > _computer):
        print("You are older than me by" + "" + difference2 + "Year(s)")
    elif( _user > 0 & _user < 101 & _user == computer):
        print("You are the same age as me!")
    else:
        print("There's an error somewhere, dont just sit there fix it!")

def guessing_game():
    _compNum = int(random.randint(1, 100))
    _userNum = int(input("Your Number 1-100 (#): "))
    n = int(0)

    while (_userNum != _compNum & _userNum <= _compNum):
        n = n + 1
        sleep(2)
        print("=======\n")
        sleep(2)
        _userNum = int()
