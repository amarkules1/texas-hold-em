from texas_hold_em_utils.deck import Deck
from texas_hold_em_utils.hands import HandOfTwo, HandOfFive
from texas_hold_em_utils.player import Player


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
        """
        Initializes a game of Texas Hold 'Em with the given number of players, big blind, and starting chips
        :param num_players: the number of players in the game, by default these players are simple players
        :param big_blind: The big blind for the game
        :param starting_chips: The number of chips each player starts with
        """
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
        """
        Deals two cards to each player in the game
        :return:
        """
        # two loops to simulate real dealing
        for player in self.players:
            player.hand_of_two.add_card(self.deck.draw())
        for player in self.players:
            player.hand_of_two.add_card(self.deck.draw())

    def flop(self):
        """
        Deals the flop and adds it to the community cards
        :return: an array of the community cards, in this case just the 3 flopped cards
        """
        # burn
        self.deck.draw()
        # turn
        self.community_cards = [self.deck.draw() for _ in range(3)]
        self.round += 1
        return self.community_cards

    def turn(self):
        """
        Deals the turn and adds it to the community cards
        :return: a list of the community cards, in this case  the 3 flop cards plus the turn card
        """
        # burn
        self.deck.draw()
        # turn
        self.community_cards.append(self.deck.draw())
        self.round += 1
        return self.community_cards

    def river(self):
        """
        Deals the river and adds it to the community cards
        :return: a list of the community cards, in this case  the 3 flop cards plus the turn card and the river card
        """
        # burn
        self.deck.draw()
        # turn
        self.community_cards.append(self.deck.draw())
        self.round += 1
        return self.community_cards

    def get_bets(self):
        """
        Gets the bets from each player in the round, keeping track of the pot and the required bet to stay in the round
        :return:
        """
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
                        # TODO - all other players must call or fold until last raiser is reached
                        self.all_day = player.round_bet
                    self.pot += decision[1]
        else:
            for i in range(self.player_ct):
                player = self.players[(self.dealer_position + i) % self.player_ct]
                if player.in_round:
                    decision = player.decide(self.round, self.pot, self.all_day, self.big_blind, self.community_cards)
                    if decision[0] == "raise":
                        # TODO - all other players must call or fold until last raiser is reached
                        self.all_day = player.round_bet
                    self.pot += decision[1]

    def determine_round_winners(self):
        """
        Determines the winners of the round based on the best hand of five cards from each player
        :return: a list of players who have the best hand (usually just 1 player)
        """
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
