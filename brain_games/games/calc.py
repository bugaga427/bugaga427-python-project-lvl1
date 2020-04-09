from random import randint, choice
from operator import add, sub, mul


DESCRIPTION = 'What is the result of the expression?'


def round():
    OPERATORS = ((add, '+'), (sub, '-'), (mul, '*'))

    first_number = randint(1, 25)
    second_number = randint(1, 25)
    operator, char = choice(OPERATORS)

    if first_number < second_number and char == '-':
        first_number, second_number = second_number, first_number

    question = '{} {} {}'.format(str(first_number), char, str(second_number))
    answer = str(operator(first_number, second_number))

    return question, answer
