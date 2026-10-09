# Number Guessing Game
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("----- NUMBER GUESSING GAME -----")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Guess a number: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:

            print("****************************")
            print("That number is out of range.")
            print("****************************")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again.")
        elif guess > answer:
            print("Too high! Try again.")
        else:
            print("*****************************")
            print("You guessed correctly!")
            print(f"Number of guesses: {guesses}")
            print("*****************************")
            is_running = False
    else:
        print("***************")
        print("Invalid guess!")
        print("***************")
        print(f"Please select a number between {lowest_num} and {highest_num}")