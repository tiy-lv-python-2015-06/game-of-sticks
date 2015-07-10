import random


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

    def able_to_pickup(self, num_sticks, player):
        print('total sticks in play {} and your asking to pick up {}'.
              format(self.total_sticks_in_play, num_sticks))
        if self.total_sticks_in_play < num_sticks:
            print('Only {} sticks left. Try again.'.
                  format(self.total_sticks_in_play))
        else:
            if 0 < num_sticks < 4:
                self.sticks_picked_up = num_sticks
                self.decrease_num_sticks()

            player.picked_up = True


class Player:
    # player should keep track of if its their turn or not
    # player will have two sub-classes human & computer

    def __init__(self, name):
        self.name = name
        self.picked_up = False
        self.won = False
        self.win_count = 0

    def increment_win_count(self):
        self.win_count += 1


class ComputerPlayer(Player):

    def __init__(self, name):
        super().__init__(name)

        # make a hat for each possible guess
        self.hat = {x: Hat(x) for x in range(0, 101)}

    def get_num_sticks(self, hat_num):
        #pu = random.choice(range(1, 4))

        cnt = random.choice(self.hat[hat_num].inside_balls)

        # cnt = max(cnt1, cnt2, cnt3)

        self.hat[hat_num].chosen_ball = cnt
        #print('the computer is picking up {} sticks'.format(cnt))

        return cnt

    def update_hat(self, is_winner):

        for each in range(len(self.hat)):
            if self.hat[each].chosen_ball != 0:
                if is_winner:
                    self.hat[each].inside_balls.\
                        append(self.hat[each].chosen_ball)

                    #print('we are appending this ball {}'.
                          #format(self.hat[each].chosen_ball))
                else:
                    if self.hat[each].inside_balls.count(
                            self.hat[each].chosen_ball) > 1:
                        #print('we lost and there is more than '
                        #      'one of these balls'
                        #      'in here so we are deleting one')
                        indx = self.hat[each].inside_balls.\
                            index(self.hat[each].chosen_ball)
                        del self.hat[each].inside_balls[indx]
                        #print(str(self.hat[each]))


class Hat():

    def __init__(self, index):
        self.inside_balls = [1, 2, 3]
        self.chosen_ball = 0
        self.number = index

    def __str__(self):
        return "inside_balls: {} chosen_ball:{}".\
            format(self.inside_balls, self.chosen_ball)


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
        # start_num = input(
        #    'How many sticks are there on the table initially (10-100)?\n')
        start_num = 20

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
        # if theres a human let them pick
        if type(self.current_player) == Player:
            pickup_num = random.choice(range(1, 4))
        #     pickup_num = input('{}: How many sticks do you take (1-3)?'.
        #                 format(self.current_player.name))
        #     # this checks if the number is valid won't need for computer play
        #     while not self.got_number:
        #         self.check_valid_input(pickup_num)
        #
        #     pickup_num = int(pickup_num)
        # # otherwise call the computers method to pick
        else:
            pickup_num = self.current_player.get_num_sticks(
                self.sticks.total_sticks_in_play)

        # check if the input is within the range and we have that many
        # sticks available to pickup
        self.sticks.able_to_pickup(pickup_num, self.current_player)

        # check if we are still playing
        self.still_playing_game()

    def still_playing_game(self):
        if self.sticks.total_sticks_in_play > 0:
            self.still_playing = True
        else:
            self.still_playing = False
            if self.current_player == self.player1:
                self.player1.won = False
                self.player2.won = True
                self.player2.increment_win_count()

                # after the game end update the computer hat
                if type(self.current_player) == ComputerPlayer:
                    self.current_player.update_hat(self.current_player.won)
                else:
                    self.player2.update_hat(self.player2.won)
            else:
                self.player2.won = False
                self.player1.won = True
                self.player1.increment_win_count()

                # after the game end update the computer hat
                if type(self.current_player) == ComputerPlayer:
                    self.current_player.update_hat(self.current_player.won)
            print('{} You lose!'.format(self.current_player.name))


    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

        self.current_player.picked_up = False


if __name__ == '__main__':

    gm_cnt = 0

    print('Welcome to the Game of Sticks!')

    player1 = Player('Bill')
    #player2 = Player('Ted')
    player2 = ComputerPlayer('Bot')

    while gm_cnt < 10000:
        game = Game(player1, player2)
        game.start_game()

        print('{}:  win count {}  {}:  win count {}'
          .format(player1.name, player1.win_count,
          player2.name, player2.win_count))

        print('game number {}'.format(gm_cnt))
        gm_cnt += 1

