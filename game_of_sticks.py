class Sticks (object):
    """This class keeps track of the number of sticks and allows access to the number."""
    total_sticks = 0

    def __init__(self, number_of_sticks):
        """Initializes the object with the number of sticks."""
        self.total_sticks = number_of_sticks

    def get_number_of_sticks(self):
        """Gets and returns the total sticks in the object."""
        return self.total_sticks

    def subtract_sticks(self, number_to_subtract):
        """Subtracts from total sticks."""
        self.total_sticks = self.total_sticks - number_to_subtract


class PlayerTracking(object):
    """This class keeps track of which player is picking"""
    current_player = 1

    def __init__(self, the_player):
        """Initializes player."""
        self.current_player = the_player

    def get_player(self):
        """Gets the player."""
        return self.current_player

    def set_player(self, the_player):
        """Sets the player."""
        self.current_player = the_player


def setup_game():
    """Sets up the game by asking user for the number of sticks to use in the game."""
    user_input = ""
    good_number = False
    print("Welcome to the Game of Sticks!")
    while not good_number:
        user_input = input("How many sticks are there on the table initially (10-100)? ")
        if (int(user_input) < 10) or (int(user_input) > 100):
            print("Please enter a valid number between 10 and 100.")
            good_number = False
        else:
            good_number = True
    print()
    return int(user_input)


def player_chooses_sticks(player_number, sticks_left):
    """Gets the number of sticks the player wants to choose."""
    user_input = ""
    good_number = False
    while not good_number:
        if sticks_left >= 3:
            user_input = input("Player {}: How many sticks do you take (1-3)?".format(player_number))
            if (int(user_input) < 1) or (int(user_input) > 3):
                print("Please enter a valid number between 1 and 3.")
                good_number = False
            else:
                good_number = True
        elif sticks_left == 2:
            user_input = input("Player {}: How many sticks do you take (1-2)?".format(player_number))
            if (int(user_input) < 1) or (int(user_input) > 2):
                print("Please enter a valid number between 1 and 2.")
                good_number = False
            else:
                good_number = True
        elif sticks_left == 1:
            user_input = input("Player {}: How many sticks do you take (1)?".format(player_number))
            if int(user_input) != 1:
                print("Please enter a valid number.  The only valid number now is 1.")
                good_number = False
            else:
                good_number = True
    print()
    return int(user_input)


if __name__ == '__main__':
    # Start program here if file run directly
    game_won = False
    player = PlayerTracking(1)
    sticks_for_game = Sticks(setup_game())
    while not game_won:
        print("There are {} sticks on the board.".format(sticks_for_game.get_number_of_sticks()))
        temp_sticks = player_chooses_sticks(player.get_player(), sticks_for_game.get_number_of_sticks())
        sticks_for_game.subtract_sticks(temp_sticks)
        if sticks_for_game.get_number_of_sticks() == 0:
            game_won = True
            print("Player {}, you lose!".format(player.get_player()))
        else:
            game_won = False
            if player.get_player() == 1:
                player.set_player(2)
            else:
                player.set_player(1)