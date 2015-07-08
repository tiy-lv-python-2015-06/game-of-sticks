import random

#look at how the AI is running
#pit how AI

class StickStack:
    def __init__(self, how_many_sticks=20):
        """Creates instance of Stack of Sticks"""
        self.stick_count = how_many_sticks


    def take_away_sticks(self, how_many_sticks):
        self.stick_count = self.stick_count - how_many_sticks
        print("Debug took away {} sticks stick_count now{}".format(how_many_sticks, self.stick_count))
        return self.stick_count


    def add_sticks(self, how_many_sticks):
        self.stick_count = self.stick_count + how_many_sticks
        print("Debug added {} sticks stick_count now{}".format(how_many_sticks, self.stick_count))
        return self.stick_count

class Picks:

    def __init__(self):
        pass


    def set_pick(self, how_many_sticks):
        print("Debug set_pick {}".format(how_many_sticks))
        self.stick_count = how_many_sticks
        return self.stick_count



class Player:
    """Player keeps its score, its name, his sets of turns"""
    def __init__(self, name="Hal"):
        self.name = name
        self.score = 0
        self.picked_sets = []



class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        current_player = player1

    def start(self):
        #creates stick_stack
        stick_stack = StickStack()
        number_of_sticks = stick_stack.stick_count
        print(number_of_sticks)
        # If stick stack is not 0, ask current player if they want to pick
        while stick_stack != 0:
            


# class AIPlayer
# It will inherit attributes and methods from Player with additional attributes and methods
#    pass


if __name__ == '__main__':

    player1 = Player("Hal")
    player2 = Player("Marvin")
    game = Game(player1, player2)
    game.start()




    # new_stack = StickStack(20)
    # new_stack.take_away_sticks(3)
    # new_stack.add_sticks(4)
    # print(new_stack.get_stick_count())
