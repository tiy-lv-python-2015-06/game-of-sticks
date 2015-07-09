


class Game:
#This does all the heavy lifting
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.stick_count = Sticks()

    def active_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
            self.player = self.current_player
        else:
            self.current_player = self.player1
            self.player = self.current_player

    def start(self):
        while self.stick_count > 0:
            print("{} sticks in the stick pile!".format(self.stick_count))

        #I need to activate the players turn
        #and set the win / lose conditions
        #then run it all.
        #that sounds so easy to type.


class Player:
#This will handle player 1, 2 and AI. and Turns
    def __init__(self, name="Hank"):
        self.name = name
        self.stick_count = Sticks()
        self.stick_remove = 0

    def player_turn(self):
        if self.stick_count >= 3:
            stick_remove = input("{} how many sticks would"
                                 " you like to remove (1-3)? ".format(self.name))
            self.stick_count = self.stick_count -  self.stick_remove
            return self.stick_count

        elif self.stick_count <= 2:
            stick_remove = input("{} how many sticks would"
                            "you like to remove (1-2)? ".format(self.name))
            self.stick_count = self.stick_count - self.stick_remove
            return self.stick_count


class Sticks:
#This is just going to hold the sticks
    def __init__(self):
        self.stick_count = 0

    def stick_pile(self):
        stick_count = input(int("Welcome to Sticks! Please choose (10-100)"))
        if stick_count < 10 or stick_count > 100:
            print("That was not a valid number!")
        else:
            return stick_count


if __name__ == '__main__':

