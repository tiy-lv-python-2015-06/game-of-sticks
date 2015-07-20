import random


class Game:
    """Controls flow and functioning of game."""
    number_of_sticks = 0
    option = 0
    current_player = 1

    def __init__(self):
        """Sets up the game and requests number of sticks to use and the option for the game"""
        self.setup_game()
        self.get_game_options()

    def setup_game(self):
        """Sets up the game by asking user for the number of sticks to use in the game."""
        user_input = ""
        good_number = False
        print("Welcome to the Game of Sticks!")
        while not good_number:
            user_input = int(input("How many sticks are there on the table initially (10-100)? "))
            if user_input < 10 or user_input > 100:
                print("Please enter a valid number between 10 and 100.")
                good_number = False
            else:
                good_number = True
        print()
        self.number_of_sticks = user_input

    def get_game_options(self):
        """Gets options for player or AI opponent."""
        user_input = ""
        good_number = False
        print("Options:")
        print(" Play against a friend (1)")
        print(" Play against the computer (2)")
        while not good_number:
            user_input = int(input("Which option do you take (1-2)? "))
            if user_input not in [1, 2]:
                print("Please enter a valid number for option.  Must be 1 or 2.")
                good_number = False
            else:
                good_number = True
        print()
        self.option = user_input

    def switch_player(self):
        """Switches the current player to the next one."""
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    def subtract_sticks(self, number_to_subtract):
        """Subtracts amount from total sticks."""
        self.number_of_sticks = self.number_of_sticks - number_to_subtract

    def game_start(self, player_one, player_two):
        """Starts game play and controls the flow."""
        won = False
        while not won:
            print("There are {} sticks on the board.".format(self.number_of_sticks))
            if self.current_player == 1:
                temp_sticks = player_one.player_chooses_sticks(self.current_player, self.number_of_sticks)
            else:
                temp_sticks = player_two.player_chooses_sticks(self.current_player, self.number_of_sticks)
            self.subtract_sticks(temp_sticks)
            if self.number_of_sticks == 0:
                if self.current_player == 2:
                    won = True
                    print("AI Player {}, you lose!".format(self.current_player))
                else:
                    won = True
                    print("Player {}, you lose!".format(self.current_player))
            else:
                won = False
                self.switch_player()

    def play_again(self):
        """Asks whether player wants to play again."""
        play_again = input("Play again (y/n)? ")
        if play_again.lower() == 'y':
            print()
            return True
        else:
            print()
            return False


class Player:
    """Controls decision of human player."""
    sticks_left = 0

    def __init__(self, sticks):
        """Initializes human controlled player with sticks for game and choices."""
        self.sticks_left = sticks

    def player_chooses_sticks(self, player_number, sticks_left):
        """Gets the number of sticks the human player wants to choose."""
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


class ComputerPlayer(Player):
    """Controls decision of computer controlled player."""

    def __init__(self, sticks):
        """Initializes computer controlled player with sticks for game and choices."""
        super().__init__(sticks)
        self.hats = Hat(sticks)

    def player_chooses_sticks(self, player_number, sticks_left):
        """Gets the number of sticks the AI player wants to choose."""
        user_input = 0
        good_number = False
        while not good_number:
            if sticks_left >= 3:
                print("AI Player {}: How many sticks do you take (1-3)?".format(player_number))
                user_input = self.hats.ai_sticks_to_take()
                print("The AI chose {} sticks.".format(user_input))
                if (user_input < 1) or (user_input > 3):
                    print("Please enter a valid number between 1 and 3.")
                    good_number = False
                else:
                    good_number = True
            elif sticks_left == 2:
                print("AI Player {}: How many sticks do you take (1-2)?".format(player_number))
                user_input = self.hats.ai_sticks_to_take()
                print("The AI chose {} sticks.".format(user_input))
                if (user_input < 1) or (user_input > 2):
                    print("Please enter a valid number between 1 and 2.")
                    good_number = False
                else:
                    good_number = True
            elif sticks_left == 1:
                print("AI Player {}: How many sticks do you take (1)?".format(player_number))
                user_input = self.hats.ai_sticks_to_take()
                print("The AI chose {} sticks.".format(user_input))
                if user_input != 1:
                    print("Please enter a valid number.  The only valid number now is 1.")
                    good_number = False
                else:
                    good_number = True
        print()
        return user_input


class Hat:
    """Keeps track of hats for a computer player."""
    hat_list = []
    content = [1, 2, 3]
    beside = []

    def __init__(self, num_of_sticks):
        """Initializes the hat object with list of contents."""
        count = 0
        while count <= num_of_sticks - 1:
            self.hat_list.append(self.content)
            self.beside.append([])
            count += 1

    def organize_hats(self, num_of_sticks, won, stick_chosen):
        """Manipulates hats for AI"""
        if won:
            self.beside[num_of_sticks].append(stick_chosen)
        else:
            del self.beside[num_of_sticks]

    def ai_sticks_to_take(self):
        """AI chooses the sticks to take"""
        return random.choice(self.content)


if __name__ == '__main__':
    """Run if file run directly."""
    playing = True
    while playing:
        game = Game()
        if game.option == 1:
            player1 = Player(game.number_of_sticks)
            player2 = Player(game.number_of_sticks)
        else:
            player1 = Player(game.number_of_sticks)
            player2 = ComputerPlayer(game.number_of_sticks)
        game.game_start(player1, player2)
        playing = game.play_again()
