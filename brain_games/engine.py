import prompt
from brain_games.cli import greet, welcome_user


def run(game, round_of_game=3):
    greet()
    print(game.DESCRIPTION)
    print()
    name = welcome_user()
    print()

    counter = 0

    while counter != round_of_game:
        question, correct_answer = game.new_round()
        print("Question: {}".format(question))
        user_answer = prompt.string("Your answer: ")
        if user_answer != correct_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'".format(
                user_answer, correct_answer))
            print("Let's try again!")
            break 
        counter += 1
        print("Correct!")
    else:
        print("Congratulations, {}".format(name))
