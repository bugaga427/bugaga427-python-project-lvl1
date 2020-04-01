from random import randint
from brain_games.cli import welcome_user, greet


def calc():
    greet()
    print("What is the result of the expression?")
    print()
    name = welcome_user()
    print()
    operators = ('+', '-', '*')
    attempt = 0

    while attempt < 3:
        first_operand = randint(1, 50)
        second_operand = randint(1, 50)
        index = randint(0, 2)
        print('Question: {} {} {}'.format(
                                    str(first_operand),
                                    operators[index],
                                    str(second_operand)))
        answer = input('Your answer: ')

        if operators[index] == '+':
            result = first_operand + second_operand
        elif operators[index] == '-':
            result = first_operand - second_operand
        elif operators[index] == '*':
            result = first_operand * second_operand

        if int(answer) == result:
            print('Correct!')
            attempt += 1
        else:
            print("'{}' is wrong answer ;(. \
Correct answer was '{}'".format(
                             answer,
                             str(result)))
            print("Let's try again")
            break

    else:
        print('Congratulation, {}!'.format(name))


if __name__ == '__main__':
    calc()
