import secrets

import prompt

from ..cli import engine, is_correct_answer, welcome_user


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def correct_answer(number: int) -> str:
    return "yes" if is_prime(number) else "no"


def play_round() -> bool:
    number = secrets.randbelow(100) + 1
    print(f"Question: {number}")
    user_answer = prompt.string("Your answer: ")
    return is_correct_answer(user_answer, correct_answer(number))


def brain_prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    engine(play_round, name)