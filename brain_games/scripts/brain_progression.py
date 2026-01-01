from brain_games.cli import engine, welcome_user
from brain_games.games.progression import play_round


def brain_progression():
    name = welcome_user()
    print('What number is missing in the progression?')
    engine(play_round, name)


if __name__ == '__main__':
    brain_progression()