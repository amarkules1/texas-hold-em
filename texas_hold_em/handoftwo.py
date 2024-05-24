from texas_hold_em.game_utils import *

HAND_FUNCTIONS = [
    find_royal_flush,
    find_straight_flush,
    find_four_of_a_kind,
    find_full_house,
    find_flush,
    find_straight,
    find_three_of_a_kind,
    find_two_pair,
    find_single_pair,
    find_high_card
]

class HandOfTwo:

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        if len(self.cards) < 2:
            self.cards.append(card)
        else:
            raise ValueError("Hand already has 2 cards")


class HandOfFive:

    def __init__(self):
        self.cards = []
        self.hand_rank = None

    def determine_best(self, hand_cards, community_cards):
        for i in range(len(HAND_FUNCTIONS)):
            hand = HAND_FUNCTIONS[i](hand_cards, community_cards)
            if hand is not None:
                self.cards = hand
                self.hand_rank = i
                return i

    def __gt__(self, other):
        if self.hand_rank > other.hand_rank:
            return True
        elif self.hand_rank < other.hand_rank:
            return False
        for i in range(5):
            if self.cards[i].rank > other.cards[i].rank:
                return True
            elif self.cards[i].rank < other.cards[i].rank:
                return False
        return False

