from random import randint
from brain_games.cli import greet, welcome_user


def gcd():
    greet()
    print("Find the greatest common divisor of given numbers")
    print()
    name = welcome_user()
    print()
    attempt = 3
    while attempt != 0:
        a = randint(1, 100)
        b = randint(1, 100)
        print("Question: {} {}".format(a, b))
        result = int(input("Your answer: "))
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        answer = a + b
        if answer == result:
            print('Correct!')
            attempt -= 1
        else:
            print("'{}' is wrong answer ;(. \
Correct answer was '{}'.".format(result, answer))
            print("Let's try again!")
            break
    else:
        print("Congratulations, {}!".format(name))


if __name__ == "__main__":
    gcd()
