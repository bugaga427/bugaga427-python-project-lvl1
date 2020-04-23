import prompt
from brain_games.cli import greet, welcome_user


def run(game, ROUND_OF_GAME=3):
    greet()
    print(game.DESCRIPTION)
    print()
    name = welcome_user()
    print()

    counter = 0

    while counter != ROUND_OF_GAME:
        question, correct_answer = game.round()
        print("Question: {}".format(question))
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            counter += 1
            print("Correct!")
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'".format(
                user_answer, correct_answer))
            print("Let's try again!")
            break
    else:
        print("Congratulations, {}".format(name))
