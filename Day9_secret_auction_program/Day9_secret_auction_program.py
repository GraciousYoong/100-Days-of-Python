import secret_auction_pics
import os

print(secret_auction_pics.logo)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def secret_auction_program() -> None:
    auction_dict = {}
    highest_auction = 0
    winner = ""
    auction_continue = True
    while auction_continue:
        user_name = input("What is your name? ")
        user_bid = int(input("What is your bid? $"))
        auction_dict[user_name] = user_bid
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if other_bidders != "yes":
            auction_continue = False
        else:
             clear_screen()
    for key in auction_dict:
                if auction_dict[key] > highest_auction:
                    highest_auction = auction_dict[key]
                    winner = key
    print(f"The winner is {winner} with a bid of ${highest_auction}")
    
secret_auction_program()