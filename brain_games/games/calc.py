import secrets

from ..cli import is_correct_answer


def correct_answer(number_1: int, number_2: int, operation: str):
    match operation:
        case "+":
            return str(number_1 + number_2)
        case "-":
            return str(number_1 - number_2)
        case "*":
            return str(number_1 * number_2)
        

def play_round() -> bool:
    MAX_NUMBER = 100
    number_1 = secrets.randbelow(MAX_NUMBER) + 1
    number_2 = secrets.randbelow(MAX_NUMBER) + 1
    operation = secrets.choice(["+", "-", "*"])
    print(f"Question: {number_1} {operation} {number_2}")
    user_answer = input("Your answer: ")
    return is_correct_answer(
        user_answer, 
        correct_answer(number_1, number_2, operation)  # type: ignore
    )
