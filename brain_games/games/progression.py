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
    start = secrets.randbelow(50) + 1
    step = secrets.randbelow(10) + 1
    length = 10
    hidden_index = secrets.randbelow(length)
    progression = generate_progression(start, step, length)
    question = create_question(progression, hidden_index)
    print(f"Question: {question}")
    user_answer = input("Your answer: ")
    return is_correct_answer(
        user_answer, 
        correct_answer(progression, hidden_index)
    )