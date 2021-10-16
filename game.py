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


print("Welcome to the guessing game!")
player_name = input("What's your name? ")
print(f"{player_name}, I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")

num = random.randint(1, 100)

play_game = True

while play_game:
    tries = 0
    guess = int(input("Your guess? "))
    if guess == num:
        print(f"Well done, {player_name}! You found my number in {tries} tries!")
        play_game = False
    elif guess > num:
        print("Your guess is too high, try again.")
        tries += 1
    elif guess < num:
        print("Your guess is too low, try again.")
        tries += 1