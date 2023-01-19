NUMBER_OF_GAMES = 2
WELCOME_MESSAGE = "Hello, welcome to my little gaming program. I hope you will enjoy it!"
CHOOSE_GAME_MESSAGE = "Choose from the games below!"
MENU_POINTS = "1. Number guessing \n2. 2048"
CHOOSE_NUMBER_MESSAGE = "Please choose a number! "
WRONG_INPUT_MESSAGE = "Please choose a valid number"


def welcome_message():
    print(WELCOME_MESSAGE)


def menu():
    print(CHOOSE_GAME_MESSAGE)
    print(MENU_POINTS)
    valid = False
    input_guess = input(CHOOSE_NUMBER_MESSAGE)
    while not valid:
        try:
            int(input_guess)
            if input_guess not in range(1, NUMBER_OF_GAMES + 1):
                raise ValueError
        except ValueError:
            input_guess = input(WRONG_INPUT_MESSAGE)
        else:
            return int(input_guess)
