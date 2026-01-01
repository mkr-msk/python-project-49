import secrets

from ..cli import is_correct_answer


def correct_answer(number: int) -> str:
    return "yes" if number % 2 == 0 else "no"


def play_round() -> bool:
    MAX_NUMBER = 100
    number = secrets.randbelow(MAX_NUMBER) + 1
    print(f"Question: {number}")
    user_answer = input("Your answer: ")
    return is_correct_answer(user_answer, correct_answer(number))
