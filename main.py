from core.deck import build_standard,shuffle_by_suit,converion_symbols
from core.game_logic import calculate_hand_value,deal_two_each,dealer_play,run_full_game
from core.player_io import ask_player_action
if __name__ == "__main__":
    deck = build_standard()
    shuffle_deck = shuffle_by_suit(deck)
    player = {"hand": []}
    dealer = {"hand": []}
    print(run_full_game(shuffle_deck,player,dealer))

