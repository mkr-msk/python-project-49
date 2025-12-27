import prompt


def welcome_user() -> str | None:
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def is_correct_answer(user_answer: str | None, correct_answer: str) -> bool:
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: E501
    return False


def engine(play_round, name) -> None:
    wins_count = 0
    rounds_to_win = 3
    while wins_count < rounds_to_win:
        if play_round():
            wins_count += 1
        else:
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")