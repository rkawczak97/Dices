import random
from collections import Counter

class Dices:
    def __init__(self, n: int=5, min_dice: int=1, max_dice: int=6) -> None:
        assert n >= 1, 'Number of dices must be greater then 0!'
        self.n = n
        self.dices_throw = [None]*n
        self.dices_side = list()
        self.min_dice = min_dice
        self.max_dice = max_dice

    def throw(self):
        n_dices = len(self.dices_throw)
        if n_dices <= 0:
            print('No dices to throw!')
        else:
            self.dices_throw = [random.randint(self.min_dice , self.max_dice) for _ in range(n_dices)]

    def keep(self, idx: list):
        idx = sorted(idx)[::-1]
        for i in idx:
            self.dices_side.append(self.dices_throw[i])
            self.dices_throw.pop(i)

    def back(self, idx: list):
        idx = sorted(idx)[::-1]
        for i in idx:
            self.dices_throw.append(self.dices_side[i])
            self.dices_side.pop(i)
    
    def score(self):
        score = {k: k*(-3) for k in range(self.min_dice, self.max_dice+1)}
        counter = Counter(self.dices_side + self.dices_throw)
        tmp = {k: k*((-3)+v) for k, v in counter.items()}
        for k, v in tmp.items():
            score[k] = v
        return score

    def reset(self):
        self.dices_throw = [None]*self.n
        self.dices_side = list()

    def get_dices_throw(self):
        return self.dices_throw
    
    def get_dices_side(self):
        return self.dices_side