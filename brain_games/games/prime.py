from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def round():
    number = randint(1, 100)
    question = str(number)
    
    choise = 0

    for i in range(2, number + 1):
        if number % i == 0:
            choise += 1

        if choise == 2:
            answer = 'yes'
        else:
            answer = 'no'

    return question, answer
