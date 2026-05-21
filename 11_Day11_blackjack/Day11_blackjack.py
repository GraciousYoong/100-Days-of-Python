import random
import blackjack_pics
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pull_card() -> int:
    cards = [11, 2, 3, 4, 5, 6, 7 , 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards: list) -> int:
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score: int, computer_score:int) -> str:
    if user_score > 21:
        return "You went over 21. You busted. You lose 😵"
    elif computer_score > 21:
        return "Computer busted. You win 🎉"
    elif user_score == computer_score:
        return "It's a draw 🤝"
    elif computer_score == 0:
        return "Computer has Blackjack. You lose 💀"
    elif user_score == 0:
        return "Blackjack! You win 🂡🔥"
    elif user_score > computer_score:
        return "You win 🎉 Your hand is stronger"
    else:
        return "You lose 😢 Computer wins"
    
def blackjack() -> None:
    clear_screen()
    print(blackjack_pics.logo)
    user_cards = []
    computer_cards = []
    card_pulled = 0
    for _ in range(2):
        user_cards.append(pull_card())
        computer_cards.append(pull_card())
    should_continue = True
    computer_first_card = computer_cards[0]
    while should_continue == True:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        if user_score == 0 or computer_score == 0 or user_score > 21:
            should_continue = False
        else:
            print(f"    Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
            print(f"    Computer first card: {computer_first_card}")
            if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
                card_pulled = pull_card()
                user_cards.append(card_pulled)
            else:
                should_continue = False
    while computer_score != 0 and computer_score < 17 :
            computer_cards.append(pull_card())
            computer_score = calculate_score(computer_cards)
    print(f"    Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
    print(f"    Computer final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
    print(compare(user_score, computer_score))
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        blackjack()

if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    blackjack()