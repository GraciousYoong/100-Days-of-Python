import caesar_cipher_pics

print(caesar_cipher_pics.logo)

def caesar_cipher() -> None:
    letter_list = "abcdefghijklmnopqrstuvwxyz"
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != "encode" and direction != "decode":
        print("Invalid input.")
    else:
        message = input("Type your message:\n").lower()
        shift_num = int(input("Type the shift number:\n"))
        result = ""
        for char in message:
            if char in letter_list:
                index = letter_list.index(char)

                if direction == "encode":
                    new_index = (index + shift_num) % 26
                    result += letter_list[new_index]            
                else:
                    new_index = (index - shift_num) % 26
                    result += letter_list[new_index]
            else:
                result += char
        if direction == "encode":
            print(f"Here is the encoded result: {result}")
        else:
            print(f"Here is the decoded result: {result}")
        go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if go_again == "yes":
            caesar_cipher()
        else:
            print("Goodbye")
caesar_cipher()
