from texas_hold_em.deck import Deck
from texas_hold_em.handoftwo import HandOfTwo


class Game:
    deck = None
    hands = []
    community_cards = []

    def __init__(self, num_players):
        self.deck = Deck()
        self.deck.shuffle()
        self.hands = [HandOfTwo() for _ in range(num_players)]

    def deal(self):
        # two loops to simulate real dealing
        for hand in self.hands:
            hand.add_card(self.deck.draw())
        for hand in self.hands:
            hand.add_card(self.deck.draw())

    def flop(self):
        # burn
        self.deck.draw()
        # turn
        self.community_cards = [self.deck.draw() for _ in range(3)]

    def turn(self):
        # burn
        self.deck.draw()
        # turn
        self.community_cards.append(self.deck.draw())

    def river(self):
        # burn
        self.deck.draw()
        # turn
        self.community_cards.append(self.deck.draw())

    def determine_winner(self, remaining_players):
        best_hand = None
        for i in remaining_players:
            hand = self.hands[i]
            if best_hand is None:
                best_hand = hand
            else:
                if hand > best_hand:
                    best_hand = hand
        pass


