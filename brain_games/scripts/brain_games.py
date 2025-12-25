import prompt

from ..games import brain_calc, brain_even, brain_gcd, brain_progression


def main():
    print("Please choose a game to play:")
    print("1 - Even Number Game")
    print("2 - Calculator Game")
    print("3 - Greatest Common Divisor Game")
    print("4 - Arithmetic Progression Game")
    choice = prompt.string("Enter the number of your choice: ")
    match choice:
        case "1":
            brain_even.brain_even()

        case "2":
            brain_calc.brain_calc()

        case "3":
            brain_gcd.brain_gcd()

        case "4":
            brain_progression.brain_progression()


if __name__ == '__main__':
    main()