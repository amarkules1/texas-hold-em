class Hand:

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        if len(self.cards) < 2:
            self.cards.append(card)
        else:
            raise ValueError("Hand already has 2 cards")
