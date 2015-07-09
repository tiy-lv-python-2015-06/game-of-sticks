import random

#look at how the AI is running
#pit how AI

class StickStack:
    def __init__(self, how_many_sticks=20):
        """Creates instance of Stack of Sticks"""
        self.stick_count = how_many_sticks


    def take_away_sticks(self, how_many_sticks):
        self.stick_count = self.stick_count - how_many_sticks
        print("Took away {}, there are {} sticks in the stack now. \n".format(how_many_sticks, self.stick_count))
        return self.stick_count


    # Don't make a get_stick_count() method, instead call stick_stack.stick_count attribute


    def add_sticks(self, how_many_sticks):
        self.stick_count = self.stick_count + how_many_sticks
        print("Debug added {} sticks stick_count now{}".format(how_many_sticks, self.stick_count))
        return self.stick_count


class Player:
    """Player keeps its score, its name, his sets of turns"""
    def __init__(self, name="Hal", player_type="human"):
        self.name = name
        self.player_type = type   # marker for Human or AI later
        self.score = 0
        self.picked_sets = []


    def choose_number_of_sticks(self):
        print("Your turn, {}.\n".format(self.name))
        raw_choice = input("How many sticks do you want? > \n")
        number_chosen = int(raw_choice)
        return number_chosen


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.player = self.current_player
        self.stick_stack = StickStack()
        self.winner = None


    def change_current_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
            self.player = self.current_player
        else:
            self.current_player = self.player1
            self.player = self.current_player


    def set_choice(self, number_chosen):
        # have that choice go to set_choice which updates stick_stack.count and turn count
        # update stick_stack
        self.stick_stack.take_away_sticks(number_chosen)


    def start(self):
        #creates stick_stack
        print("stick_stack stick_count is {}".format(self.stick_stack.stick_count))
        # If stick stack is not 0, ask current player if they want to pick
        if self.stick_stack.stick_count != 0:
            #game.run() is going to call game.go() which will do most of the work
            self.run()

    def you_lose(self):
        print("Sorry, {}, you lose.".format(self.current_player.name))
        if self.current_player == self.player1:
            self.winner = self.player2.name
        elif self.current_player == self.player2:
            self.winner = self.player1.name
        print("{} Wins!".format(self.winner))


    def run(self):
        self.go()   #this isolates the loop into one method for testing


    def go(self):
        #if player eligible
        while self.stick_stack.stick_count <= 20 and self.stick_stack.stick_count > 1:
            print("-- " * self.stick_stack.stick_count)
            # tell player how many sticks in overall stick_stack
            print("There are {} sticks in the Stick Stack \n".format(self.stick_stack.stick_count))
            # ask player to choose number of sticks
            number_chosen = self.player.choose_number_of_sticks()
            # have that choice go to set_choice which and updates stick_stack.count and turn count
            self.set_choice(number_chosen)
            #change players
            self.change_current_player()
        if self.stick_stack.stick_count < 1:
            self.you_lose()
            print("You lose, {}".format(self.current_player))



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
