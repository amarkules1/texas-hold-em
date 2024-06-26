"""
HAND_FUNCTIONS need to be operated on in the below order BUT ranks are the other way: Royal Flush = 7, and High Card = 0
"""
from texas_hold_em_utils.game_utils import *

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

    def __init__(self, cards):
        self.cards = cards

    def add_card(self, card):
        """
        Adds a card to the hand if there are less than 2 cards
        :param card:
        :return:
        """
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
        """

        :param hand_cards: list of 2 cards
        :param community_cards: list of 5 cards
        """
        self.hand_cards = hand_cards
        self.community_cards = community_cards
        self.determine_best(hand_cards, community_cards)

    def determine_best(self, hand_cards, community_cards):
        """
        Determines the best hand from the hand and community cards
        :param hand_cards: list of 2 cards
        :param community_cards: list of 5 cards
        :return: the 5 cards that make up the best hand, ordered so that the hand is easily compared to other hands
        Ex: a straight flush would be ordered from highest to lowest card, a full house would be ordered with the three
        of a kind first, then the pair
        """
        for i in range(len(HAND_FUNCTIONS)):
            self.hand = HAND_FUNCTIONS[i](hand_cards, community_cards)
            if self.hand is not None:
                self.hand_rank = 9 - i
                break

    def __gt__(self, other):
        """
        Compares two hands to see if the first hand is better than the second
        :param other: the other hand to compare to
        :return: True if this hand is better than the other, False otherwise (including when they are equal)
        """
        if self.hand_rank > other.hand_rank:
            return True
        elif self.hand_rank < other.hand_rank:
            return False
        for i in range(5):
            if self.hand[i].rank > other.hand[i].rank:
                return True
            elif self.hand[i].rank < other.hand[i].rank:
                return False
        return False

    def __eq__(self, other):
        """
        Compares two hands to see if they are equal
        :param other: the other hand to compare to
        :return: True if the hands are equal, False otherwise
        """
        if self.hand_rank == other.hand_rank:
            for i in range(5):
                if self.hand[i].rank != other.hand[i].rank:
                    return False
            return True
        return False

    def __lt__(self, other):
        """
        Compares two hands to see if the first hand is worse than the second
        :param other: the other hand to compare to
        :return: True if this hand is worse than the other, False otherwise (including when they are equal)
        """
        return not self.__gt__(other) and not self.__eq__(other)
