from texas_hold_em_utils.hands import HandOfFive
from texas_hold_em_utils.deck import Deck


def rank_hand(hand, community_cards):
    player_hand = HandOfFive(hand, community_cards)
    deck1 = Deck()
    deck2 = Deck()
    wins = 0
    losses = 0
    ties = 0
    for card1 in deck1.cards:
        if card1 not in hand + community_cards:
            for card2 in deck2.cards:
                if card2 not in hand + community_cards and card2 != card1:
                    other_hand = HandOfFive([card1, card2], community_cards)
                    if player_hand > other_hand:
                        wins += 1
                    elif player_hand < other_hand:
                        losses += 1
                    else:
                        ties += 1
    return wins, losses, ties
