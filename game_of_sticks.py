import random


class Game():
#This does all the heavy lifting
    def __init__(self, sticks, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.sticks = sticks


    def active_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
            self.player = self.current_player
        else:
            self.current_player = self.player1
            self.player = self.current_player


    def start(self):
        starting_sticks = int(input("Welcome to Sticks! Please enter a number"
                            " between (10-100): "))
        if starting_sticks < 10 or starting_sticks > 100:
            print("That was not a valid choice, Please try again (10_100): ")
            self.start()

        while self.sticks > 1:
            print("{} sticks in the stick pile!".format(self.sticks))
            picker = self.current_player.player_turn(self.sticks)
            self.sticks -= picker
            self.active_player()

        else:
            print("{} You Lose!".format(self.current_player.name))


class Player:
#This will handle player 1, 2 and AI.
    def __init__(self, name):
        self.name = name

    def player_turn(self, sticks):
        choice = int(input("{} How many sticks would you"
                           " like to remove(1-3)? ".format(self.name)))
        if choice < 1 or choice > 3:
            self.player_turn()
        else:
            return choice


class DumbComputer(Player):

    def __init__(self, name):
        super().__init__(name)

    def player_turn(self, sticks):
        choice = random.randint(1, 3)
        print("{} removed {} sticks".format(self.name, choice))
        return choice

class Hat:
    ball_list = [1, 2, 3]
    ball_choice = 0
    number = 0
    def __init__(self, number):
        self.number = number

    def choose_ball(self):
        self.ball_choice = random.choice(self.ball_list)
        return self.ball_choice





if __name__ == '__main__':

    player1 = Player("Jim")
    player2 = DumbComputer("AI")

    game = Game(10, player1, player2)
    game.start()
