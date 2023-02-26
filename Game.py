from Dices import *
from Player import *

class Game:
    def __init__(self, n_players: int=1, n_throws: int=3) -> None:
        self.n_players = n_players
        self.n_throws = n_throws

    def play(self):
        d = Dices()
        name = input('Type player name: ')
        p = Player(d, name)
        while True:
            t = input('Throw dices [y/n]?: ')
            if t.lower() == 'y':
                for t in range(self.n_throws):
                    d.throw()
                    print('({}/{}) T: {}'.format(t+1, self.n_throws, d.get_dices_throw()))
                    self.select_dices_to_keep(d, t)
                    self.select_dices_to_return(d, t)
                    print('({}/{}) S: {}'.format(t+1, self.n_throws, d.get_dices_side()))
                self.display_score(d)
                self.display_player_score(p)
                self.select_score(d, p)
            else:
                self.display_player_score(p)
                print('Closing the game...')
                break
            d.reset()

    def select_dices_to_keep(self, dices: Dices, throw: int):
        k = input('({}/{}) Select dices to keep: '.format(throw+1, self.n_throws))
        if k != '':
            idx = [int(x)-1 for x in k.split()]
            dices.keep(idx)
    
    def select_dices_to_return(self, dices: Dices, throw: int):
        k = input('({}/{}) Select dices to return: '.format(throw+1, self.n_throws))
        if k != '':
            idx = [int(x)-1 for x in k.split()]
            dices.back(idx)

    def display_score(self, dices: Dices):
        score = dices.get_score()
        print('SCORE: | ', end='')
        for k, v in score.items():
            if v == 0:
                score[k] = 'X'
            elif v > 0:
                score[k] = '+{}'.format(v)
            else:
                score[k] = str(v)
            print('{}: {} |'.format(k, score[k]), end=' ')
        print('\n', end='')
    
    def select_score(self, dice: Dices, player: Player):
        s = int(input('Choose score: '))
        if player.get_score()[s] == None:
            player.get_score()[s] = dice.get_score()[s]
        else:
            print('Choose again...')
            return self.select_score(dice)

    def display_player_score(self, player: Player):
        print('{}: | '.format(player.get_name()), end='')
        for k, v in player.get_score().items():
            print('{}: {} |'.format(k, v), end=' ')
        print('\n', end='')