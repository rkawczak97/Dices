from Dices import *

class Game:
    def __init__(self, n_players: int=1, n_throws: int=3) -> None:
        self.n_players = n_players
        self.n_throws = n_throws
        self.player_score = dict()

    def play(self):
        d = Dices()
        self.player_score = {k: '-' for k in range(d.min_dice, d.max_dice+1)}
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
                # print current score
                # select score
            else:
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

    def select_score(self, dices: Dices):
        s = int(input('Select score: '))
        if self.player_score[s] == '-':
            self.player_score[s] = dices.score()[s]
        else:
            pass

    def display_score(self, dices: Dices):
        score = dices.score()
        print('SCORE: | ', end='')
        for k, v in score.items():
            if v == 0:
                score[k] = 'X'
            elif v > 0:
                score[k] = '+{}'.format(v)
            else:
                score[k] = str(v)
            print('{}: {} |'.format(k, v), end=' ')