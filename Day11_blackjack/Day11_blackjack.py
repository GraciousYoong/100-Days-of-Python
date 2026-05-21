import random
import blackjack_pics

def pull_card() -> int:
    return random.randint(1, 10)

def blackjack() -> None:
    print(blackjack_pics.logo)
    your_cards = []
    your_cards.append(pull_card())
    your_cards.append(pull_card())
    sum = 0
    card_pulled = 0
    should_continue = True
    computer_continue = True
    for card in your_cards:
        sum += card
    computer_cards = []
    computer_first_card = pull_card()
    computer_cards.append(computer_first_card)
    computer_sum = computer_first_card
    while should_continue == True:
        print(f"    Your cards: {your_cards}, current score: {sum}")
        print(f"    Computer first card: {computer_first_card}")
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
            card_pulled = pull_card()
            your_cards.append(card_pulled)
            sum += card_pulled
            if sum > 21:
                should_continue = False
                computer_continue = False
        else:
            should_continue = False

    while computer_continue == True:
        if computer_sum > 21:
            computer_continue = False
        else:
            card_pulled = pull_card()
            computer_cards.append(card_pulled)
            computer_sum += card_pulled
            if computer_sum > 12:
                if random.randint(0, 1) == 0:
                    computer_continue = False

    print(f"    Your final hand: {your_cards}, final score: {sum}")
    print(f"    Computer final hand: {computer_cards}, final score: {computer_sum}")
    if sum > 21:
        print("You went over. You lose")
    elif sum <= 21 and sum > computer_sum or computer_sum > 21:
        print("You win!")
    else:
        print("You lose!")
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        blackjack()

if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    blackjack()