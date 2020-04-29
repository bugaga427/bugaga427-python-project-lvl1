from random import randint


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def new_round():
    question = randint(1, 100)

    if question % 2 == 0:
        answer = "yes"
    else:
        answer = "no"

    return question, answer
