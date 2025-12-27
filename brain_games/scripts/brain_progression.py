from brain_games.cli import engine
from brain_games.games.progression import play_round


def brain_progression(name: str = 'User'):
    print('What number is missing in the progression?')
    engine(play_round, name)


if __name__ == '__main__':
    brain_progression()