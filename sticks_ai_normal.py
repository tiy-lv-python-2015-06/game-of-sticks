import random


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


class ComputerPlayer(object):
    """Object for controlling AI"""
    hat_size = 0
    hat = []
    content = [1, 2, 3]
    beside = []

    def __init__(self, the_sticks):
        """Initializes AI object"""
        count = 0
        self.hat_size = the_sticks
        while count <= the_sticks - 1:
            self.hat.append(self.content)
            self.beside.append([])
            count += 1

    def choose_stick(self):
        """Chooses a stick in a hat and reorders"""
        return random.choice(self.content)


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


def ai_chooses_sticks(ai, sticks_left):
    """Gets the number of sticks the ai wants to choose."""
    ai_input = 0
    good_number = False
    while not good_number:
        if sticks_left >= 3:
            print("AI player, how many sticks do you take (1-3)? ")
            ai_input = ai.choose_stick()
            print("The AI chose {} sticks.".format(ai_input))
            if (ai_input < 1) or (ai_input > 3):
                print("Please enter a valid number between 1 and 3.")
                good_number = False
            else:
                good_number = True
        elif sticks_left == 2:
            print("AI player, how many sticks do you take (1-2)? ")
            ai_input = ai.choose_stick()
            print("The AI chose {} sticks.".format(ai_input))
            if (ai_input < 1) or (ai_input > 2):
                print("Please enter a valid number between 1 and 2.")
                good_number = False
            else:
                good_number = True
        elif sticks_left == 1:
            print("AI player, how many sticks do you take (1)? ")
            ai_input = ai.choose_stick()
            print("The AI chose {} sticks.".format(ai_input))
            if ai_input != 1:
                print("Please enter a valid number.  The only valid number now is 1.")
                good_number = False
            else:
                good_number = True
    print()
    return ai_input


def game_options():
    """Gets options for player or AI opponent."""
    user_input = ""
    good_number = False
    print("Options:")
    print(" Play against a friend (1)")
    print(" Play against the computer (2)")
    while not good_number:
        user_input = input("Which option do you take (1-2)? ")
        if int(user_input) not in [1, 2]:
            print("Please enter a valid number for option.  Must be 1 or 2.")
            good_number = False
        else:
            good_number = True
    print()
    return int(user_input)


def player_v_player(won, player_object, sticks_object):
    """Player vs. Player part of game."""
    while not won:
        print("There are {} sticks on the board.".format(sticks_object.get_number_of_sticks()))
        temp_sticks = player_chooses_sticks(player_object.get_player(), sticks_object.get_number_of_sticks())
        sticks_object.subtract_sticks(temp_sticks)
        if sticks_object.get_number_of_sticks() == 0:
            won = True
            print("Player {}, you lose!".format(player_object.get_player()))
        else:
            won = False
            if player_object.get_player() == 1:
                player_object.set_player(2)
            else:
                player_object.set_player(1)


def player_v_ai(won, player_object, sticks_object, ai_object):
    """Player vs. AI part of game."""
    while not won:
        print("There are {} sticks on the board.".format(sticks_object.get_number_of_sticks()))
        if player_object.get_player() == 1:
            temp_sticks = player_chooses_sticks(player_object.get_player(), sticks_object.get_number_of_sticks())
        else:
            temp_sticks = ai_chooses_sticks(ai_object, sticks_object.get_number_of_sticks())
        sticks_object.subtract_sticks(temp_sticks)
        if sticks_object.get_number_of_sticks() == 0:
            won = True
            if player_object.get_player() == 1:
                print("Player {}, you lose!".format(player_object.get_player()))
            else:
                print("AI Player, you lose!")
        else:
            won = False
            if player_object.get_player() == 1:
                player_object.set_player(2)
            else:
                player_object.set_player(1)


if __name__ == '__main__':
    # Start program here if file run directly
    play_again = True
    while play_again:
        option_chosen = 0
        game_won = False
        player = PlayerTracking(1)
        num_of_sticks = setup_game()
        sticks_for_game = Sticks(num_of_sticks)
        ai_player = ComputerPlayer(num_of_sticks)
        option_chosen = game_options()
        if option_chosen == 1:
            player_v_player(game_won, player, sticks_for_game)
        if option_chosen == 2:
            player_v_ai(game_won, player, sticks_for_game, ai_player)
        play_again = input("Play again (y/n)? ")
        if play_again.lower() == 'y':
            play_again = True
        else:
            play_again = False
        print()
