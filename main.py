from Game import *

if __name__ == '__main__':
    n_players = int(input('Type number of players: '))
    g = Game(n_players=n_players)
    g.play()
    