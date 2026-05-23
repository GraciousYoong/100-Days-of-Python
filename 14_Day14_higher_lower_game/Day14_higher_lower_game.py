import higher_lower_pics
import higher_lower_data
import random
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def compare() -> bool:
    compare_a = random.choice(list(higher_lower_data.data_set.keys()))
    compare_b = random.choice(list(higher_lower_data.data_set.keys()))
    while compare_a == compare_b:
        compare_b = random.choice(list(higher_lower_data.data_set.keys()))
    print(f"Compare A: {compare_a}, a {higher_lower_data.data_set[compare_a]['occupation']}, from {higher_lower_data.data_set[compare_a]['location']}.")
    print(higher_lower_pics.vs)
    print(f"Compare B: {compare_b}, a {higher_lower_data.data_set[compare_b]['occupation']}, from {higher_lower_data.data_set[compare_b]['location']}.")
    user_guess = input("Who has more followers? Type 'A' or 'B': ").capitalize()
    if user_guess == "A":
        if higher_lower_data.data_set[compare_a]['followers'] > higher_lower_data.data_set[compare_b]['followers']:
            return True
        else:
            return False
    elif user_guess == "B":
        if higher_lower_data.data_set[compare_b]['followers'] > higher_lower_data.data_set[compare_a]['followers']:
            return True
        else:
            return False
    else:
        return False
    
def higher_lower_game() -> None:
    final_score = 0
    clear_screen()
    print(higher_lower_pics.logo)
    while compare():
        final_score += 1
        clear_screen()
        print(higher_lower_pics.logo)
        print(f"You are right. Current score: {final_score}.")
    clear_screen()
    print(higher_lower_pics.logo)
    print(f"Sorry, that's wrong. Final score: {final_score}.")

higher_lower_game()