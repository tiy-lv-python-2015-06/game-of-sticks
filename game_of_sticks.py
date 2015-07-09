import random


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.sticks_left = sticks_left.initial_sticks


    def play(self):
        while self.sticks_left > 0:
            self.sticks_left -= self.current_player.remove_sticks(current_sticks=self.sticks_left)
            if self.current_player == self.player1:
                self.current_player = self.player2
            else:
                self.current_player = self.player1
        if self.current_player == self.player1:
            self.player1.teach(win=True)
            self.player2.teach(win=False)
        else:
            self.player1.teach(win=False)
            self.player2.teach(win=True)
        # print('{} Wins!'.format(self.current_player.name))



class Player:
    name = None
    win = 0
    def __init__(self, name):
        self.name = name

    def teach(self, win):
        if win:
            self.win += 1

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
    def __init__(self, training):
        self.name = 'Smart'
        self.training = training
        # self.hats = self.create_hats()
        self.hats = {x: Hat() for x in range(1, sticks_left.initial_sticks + 1)}
        self.current_hat = None
        self.win = 0

    def remove_sticks(self, current_sticks):
        hat = self.hats.get(current_sticks)
        remove_sticks = hat.grab_ball()
        if self.training:
            return remove_sticks
        else:
            print('There are {} Sticks Left'.format(current_sticks))
            print("The computer has removed {} sticks".format(remove_sticks))
            return remove_sticks


    def teach(self, win=True):
        if win:
            self.win +=1
        for x in self.hats:
            self.hats.get(x).learn(win)



class DumbAI(Player):
    def __init__(self, training):
        self.name = 'Dumb'
        self.training = training
        # self.hats = self.create_hats()
        self.hats = {x: Hat() for x in range(1, (sticks_left.initial_sticks + 1))}
        self.current_hat = None
        self.win = 0

    def remove_sticks(self, current_sticks):
        remove_sticks = random.choice(range(1,4))
        if self.training:
            return remove_sticks
        else:
            print('There are {} Sticks Left'.format(current_sticks))
            print("The computer has removed {} sticks".format(remove_sticks))
            return remove_sticks


    def teach(self, win=True):
        if win:
            self.win +=1



class Sticks:
    def __init__(self):
        print('How many Sticks would you like to start with (10-100)?\n')
        self.initial_sticks = int(input('Please enter a number between 10-100\n'))
        while 10 > self.initial_sticks or self.initial_sticks > 100:
            self.initial_sticks = int(input('Please enter a number between 10-100\n'))


class Hat:
    def __init__(self):
        self.list_of_balls = [1, 2, 3]
        self.guessed_ball = 0

    def grab_ball(self):
        while self.guessed_ball == 0:
            self.guessed_ball = random.choice(self.list_of_balls)
        return self.guessed_ball

    def learn(self, win=True):

        if self.guessed_ball == 0:
            pass
        elif win:
            self.list_of_balls.append(self.guessed_ball)
        else:
            self.list_of_balls.remove(self.guessed_ball)
            for x in range(1,4):
                if x not in self.list_of_balls:
                    self.list_of_balls.append(x)
        # print(self.list_of_balls)

    def __str__(self):
        return "Ball: Ball List:{}".format(self.list_of_balls)


# def train_ai(playerone, playertwo):
#     for x in range(1,10):
#         game = Game(playerone, playertwo)
#         game.play()
#         print('playing')


if __name__ == '__main__':
    print('Welcome to the Game of Sticks')
    game_mode = input(
        "Please select a game mode:\n1: Player vs Player\n2: Player vs Computer (untrained)\n3: Player vs Computer (trained)\n")
    sticks_left = Sticks()
    #Make this two functions...(3, if you count the training
    while True:
        if game_mode == '1':
            player1 = Player(input('Please Enter a name for Player 1\n'))
            player2 = Player(input('Please Enter a name for Player 2\n'))
            break
        elif game_mode == '2':
            player1 = Player(input('Please Enter a name for the player\n'))
            player2 = AI(training=False)
            break
        elif game_mode == '3':
            player1 = DumbAI(training=True)
            player2 = AI(training=True)
            while True:
                for x in range(1,100000):
                    game = Game(player1, player2)
                    game.play()
                print('{} has won {} wins'.format(player1.name, player1.win))
                print('{} has won {} wins'.format(player2.name, player2.win))
                again = input('Train again?')
                if again == 'n':
                    break
                else:
                    continue
            # train_ai(player1,player2)
            player2.training=False
            player1 = Player(input('Please Enter a name for the player\n'))
            break
        else:
            print('Please enter a Valid Game Choice (1,2,3)\n')

    stop = 'n'
    while stop != 'y':
        game = Game(player1, player2)
        game.play()
        stop = input('stop? y or n')
