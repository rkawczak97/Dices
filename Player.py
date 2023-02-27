from Dices import *

class Player:
    def __init__(self, dices: Dices, name: str='player') -> None:
        self.name: str = name
        self.score: dict = self.init_score(dices)
        self.total_score: int = 0

    def init_score(self, dices: Dices):
        return {s: None for s in dices.get_sides()}

    def count_total_score(self):
        self.total_score = sum(self.score.values())

    def set_score(self, side: int, score: int):
        self.score[side] = score

    def get_score(self):
        return self.score

    def get_total_score(self):
        return self.total_score
    
    def get_name(self):
        return self.name