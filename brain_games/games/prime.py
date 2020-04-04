from random import randint
from brain_games.cli import greet, welcome_user


def prime():
    greet()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print()
    name = welcome_user()
    print()
    attempt = 3

    while attempt > 0:
        number = randint(2, 100)
        counter = 0
        print('Question: {}'.format(number))
        answer = input("Your answer: ")

        for i in range(1, number + 1):
            if number % i == 0:
                counter += 1

        if counter == 2:
            result = 'yes'
        else:
            result = 'no'

        if answer == result:
            print('Correct!')
            attempt -= 1
        else:
            print("'{}' is wrong answer ;(. \
Correct answer was '{}'.".format(answer, result))
            print("Let's try again!")
            break
    else:
        print("Congratulations, {}!".format(name))


if __name__ == "__main__":
    prime()
