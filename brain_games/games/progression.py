import secrets

from ..cli import is_correct_answer


def generate_progression(start: int, step: int, length: int) -> list[int]:
    return [start + step * i for i in range(length)]


def create_question(progression: list[int], hidden_index: int) -> str:
    question_parts = [
        str(num) if index != hidden_index else ".."
        for index, num in enumerate(progression)
    ]
    return " ".join(question_parts)


def correct_answer(progression: list[int], hidden_index: int) -> str:
    return str(progression[hidden_index])


def play_round() -> bool:
    MAX_NUMBER_START = 50
    MAX_NUMBER_STEP = 10
    LENGTH = 10
    
    start = secrets.randbelow(MAX_NUMBER_START) + 1
    step = secrets.randbelow(MAX_NUMBER_STEP) + 1
    hidden_index = secrets.randbelow(LENGTH)
    progression = generate_progression(start, step, LENGTH)
    question = create_question(progression, hidden_index)
    print(f"Question: {question}")
    user_answer = input("Your answer: ")
    return is_correct_answer(
        user_answer, 
        correct_answer(progression, hidden_index)
    )