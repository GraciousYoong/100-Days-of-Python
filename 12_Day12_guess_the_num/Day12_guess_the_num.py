import guess_num_pics
import random

print(guess_num_pics.logo)

def number_compare(target_num:int) -> bool:
    guessed_num = int(input("Make a guess: "))
    if target_num > guessed_num:
        print("Too low.")
        return False
    elif target_num < guessed_num:
        print("Too high.")
        return False
    else:
        print(f"You got it! The answer was {target_num}.")
        return True

def number_guessing_game() -> None:
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while mode != "easy" and mode != "hard":
        mode = input("Please enter 'easy' or 'hard' to choose difficultly.")
    target_num= random.randint(1, 100)
    if mode == "easy":
        attempts = 10
    else:
        attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
    while attempts > 0 and number_compare(target_num) == False:
        attempts -=1
        if attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            print("Guess again.")
        else:
            print(f"You've run out of guesses. The answer was {target_num}.")

number_guessing_game()
