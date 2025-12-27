import brain_calc
import brain_even
import brain_gcd
import brain_prime
import brain_progression
import prompt


def main():
    print("Please choose a game to play:")
    print("1 - Even Number Game")
    print("2 - Calculator Game")
    print("3 - Greatest Common Divisor Game")
    print("4 - Arithmetic Progression Game")
    print("5 - Prime Number Game")
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
        case "5":
            brain_prime.brain_prime()


if __name__ == '__main__':
    main()