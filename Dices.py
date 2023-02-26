import random
from collections import Counter

class Dices:
    def __init__(self, n: int=5, sides: list=[1,2,3,4,5,6]) -> None:
        assert n >= 1, 'Number of dices must be greater then 0!'
        self.n = n
        self.sides = sides
        self.dices_throw = [None]*n
        self.dices_side = list()
        self.score = dict()

    def throw(self):
        n_dices = len(self.dices_throw)
        self.dices_throw = [random.choice(self.sides) for _ in range(n_dices)]
        self.update_score()

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
    
    def update_score(self):
        self.score = {s: s*(-3) for s in self.sides}
        counter = Counter(self.dices_side+self.dices_throw)
        for k in self.score.keys():
            self.score[k] += (k*counter[k])

    def reset(self):
        self.dices_throw = [None]*self.n
        self.dices_side = list()   

    def get_dices_throw(self):
        return self.dices_throw
    
    def get_dices_side(self):
        return self.dices_side
    
    def get_sides(self):
        return self.sides

    def get_score(self):
        return self.score