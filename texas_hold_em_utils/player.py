from texas_hold_em_utils.hands import HandOfTwo


class Player:

    hand_of_two = None
    hand_of_five = None
    chips = 0
    round_bet = 0
    in_round = True
    position = -1

    def __init__(self, position, chips=1000):
        """
        Initializes a player with a position (0 to n-1) and chips
        :param position: int from 0 to n-1
        :param chips: int representing the number of chips the player starts with (default 1000)
        """
        self.position = position
        self.hand_of_two = HandOfTwo([])
        self.chips = chips
        self.round_bet = 0
        self.in_round = True

    def bet(self, amount):
        """
        Bets the given amount if the player has enough chips, otherwise bets all chips
        :param amount: amount the player wants to bet
        :return: the amount the player actually bets
        """
        if amount > self.chips:
            amount = self.chips
        self.chips -= amount
        self.round_bet += amount
        return amount

    def fold(self):
        """
        Folds the player's hand and marks them as out of the round
        :return: the player's round bet (0)
        """
        self.in_round = False
        return 0

    def decide(self, round_num, pot, all_day, big_blind, community_cards):
        """
        Abstract method for deciding what to do in a round
        :param round_num: 0 for pre-flop, 1 for flop, 2 for turn, 3 for river
        :param pot: the current pot
        :param all_day: the current highest bet (including all rounds)
        :param big_blind: the big blind for the game
        :param community_cards: the community cards (list of 0 to 5 cards)
        :return: a tuple of the action ("fold", "check", "call", "raise") and the amount to bet
        """
        pass


# Simple player calls big blind, then checks, folds to any bet past BB
class SimplePlayer(Player):
    def decide(self, round_num, pot, all_day, big_blind, community_cards):
        """
        Simple player calls big blind, then checks, folds to any bet past BB
        :param round_num: 0 for pre-flop, 1 for flop, 2 for turn, 3 for river
        :param pot: the current pot
        :param all_day: the current highest bet (including all rounds)
        :param big_blind: the big blind for the game
        :param community_cards: the community cards (list of 0 to 5 cards)
        :return: a tuple of the action ("fold", "check", "call", "raise") and the amount to bet
        """
        to_call = all_day - self.round_bet
        if round_num == 0 and all_day == big_blind and to_call > 0:
            return "call", self.bet(to_call)
        if to_call == 0:
            return "check", 0
        return "fold", self.fold()
