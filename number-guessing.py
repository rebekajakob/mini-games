import random


def get_valid_number(input_text):
    valid = False
    input_guess = input(input_text)
    while not valid:
        try:
            int(input_guess)
            if input_guess.count(',') != 0 or input_guess.count('.') != 0:
                raise ValueError
        except ValueError:
            input_guess = input("The input should be an integer NUMBER! ")
        else:
            return int(input_guess)


def get_random_number():
    from_number = get_valid_number("Please give the from number! ")
    to_number = get_valid_number("Please give the to number! ")
    while to_number <= from_number:
        to_number = get_valid_number("Please give a bigger number then " + str(from_number) + "! ")
    return random.randint(from_number, to_number)


def print_victory_message(guess):
    print("You're right! the number is " + str(guess))


def main_logic(guess, number_to_guess):
    while int(guess) != number_to_guess:
        if number_to_guess < int(guess):
            print("Number is smaller!")
        else:
            print("The number is bigger!")
        guess = get_valid_number("Please guess a number! ")


def number_guessing():
    number_to_guess = get_random_number()
    print(number_to_guess)
    guess = get_valid_number("Please guess a number! ")
    main_logic(guess, number_to_guess)
    print_victory_message(guess)




