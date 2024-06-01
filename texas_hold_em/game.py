from texas_hold_em.deck import Deck
from texas_hold_em.hands import HandOfTwo, HandOfFive
from texas_hold_em.player import Player


class Game:
    deck = None
    hands = []
    community_cards = []
    players = []
    dealer_position = 0

    def __init__(self, num_players):
        self.deck = Deck()
        self.deck.shuffle()
        for i in range(num_players):
            player = Player(i)
            player.hand_of_two = HandOfTwo([])
            self.players.append(player)

    def deal(self):
        # two loops to simulate real dealing
        for player in self.players:
            player.hand_of_two.add_card(self.deck.draw())
        for player in self.players:
            player.hand_of_two.add_card(self.deck.draw())

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

    def determine_round_winners(self):
        winners = []
        for player in self.players:
            if player.in_round:
                player.hand_of_five = HandOfFive(player.hand_of_two.cards, self.community_cards)
                if len(winners) == 0:
                    winners.append(player)
                elif player.hand_of_five > winners[0].hand_of_five:
                    winners = [player]
                elif player.hand_of_five == winners[0].hand_of_five:
                    winners.append(player)
        return winners
