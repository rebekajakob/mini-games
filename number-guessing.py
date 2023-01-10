import random

NOT_INTEGER_MESSAGE = "The input should be an integer NUMBER! "
FROM_NUMBER_MESSAGE = "Please give the from number! "
TO_NUMBER_MESSAGE = "Please give the to number! "
SMALLER_FROM_MESSAGE = ["Please give a bigger number then ", "! "]
VICTORY_MESSAGE = "You're right! the number is "
SMALLER_MESSAGE = "Number is smaller!"
BIGGER_MESSAGE = "The number is bigger!"
GUESS_NUMBER_MESSAGE = "Please guess a number! "


def get_valid_number(input_text):
    valid = False
    input_guess = input(input_text)
    while not valid:
        try:
            int(input_guess)
            if input_guess.count(',') != 0 or input_guess.count('.') != 0:
                raise ValueError
        except ValueError:
            input_guess = input(NOT_INTEGER_MESSAGE)
        else:
            return int(input_guess)


def get_random_number():
    from_number = get_valid_number(FROM_NUMBER_MESSAGE)
    to_number = get_valid_number(TO_NUMBER_MESSAGE)
    while to_number <= from_number:
        to_number = get_valid_number(SMALLER_FROM_MESSAGE[0] + str(from_number) + SMALLER_FROM_MESSAGE[1])
    return random.randint(from_number, to_number)


def print_victory_message(guess):
    print(VICTORY_MESSAGE + str(guess))


def main_logic(guess, number_to_guess):
    while int(guess) != number_to_guess:
        if number_to_guess < int(guess):
            print(SMALLER_MESSAGE)
        else:
            print(BIGGER_MESSAGE)
        guess = get_valid_number(GUESS_NUMBER_MESSAGE)
    return guess


def number_guessing():
    number_to_guess = get_random_number()
    guess = get_valid_number(GUESS_NUMBER_MESSAGE)
    guess = main_logic(guess, number_to_guess)
    print_victory_message(guess)


if __name__ == '__main__':
    number_guessing()




