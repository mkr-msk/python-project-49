from brain_games.cli import engine
from brain_games.games.even import play_round


def brain_even(name: str = 'User'):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    engine(play_round, name)


if __name__ == '__main__':
    brain_even()