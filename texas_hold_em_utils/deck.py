from texas_hold_em_utils.card import Card

import random


class Deck:
    def __init__(self):
        """
        Initializes a deck of 52 cards (does not shuffle)
        """
        self.cards = []
        for suit in [0, 1, 2, 3]:
            for value in range(0, 13):
                self.cards.append(Card().from_ints(value, suit))

    def shuffle(self):
        """
        Shuffles the deck randomly
        :return:
        """
        random.shuffle(self.cards)

    def draw(self):
        """
        Removes a card from the deck and returns it
        :return: the card drawn
        """
        return self.cards.pop()

    def remove(self, card):
        """
        Removes a specific card from the deck
        :param card: the card to be removed
        :return:
        """
        self.cards.remove(card)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return str([str(card) for card in self.cards])
