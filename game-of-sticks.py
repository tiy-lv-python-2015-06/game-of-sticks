
class Sticks:
    # sticks should keep track of how many stick total in play

    def __init__(self):
        self.valid_start_input = False
        self.sticks_picked_up = 0
        self.total_sticks_in_play = 0

    def set_start_values(self, start_sticks):

        self.total_sticks_in_play = start_sticks
        self.valid_start_input = True

    def decrease_num_sticks(self):
        if self.sticks_picked_up <= self.total_sticks_in_play:
            self.total_sticks_in_play -= self.sticks_picked_up

    def display_num_sticks(self):
        print('\nThere are {} sticks on the board.'.
              format(self.total_sticks_in_play))

    def check_start_range(self, user_input):
        # check that the starting number is between 10 and 100
        if 9 < user_input < 101:
            self.set_start_values(user_input)

    def check_pickup_range(self, user_input):
        if 0 < user_input < 4:
            self.sticks_picked_up = user_input
            self.decrease_num_sticks()

    def able_to_pickup(self, num_sticks, player):
        if self.total_sticks_in_play < num_sticks:
            print('Only {} sticks left. Try again.'.
                  format(self.total_sticks_in_play))

        player.picked_up = True




class Player:
    # player should keep track of if its their turn or not
    # player will have two sub-classes human & computer

    def __init__(self, name):
        self.name = name
        self.picked_up = False


class Game:

    def __init__(self, p1, p2):
        """When we init set the defaults to zero
           and let the user choose the number of sticks
        """
        self.sticks = Sticks()
        self.still_playing = True
        self.player1 = p1
        self.player2 = p2
        self.current_player = self.player1
        self.got_number = False

    def start_game(self):

        print('Welcome to the Game of Sticks!')

        # ask the player how many sticks to start
        while not self.sticks.valid_start_input:
            self.get_starting_sticks()

        print('There are {} sticks on the board.'.
            format(self.sticks.total_sticks_in_play))

        while self.still_playing:

            while not self.current_player.picked_up:
                self.ask_player_to_pickup()

            if self.still_playing:
                self.switch_player()
                self.sticks.display_num_sticks()

    def get_starting_sticks(self):
        start_num = input(
            'How many sticks are there on the table initially (10-100)?\n')

        while not self.got_number:
            self.check_valid_input(start_num)

        start_num = int(start_num)
        self.sticks.check_start_range(start_num)

        if self.sticks.valid_start_input:
            self.sticks.set_start_values(start_num)

    def check_valid_input(self, user_input):
        # check if the string is a positive or negative number
        self.got_number = False
        try:
            int(user_input)
            self.got_number = True
        except ValueError:
            print('Please enter a number in the desired range')


    def ask_player_to_pickup(self):
        pickup_num = input('{}: How many sticks do you take (1-3)?'.
                format(self.current_player.name))

        while not self.got_number:
            self.check_valid_input(pickup_num)

        pickup_num = int(pickup_num)
        self.sticks.check_pickup_range(pickup_num)
        self.sticks.able_to_pickup(pickup_num, self.current_player)

        self.still_playing_game()

    def still_playing_game(self):
        if self.sticks.total_sticks_in_play > 0:
            self.still_playing = True
        else:
            self.still_playing = False
            print('{} You lose!'.format(self.current_player.name))


    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player.picked_up = False
            self.current_player = self.player2
        else:
            self.current_player = self.player1


if __name__ == '__main__':

    player1 = Player('Bill')
    player2 = Player('Ted')

    game = Game(player1, player2)
    game.start_game()


