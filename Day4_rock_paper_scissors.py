import random

def rock_paper_scissors() -> None:
    answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if answer == 0:
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
              ''')
    elif answer == 1:
        print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
              ''')
    elif answer == 2:
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
              ''')
    else:
        print("You typed an invalid number, you lose!")
        return
    computer_answer = random.randint(0, 2)
    print("Computer chose: ")
    if computer_answer == 0:
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
              ''')
    elif computer_answer == 1:
        print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
              ''')
    elif computer_answer == 2:
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
              ''')
    if answer == computer_answer:
        print("It's a draw.")
    elif answer == 0:
        if computer_answer == 2:
            print("You win!")
        else:
            print("You lose!")
    elif answer == 1:
        if computer_answer == 0:
            print("You win!")
        else:
            print("You lose!")
    elif answer == 2:
        if computer_answer == 1:
            print("You win!")
        else:
            print("You lose!")

rock_paper_scissors()