from random import randint


DESCRIPTION = 'What is the result of the expression?'


def round():
    operators = ('+', '-', '*')

    first_number = randint(1, 25)
    second_number = randint(1, 25)
    index = randint(0, 2)

    if first_number < second_number and index == 1:
        first_number, second_number = second_number, first_number

    question = '{} {} {}'.format(first_number, operators[index], second_number)

    if index == 0:
        answer = str(first_number + second_number)
    elif index == 1:
        answer = str(first_number - second_number)
    elif index == 2:
        answer = str(first_number *  second_number)

    return question, answer
