import random

def pypassword_generator() -> None:
    print("Welcome to the PyPassword Generator!")
    letters_num = int(input("How many letters would you like in your password?\n"))
    symbols_num = int(input("How many symbols would you like?\n"))
    numbers_num = int(input("How many numbers would you like?\n"))
    letters_list = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G",
    "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z"
    ]
    symbols_list = [
    "!", "@", "#", "$", "%", "^", "&",
    "*", "(", ")", "-", "_", "=", "+",
    "[", "]", "{", "}", ";", ":", "'",
    '"', ",", ".", "<", ">", "/", "?",
    "\\", "|", "`", "~"
    ]
    numbers_list = [
    "0", "1", "2", "3", "4",
    "5", "6", "7", "8", "9"
    ]

    # password_list = []
    # for letter in range(0, letters_num):
    #     password_list.append(letters_list[random.randint(0, len(letters_list) - 1)])
    # for symbol in range(0, symbols_num):
    #     password_list.append(symbols_list[random.randint(0, len(symbols_list) - 1)])
    # for number in range(0, numbers_num):
    #     password_list.append(numbers_list[random.randint(0, len(numbers_list) - 1)])

    password_list = []
    for n in range(0, letters_num):
        password_list += random.choice(letters_list)
    for n in range(0, symbols_num):
        password_list += random.choice(symbols_list)
    for n in range(0, numbers_num):
        password_list += random.choice(numbers_list) 
    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    print(f"Your password is: {password}")

pypassword_generator()