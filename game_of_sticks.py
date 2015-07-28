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
        while self.sticks > 1:
            print("{} sticks in the stick pile!".format(self.sticks))
            picker = self.current_player.player_turn(self.sticks)
            self.sticks -= picker
            self.active_player()

        else:
            print("GAME OVER MAN!!")


class Player:
#This will handle player 1, 2 and AI.
    def __init__(self, name):
        self.name = name

    def player_turn(self, sticks):
        choice = int(input("How many sticks would you like to remove(1-3)? "))
        return choice

    # class Hat:
    #
    #     def __init__(self):
    #         self.chosen_ball = []
    #         self.ball_list = [1, 2, 3]
    #
    #     def hat_bucket(self):
    #         hats = {hat hats[x] for hats in hat}
    #
    #         for self.hat in hats:
    #             self.chosen_ball.self.random.choice[1, 2, 3]

if __name__ == '__main__':

    player1 = Player("Jim")
    player2 = Player("Bob")

    game = Game(10, player1, player2)
    game.start()
