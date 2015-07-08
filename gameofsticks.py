import random

#look at how the AI is running
#pit how AI

class StickStack:
    def __init__(self, how_many_sticks):
        """Creates instance of Stack of Sticks"""
        self.stick_count = how_many_sticks


    def get_stick_count(self):
        return self.stick_count


    def take_away_sticks(self, how_many_sticks):
        self.stick_count = self.stick_count - how_many_sticks
        return self.stick_count

    def add_sticks(self, how_many_sticks):
        self.stick_count = self.stick_count + how_many_sticks
        return self.stick_count

class Picks:

    def __init__(self):
        pass

    def set_pick(self, how_many_sticks):
        self.stick_count = how_many_sticks



class Player:
    """Player keeps its score, its name, his sets of turns"""
    def __init__(self, name="Hal"):
        self.name = name
        self.score = score
        self.turns_sets = []




# class AIPlayer
# It will inherit attributes and methods from Player with additional attributes and methods
#    pass



if __name__ == '__main__':
    new_stack = StickStack(20)
    new_stack.take_away_sticks(3)
    new_stack.add_sticks(4)
    print(new_stack.get_stick_count())
