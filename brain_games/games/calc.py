from random import randint, choice
import operator


DESCRIPTION = 'What is the result of the expression?'
OPERATORS = ((operator.add, '+'), (operator.sub, '-'), (operator.mul, '*'))


def new_round():
    first_number = randint(1, 25)
    second_number = randint(1, 25)
    operator, char = choice(OPERATORS)

    question = '{} {} {}'.format(first_number, char, second_number)
    answer = operator(first_number, second_number)

    return question, str(answer)
