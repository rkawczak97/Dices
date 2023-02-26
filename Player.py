from Dices import *

class Player:
    def __init__(self, dices: Dices, name: str='player') -> None:
        self.name = name
        self.score = self.init_score(dices)
        self.total_score = 0

    def init_score(self, dices: Dices):
        return {s: None for s in dices.get_sides()}

    def update_total_score(self):
        self.total_score = sum(self.score.values())

    def set_score(self, score: dict):
        self.score = score

    def get_score(self):
        return self.score
    
    def get_name(self):
        return self.name