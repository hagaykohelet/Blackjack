import random

def build_standard() -> list[dict]:
    deck_cards = []
    suites = ["H","C","D","S"]
    ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    card = {}
    for rank in ranks:
        card = {}
        for suite in suites:
            card = {}
            card["rank"] = rank
            card["suite"] = suite
            deck_cards.append(card)


    return deck_cards


def converion_symbols(card):
    symbols = ["J","Q","K"]
    if card["rank"] in symbols:
        return 10
    elif card["rank"] == "A":
        return 1
    return




def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for swap in range(swaps):
        index1 = random.randint(0,len(deck)-1)
        index2 = random.randint(0,len(deck)-1)
        if index1 == index2:
            continue
        elif converion_symbols(deck[index2]) not in [10,1]:
            if deck[index2]["suite"] == "H" and  int(deck[index2]["rank"]) % 5 != 0:
                continue

            elif deck[index2]["suite"] == "C" and  int(deck[index2]["rank"]) % 3 != 0:
                continue

            elif deck[index2]["suite"] == "D" and  int(deck[index2]["rank"]) % 2 != 0:
                continue

            elif deck[index2]["suite"] == "S" and int(deck[index2]["rank"]) % 7 != 0:
                continue

        elif converion_symbols(deck[index2]) == 10:
            if deck[index2]["suite"] != "H" or deck[index2]["suite"] != "D":
                continue
        else:
            deck[index1],deck[index2] = deck[index2],deck[index1]
    return deck


