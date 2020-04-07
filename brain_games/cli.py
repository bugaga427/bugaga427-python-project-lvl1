import prompt


def greet():
    print("Welcome to the Brain Games!", end="\n\n")


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


if __name__ == '__main__':
    welcome_user()
    greet()
