import secrets

import prompt

from ..cli import engine, is_correct_answer, welcome_user


def correct_answer(number: int) -> str:
    return "yes" if number % 2 == 0 else "no"


def play_round() -> bool:
    number = secrets.randbelow(100) + 1
    print(f"Question: {number}")
    user_answer = prompt.string("Your answer: ")
    return is_correct_answer(user_answer, correct_answer(number))


def brain_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    engine(play_round, name)