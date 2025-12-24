import random

import prompt


def welcome_user() -> str:
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'''Hello, {name}!\nAnswer "yes" if the number is even, otherwise answer "no".''')  # noqa: E501
    return name


def correct_answer(number: int) -> str:
    return "yes" if number % 2 == 0 else "no"


def is_correct_answer(user_answer: str, correct_answer: str) -> bool:
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: E501
    return False


def play_round() -> bool:
    number = random.randint(1, 100)
    print(f"Question: {number}")
    user_answer = prompt.string("Your answer: ")
    return is_correct_answer(user_answer, correct_answer(number))


def main():
    name = welcome_user()
    wins_count = 0
    rounds_to_win = 3
    while wins_count < rounds_to_win:
        if play_round():
            wins_count += 1
        else:
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()