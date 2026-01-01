import secrets

from ..cli import is_correct_answer


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
    MAX_NUMBER = 100
    number = secrets.randbelow(MAX_NUMBER) + 1
    print(f"Question: {number}")
    user_answer = input("Your answer: ")
    return is_correct_answer(user_answer, correct_answer(number))