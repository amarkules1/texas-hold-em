from src.texas_hold_em_utils.deck import Deck
from src.texas_hold_em_utils.hands import HandOfTwo, HandOfFive
from src.texas_hold_em_utils.player import Player


class Game:
    deck = None
    hands = []
    community_cards = []
    players = []
    dealer_position = 0
    big_blind = 0
    starting_chips = 0
    pot = 0
    all_day = 0
    round = 0
    player_ct = 0

    def __init__(self, num_players, big_blind=20, starting_chips=1000):
        self.player_ct = num_players
        self.big_blind = big_blind
        self.starting_chips = starting_chips
        self.deck = Deck()
        self.deck.shuffle()
        for i in range(num_players):
            player = Player(i, starting_chips)
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
        self.round += 1

    def turn(self):
        # burn
        self.deck.draw()
        # turn
        self.community_cards.append(self.deck.draw())
        self.round += 1

    def river(self):
        # burn
        self.deck.draw()
        # turn
        self.community_cards.append(self.deck.draw())
        self.round += 1

    def get_bets(self):
        if self.round == 0:
            self.all_day = self.big_blind
            # small blind
            self.pot += self.players[(self.dealer_position + 1) % self.player_ct].bet(self.big_blind // 2)
            # big blind
            self.pot += self.players[(self.dealer_position + 2) % self.player_ct].bet(self.big_blind)
            for i in range(3, self.player_ct + 3):
                player = self.players[(self.dealer_position + i) % self.player_ct]
                if player.in_round:
                    decision = player.decide(self.round, self.pot, self.all_day, self.big_blind, self.community_cards)
                    if decision[0] == "raise":
                        self.all_day = player.round_bet
                    self.pot += decision[1]
        else:
            for i in range(self.player_ct):
                player = self.players[(self.dealer_position + i) % self.player_ct]
                if player.in_round:
                    decision = player.decide(self.round, self.pot, self.all_day, self.big_blind, self.community_cards)
                    if decision[0] == "raise":
                        self.all_day = player.round_bet
                    self.pot += decision[1]

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
