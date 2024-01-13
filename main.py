# Welcome to the Number Guessing Game!
# I'm thinking of a number between 1 and 100.
# Choose a difficulty. type 'easy' or 'hard':
# You have 10 attempts remainig to guess the number.
# Make a guess:
# Too high.
# Guess again
# Too low.
# Guess again

from random import randint
guess = randint(1, 100)


def set_difficulty():
    difficulty = input("Choose a difficulty. type 'easy' or 'hard': ")
    if difficulty == "hard":
        return 5
    else:
        return 10


def check_answer():
    answer = int(input("Make a guess:"))
    if answer > guess:
        print("Too high")
        return "Too high"
    elif guess > answer:
        print("Too low")
        return "Too low"
    else:
        print(f"You got it! The answer was {answer}")
        return "win"


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

attempts = set_difficulty()

for _ in range(0, attempts):
    result = check_answer()
    if result == "win":
        break
