from brain_games.cli import engine
from brain_games.games.prime import play_round


def brain_prime(name: str = 'User'):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    engine(play_round, name)


if __name__ == '__main__':
    brain_prime()