def treasure_island_game() -> None:
    print("""
 ________                                                                    
/        |                                                                   
$$$$$$$$/______    ______    ______    _______  __    __   ______    ______  
   $$ | /      \  /      \  /      \  /       |/  |  /  | /      \  /      \ 
   $$ |/$$$$$$  |/$$$$$$  | $$$$$$  |/$$$$$$$/ $$ |  $$ |/$$$$$$  |/$$$$$$  |
   $$ |$$ |  $$/ $$    $$ | /    $$ |$$      \ $$ |  $$ |$$ |  $$/ $$    $$ |
   $$ |$$ |      $$$$$$$$/ /$$$$$$$ | $$$$$$  |$$ \__$$ |$$ |      $$$$$$$$/ 
   $$ |$$ |      $$       |$$    $$ |/     $$/ $$    $$/ $$ |      $$       |
   $$/ $$/        $$$$$$$/  $$$$$$$/ $$$$$$$/   $$$$$$/  $$/        $$$$$$$/                                                                                                                                                                                               
 ______            __                            __                          
/      |          /  |                          /  |                         
$$$$$$/   _______ $$ |  ______   _______    ____$$ |                         
  $$ |   /       |$$ | /      \ /       \  /    $$ |                         
  $$ |  /$$$$$$$/ $$ | $$$$$$  |$$$$$$$  |/$$$$$$$ |                         
  $$ |  $$      \ $$ | /    $$ |$$ |  $$ |$$ |  $$ |                         
 _$$ |_  $$$$$$  |$$ |/$$$$$$$ |$$ |  $$ |$$ \__$$ |                         
/ $$   |/     $$/ $$ |$$    $$ |$$ |  $$ |$$    $$ |                         
$$$$$$/ $$$$$$$/  $$/  $$$$$$$/ $$/   $$/  $$$$$$$/                                                  
          """)
    print("""
Welcome to Treasure Island.
Your mission is to find the treasure.
    """)
    print("You're at a cross road. Where do you want to go?")
    first_answer = str(input('	Type "left" or "right"\n').lower())
    if first_answer == "left":
        print("You came to a lake. There is an island in the middle of the lake.")
        second_answer = str(input('	Type "wait" to wait for a boat or "swim" to swim across.\n').lower())
        if second_answer == "wait":
            print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
            third_answer = str(input('	Which colour do you choose?\n').lower())
            if third_answer == "red":
                print("It's a room full of fire. Game Over.")
            elif third_answer == "yellow":
                print("You found the treasure! You Win!")
            elif third_answer == "blue":
                print("You enter a room of beasts. Game Over.")
            else:
                print("You choose a door that doesn't exist. Game Over.")
        elif second_answer == "swim":
            print("You get attacked by an angry trout. Game Over.")
    elif first_answer == "right":
        print("You fell into a hole. Game over.")

treasure_island_game()
