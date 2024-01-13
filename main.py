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

difficulty = "easy"
attempts = 10
random_number = 50
userNumber = 0
win = False
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. type 'easy' or 'hard': ")

if difficulty == "hard":
    attempts = 5

random_number = randint(1,100)

for _ in range(0,attempts):
    userNumber = int(input("Make a guess: "))
    if userNumber > random_number:
        print("Too high")
    if userNumber < random_number:
        print("Too low")
    if userNumber == random_number:
        print("You win")
        win = True
        break


    

