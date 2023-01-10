import random


def get_valid_number(input_text):
    valid = False
    input_guess = input(input_text)
    while not valid:
        try:
            int(input_guess)
        except ValueError:
            input_guess = input("The input should be an integer NUMBER! ")
        else:
            return int(input_guess)


number_to_guess = random.randint(0, 101)
print(number_to_guess)
guess = get_valid_number("Please guess a number! ")

while int(guess) != number_to_guess:
    if number_to_guess < int(guess):
        print("Number is smaller!")
    else:
        print("The number is bigger!")
    guess = get_valid_number("Please guess a number! ")

print("You're right! the number is " + str(guess))


