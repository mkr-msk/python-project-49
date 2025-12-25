import prompt

from ..games import brain_calc, brain_even


def main():
    print("Please choose a game to play:")
    print("1 - Even Number Game")
    print("2 - Calculator Game")
    choice = prompt.string("Enter the number of your choice: ")
    match choice:
        case "1":
            brain_even.brain_even()

        case "2":
            brain_calc.brain_calc()


if __name__ == '__main__':
    main()