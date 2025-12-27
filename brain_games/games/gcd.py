import secrets

import prompt

from ..cli import is_correct_answer


def gcd(number_1: int, number_2: int) -> int:
    while number_2:
        number_1, number_2 = number_2, number_1 % number_2
    return number_1


def correct_answer(number_1: int, number_2: int) -> str:
    return str(gcd(number_1, number_2))


def play_round() -> bool:
    number_1 = secrets.randbelow(100) + 1
    number_2 = secrets.randbelow(100) + 1
    print(f"Question: {number_1} {number_2}")
    user_answer = prompt.string("Your answer: ")
    return is_correct_answer(
        user_answer,
        correct_answer(number_1, number_2)
    )