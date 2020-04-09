from random import randint


DESCRIPTION = "Find the greatest common divisor of given numbers."


def round():
    first_number = randint(1, 50)
    second_number = randint(1, 50)
    question = '{} {}'.format(str(first_number), str(second_number))

    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number

        answer = str(first_number + second_number)

    return question, answer
