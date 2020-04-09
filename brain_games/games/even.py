from random import randint


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def round():
    question = randint(1, 100)

    if question % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    return str(question), answer
