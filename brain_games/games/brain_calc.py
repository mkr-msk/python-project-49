import secrets

import prompt

from ..cli import engine, is_correct_answer, welcome_user


def correct_answer(number_1: int, number_2: int, operation: str) -> str:
    match operation:
        case "+":
            return str(number_1 + number_2)
        case "-":
            return str(number_1 - number_2)
        case "*":
            return str(number_1 * number_2)
        

def play_round() -> bool:
    number_1 = secrets.randbelow(100) + 1
    number_2 = secrets.randbelow(100) + 1
    operation = secrets.choice(["+", "-", "*"])
    print(f"Question: {number_1} {operation} {number_2}")
    user_answer = prompt.string("Your answer: ")
    return is_correct_answer(
        user_answer, 
        correct_answer(number_1, number_2, operation)
        )


def brain_calc():
    name = welcome_user()
    print('What is the result of the expression?')
    engine(play_round, name)
