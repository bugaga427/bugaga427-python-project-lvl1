from random import randint


DESCRIPTION = "What number is missing in the progression?"


def round():
    first = randint(0, 50)
    step = randint(1, 10)
    index = randint(0, 9)

    seq = list(range(first, first + (10 * step), step))
    answer = str(seq[index])
    seq[index] = '..'

    for item in seq:
        if item == seq[0]:
            question = str(item)
        else:
            question += ' ' + str(item)

    return question, answer
