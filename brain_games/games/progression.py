from random import randint
from brain_games.cli import greet, welcome_user


def progression():
    greet()
    print("What number is missing in the progression?")
    print()
    name = welcome_user()
    print()
    attempt = 3

    while attempt > 0:
        first = randint(0, 50)
        step = randint(1, 10)
        index = randint(0, 9)

        seq = list(range(first, first + (10 * step), step))
        answer = seq[index]
        seq[index] = '..'

        question = "Question:"
        for item in seq:
            question += ' ' + str(item)

        print(question)
        result = int(input("Your answer: "))

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
    progression()
