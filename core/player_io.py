def ask_player_action() -> str:
    while True:
        choose = input("Enter 'H' for issuing a car or 'S' for dealer play: ")
        if choose == "S" or choose == "H":


            return choose
        else:
            print("its not correct input")


