from brain_games.cli import engine, welcome_user
from brain_games.games.even import play_round


def brain_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    engine(play_round, name)


if __name__ == '__main__':
    brain_even()