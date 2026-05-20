import random
import hangman_words
import hangman_pics

def hangman() -> None:
    print(hangman_pics.logo)
    hangmanpics = hangman_pics.hangmanpics
    
    word = random.choice(hangman_words.word_list)
    correct_guessing = ["-"] * len(word)
    lives = 7

    while "".join(correct_guessing) != word:
        print("=======================================")
        if lives == 0:
            print(hangmanpics[6])
            print(f"The word is: {word}.")
            print("You lose!")
            return
        print("".join(correct_guessing))
        print(f"lives left: {lives}")
        if lives < 7:
            print(hangmanpics[6 - lives])
        user_input = input("Guess a letter: ").lower()
        if len(user_input) > 1:
            print("Please enter ONE letter only.")
        elif user_input in word:
            for index, char in enumerate(word):
                if user_input == char:
                    correct_guessing[index] = char
        else:
            lives -= 1
            print(f"'{user_input}' is not inside the word. You lose a live.")
        print("=======================================")
    print(f"The word is: {word}.")
    print("You win!")

hangman()