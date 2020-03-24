from random import randint
from brain_games.cli import welcome_user, greet


def even():
    greet()
    print('Answer "yes" if number even otherwise answer "no".')
    print()
    name = welcome_user()
    print()
    attempt = 0

    while attempt < 3:
        number = randint(1, 100)
        print('Question: {}'.format(str(number)))
        answer = input('Your answer: ')

        if number % 2 == 0:
            result = 'yes'
        else:
            result = 'no'

        if answer == result:
            print('Correct!')
            attempt += 1
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again!")
            break

    else:
        print("Congratulations, {}!".format(name))


if __name__ == "__main__":
    even()
