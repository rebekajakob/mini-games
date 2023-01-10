import random

number_to_guess = random.randint(0, 101)
print(number_to_guess)
guess = input("Please guess a number! ")

while int(guess) != number_to_guess:
    if number_to_guess < int(guess):
        print("Number is smaller!")
    else:
        print("The number is bigger!")
    guess = input("Please guess a number! ")

print("You're right! the number is " + guess)


