from brain_games.cli import engine
from brain_games.games.calc import play_round


def brain_calc(name: str = 'User'):
    print('What is the result of the expression?')
    engine(play_round, name)


if __name__ == '__main__':
    brain_calc()