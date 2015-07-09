import random
import collections


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = random.choice([player1, player2])
        print('Welcome to the Game of Sticks')
        self.sticks_left = sticks_left.initial_sticks
        print(player2.hats.get(0))

    def play(self):
        while self.sticks_left > 0:
            self.sticks_left -= self.current_player.remove_sticks(current_sticks=self.sticks_left)
            if self.current_player == self.player1:
                self.current_player = self.player2
        try:
            if self.current_player == self.player1:
                self.player1.teach(win=True)
                self.player2.teach(win=False)
            else:
                player1.teach(win=False)
                player2.teach(win=True)
        except:
            pass
        print('{} Wins!'.format(self.current_player.name))


class Player:
    name = None

    def __init__(self, name):
        self.name = name

    def remove_sticks(self, remove_sticks=None, current_sticks=None):
        print('It is {}\'s Turn'.format(self.name))
        print('There are {} Sticks Left'.format(current_sticks))
        print('How many Sticks would you like to remove?\n')
        while remove_sticks is None and current_sticks >= 4:
            remove_sticks = input('Please enter a number between 1-3\n')
            try:
                if 3 >= int(remove_sticks) >= 1:
                    return int(remove_sticks)
                else:
                    remove_sticks = None
                    continue
            except:
                remove_sticks = None
                continue
        while current_sticks <= 3:
            remove_sticks = input('Please enter a number between 1-{}\n'.format(current_sticks, ))
            try:
                if current_sticks >= int(remove_sticks) >= 1:
                    return int(remove_sticks)
                else:
                    continue
            except:
                continue


class AI(Player):
    def __init__(self):
        self.name = 'CPU'
        self.training = False
        # self.hats = self.create_hats()
        self.hats = {x: Hat for x in range(sticks_left.initial_sticks)}

    def remove_sticks(self, current_sticks):
        self.current_hat = self.hats.get(current_sticks - 1)
        print(self.current_hat)
        self.remove_sticks = self.current_hat.takes_guess()
        # remove_sticks = self.hats.get(current_sticks).takes_guess()
        if self.training:
            return remove_sticks
        else:
            print('There are {} Sticks Left'.format(current_sticks))
            print("The computer has removed {} sticks".format(remove_sticks))
            return remove_sticks

    # def create_hats(self):
    #     global sticks_left
    #     return {x: Hat for x in range(sticks_left.initial_sticks)}

    def teach(self, win=True):
        for x in self.hats:
            hat.learn(win)


class Sticks:
    def __init__(self):
        print('How many Sticks would you like to start with (10-100)?\n')
        self.initial_sticks = int(input('Please enter a number between 10-100\n'))
        while 10 > self.initial_sticks or self.initial_sticks > 100:
            self.initial_sticks = int(input('Please enter a number between 10-100\n'))


class Hat:
    def __init__(self):
        self.list_of_balls = [1, 2, 3]

    def takes_guess(self):
        self.guessed_ball = random.choice(self.list_of_balls)
        return self.guessed_ball

    def learn(self, win=True):
        if win:
            self.list_of_balls.append(self.guessed_ball)
        else:
            self.list_of_balls.remove(self.guessed_ball)
        self.list_of_balls.append(x for x in range(1, 3) if x not in self.list_of_balls)


if __name__ == '__main__':
    game_mode = input(
        "Please select a game mode:\n1: Player vs Player\n2: Player vs Computer (untrained)\n3: Player vs Computer (trained)\n")
    sticks_left = Sticks()
    while True:
        if game_mode == '1':
            player1 = Player(input('Please Enter a name for Player 1\n'))
            player2 = Player(input('Please Enter a name for Player 2\n'))
            break
        elif game_mode == '2':
            player1 = Player(input('Please Enter a name for the player\n'))
            player2 = AI()
            break
        elif game_mode == '3':
            Train_ai()
            player1 = Player(input('Please Enter a name for the player\n'))
            player2 = AI()
        else:
            print('Please enter a Valid Game Choice (1,2,3)\n')



    game = Game(player1, player2)
    game.play()
