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

    # Don't make a get_stick_count() method, instead call stick_stack.stick_count attribute


    def add_sticks(self, how_many_sticks):
        self.stick_count = self.stick_count + how_many_sticks
        print("Debug added {} sticks stick_count now{}".format(how_many_sticks, self.stick_count))
        return self.stick_count

class Turn:

    def __init__(self, player, stick_stack):
        self.player = player
        self.stick_stack = stick_stack
        self.turn_over = False


    def set_choice(self, number_chosen):
        # have that choice go to set_choice which updates player score and updates stick_stack.count and turn count
        self.player.score += number_chosen
        #update stick stack
        self.stick_stack.take_away_sticks(number_chosen)


    def run(self):
        while not self.turn_over:
            self.go()   #this isolates the loop into one method for testing


    def go(self):
        #if player eligible
        if self.player.score < 20:
            # tell player how many sticks she has
            print("You have {} sticks.\n".format(self.player.score))
            print("-- " * self.player.score)
            # tell player how many sticks in overall stick_stack
            print("There are {} sticks in the Stick Stack \n".format(self.stick_stack.stick_count))
            print("-- " * self.stick_stack.stick_count)
            # ask player to choose number of sticks
            number_chosen = self.player.choose_number_of_sticks()
            # have that choice go to set_choice which updates player score and updates stick_stack.count and turn count
            self.set_choice(number_chosen)
            #turn is over, switch players
            self.turn_over = True
                #switch players
                # How to switch players




class Player:
    """Player keeps its score, its name, his sets of turns"""
    def __init__(self, name="Hal", player_type="human"):
        self.name = name
        self.player_type = type   # marker for Human or AI later
        self.score = 0
        self.picked_sets = []

    def choose_number_of_sticks(self):
        raw_choice = input("How many sticks do you want? (If you want to pass, pick 0)\n")
        number_chosen = int(raw_choice)
        return number_chosen

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1


    def change_current_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1


    def start(self):
        #creates stick_stack
        stick_stack = StickStack()
        number_of_sticks = stick_stack.stick_count
        print(number_of_sticks)
        # If stick stack is not 0, ask current player if they want to pick
        while stick_stack != 0:
            #instantiate a turn
            turn = Turn(self.current_player, stick_stack)
            #turn.run() is going to call turn.go() which will do most of the work
            while not turn.turn_over:
                turn.run()
                #self.current_player.choose_pass_or_play()





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
