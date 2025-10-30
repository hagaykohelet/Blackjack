from core.player_io import ask_player_action

def calculate_hand_value(hand: list[dict]) -> int:
    symbols = ["A","J","Q","K"]
    sum_of_hand = 0
    for card in hand:
        if card["rank"] not in symbols:
            sum_of_hand += int(card["rank"])
        elif card["rank"] in symbols[1:]:
            sum_of_hand += 10
        else:
            sum_of_hand += 1
    return sum_of_hand


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:

    card1_of_player = deck.pop(0)
    card2_of_player = deck.pop(0)
    card1_of_dealer = deck.pop(0)
    card2_of_dealer = deck.pop(0)
    player["hand"].append(card1_of_player)
    player["hand"].append(card2_of_player)
    dealer["hand"].append(card1_of_dealer)
    dealer["hand"].append(card2_of_dealer)
    sum_of_player_hand = calculate_hand_value(player["hand"])
    sum_of_dealer_hand = calculate_hand_value(dealer["hand"])
    print(f"the sum of player hand is {sum_of_player_hand}")
    print(f"the sum of dealer hand is {sum_of_dealer_hand}")



def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer["hand"]) <= 17:
        card = deck.pop(0)
        dealer["hand"].append(card)
    if calculate_hand_value(dealer["hand"]) > 21:
        print("over 21")
        return False
    elif 21 > calculate_hand_value(dealer["hand"]) > 17:
        return True
    return

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:

    deal_two_each(deck,player,dealer)

    while True:
        player_input = ask_player_action()
        if player_input == "H":
            card = deck.pop(0)
            player["hand"].append(card)
            calculate = calculate_hand_value(player["hand"])
            print(f"the sum of your hand is: {calculate}")
            if calculate > 21:
                return f"your sum of hand is {calculate} over 21"

        if player_input == "S":
            while True:
                dealer_turn = dealer_play(deck,dealer)
                if not dealer_turn:
                    return
                if dealer_turn:
                    player_calculate = calculate_hand_value(player["hand"])
                    dealer_calculate = calculate_hand_value(dealer["hand"])
                    closer = 21 - player_calculate
                    closer2 = 21 - dealer_calculate
                    if closer > closer2:
                        print(f"the winner is dealer with {dealer_calculate}")
                        # return
                    elif closer < closer2:
                        print(f"the winner is player with {player_calculate}")
                        # return
                    else:
                        print("Equality")

                    return