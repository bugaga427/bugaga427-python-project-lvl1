from random import randint


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def new_round():
    question = randint(1, 100)

    if is_even(question):
        answer = "yes"
    else:
        answer = "no"

    return question, answer
