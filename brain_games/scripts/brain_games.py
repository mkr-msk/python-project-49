import prompt

from brain_games.cli import welcome_user

from . import brain_calc, brain_even, brain_gcd, brain_prime, brain_progression


def main():
    name = welcome_user()
    print("Please choose a game to play:")
    print("1 - Even Number Game")
    print("2 - Calculator Game")
    print("3 - Greatest Common Divisor Game")
    print("4 - Arithmetic Progression Game")
    print("5 - Prime Number Game")
    choice = prompt.string("Enter the number of your choice: ")
    match choice:
        case "1":
            brain_even.brain_even(name)
        case "2":
            brain_calc.brain_calc(name)
        case "3":
            brain_gcd.brain_gcd(name)
        case "4":
            brain_progression.brain_progression(name)
        case "5":
            brain_prime.brain_prime(name)


if __name__ == '__main__':
    main()