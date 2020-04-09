from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def round():
    number = randint(2, 100)
    question = str(number)

    divisor = 0

    for i in range(2, number + 1):
        if number % i == 0:
            divisor += 1

        if divisor == 1:
            answer = 'yes'
        else:
            answer = 'no'

    return question, answer
