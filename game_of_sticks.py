import random
import collections

class CompPlayer:
    def __init__(self):
        pass
    def turn(self):
        pass
        # how the AI uses it's turn
    def brains(self):
        pass
        # How the AI learns, prolly needs to be more methods

def ask_for_sticks(initial_sticks=None):
    print('How many Sticks would you like to start with (10-100)?\n')
    while not initial_sticks:
        initial_sticks = input('Please enter a number between 10-100\n')
        try:
            100 > int(initial_sticks) > 10
            return int(initial_sticks)
        except:
            initial_sticks = None
            continue


def sticks_to_remove(remove_sticks=None):
    print('How many Sticks would you like to remove?\n')
    while remove_sticks is None and sticks >= 5:
        remove_sticks = input('Please enter a number between 1-3\n')
        try:
            3 > int(remove_sticks) > 1
            return int(remove_sticks)
        except:
            remove_sticks = None
            continue
    while sticks <= 4:
        remove_sticks = input('Please enter a number between 1-{}\n'.format(sticks+1,))
        try:
            sticks+1 > int(remove_sticks) > 1
            return int(remove_sticks)
        except:
            remove_sticks = None
            continue



if __name__ == '__main__':
    print('Welcome to the Game of Sticks')
    sticks = ask_for_sticks()
    sticks -= sticks_to_remove()
    print(sticks)
