from brain_games.cli import engine, welcome_user
from brain_games.games.gcd import play_round


def brain_gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    engine(play_round, name)


if __name__ == '__main__':
    brain_gcd()