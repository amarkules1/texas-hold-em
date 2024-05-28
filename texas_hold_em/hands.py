from texas_hold_em.game_utils import *

"""
HAND_FUNCTIONS need to be operated on in the below order BUT ranks are the other way: Royal Flush = 7, and High Card = 0
"""
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

    hand_cards = []
    community_cards = []
    hand_rank = None
    hand = []

    def __init__(self, hand_cards, community_cards):
        self.hand_cards = []
        self.community_cards = []
        self.hand_rank = self.determine_best(hand_cards, community_cards)

    def determine_best(self, hand_cards, community_cards):
        for i in range(len(HAND_FUNCTIONS)):
            self.hand = HAND_FUNCTIONS[i](hand_cards, community_cards)
            if self.hand is not None:
                self.hand_rank = 7 - i
                return i

    def __gt__(self, other):
        if self.hand_rank > other.hand_rank:
            return True
        elif self.hand_rank < other.hand_rank:
            return False
        for i in range(5):
            if self.hand[i].rank > other.cards[i].rank:
                return True
            elif self.hand[i].rank < other.cards[i].rank:
                return False
        return False

    def __eq__(self, other):
        if self.hand_rank == other.hand_rank:
            for i in range(5):
                if self.hand[i].rank != other.cards[i].rank:
                    return False
                return True
        return False

    def __lt__(self, other):
        return not self.__gt__(other) and not self.__eq__(other)
