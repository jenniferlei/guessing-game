"""A number-guessing game."""

# greet player
# get player name
# choose random number between 1 and 100
# repeat forever:
#     get guess
#     if guess is incorrect:
#         give hint
#         increase number of guesses
#     else:
#         congratulate player

import random

def guess_input():
    '''determines if user input a valid number equal or between 1 and 100.
    returns the guess if valid'''
    while True:
        guess = input("Your guess? ")

        if guess.isnumeric():
            guess = int(guess)
            if guess > 0 and guess < 101:
                return guess

        print("How dare you. That is an invalid input. Please try again.")




print("Welcome to the guessing game!")
player_name = input("What's your name? ")
print(f"{player_name}, I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")

num = random.randint(1, 100)

play_game = True
tries = 0


while play_game:
    guess = guess_input()
    if guess == num:
        tries += 1
        print(f"Well done, {player_name}! You found my number in {tries} tries!")
        play_game = False
    elif guess > num:
        print("Your guess is too high, try again.")
        tries += 1
    elif guess < num:
        print("Your guess is too low, try again.")
        tries += 1
    


