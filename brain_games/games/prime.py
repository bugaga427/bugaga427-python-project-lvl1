from random import randint
import math


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def new_round():
    question = randint(2, 100)

    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'

    return question, answer
