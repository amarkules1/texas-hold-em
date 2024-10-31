from texas_hold_em_utils.hands import HandOfTwo
from texas_hold_em_utils.preflop_stats_repository import PreflopStatsRepository
from texas_hold_em_utils.relative_ranking import get_hand_rank_details


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

    def decide(self, round_num, pot, all_day, big_blind, community_cards, player_ct):
        """
        Abstract method for deciding what to do in a round
        :param round_num: 0 for pre-flop, 1 for flop, 2 for turn, 3 for river
        :param pot: the current pot
        :param all_day: the current highest bet (including all rounds)
        :param big_blind: the big blind for the game
        :param community_cards: the community cards (list of 0 to 5 cards)
        :param player_ct: number of players in the game
        :return: a tuple of the action ("fold", "check", "call", "raise") and the amount to bet
        """
        pass


# Simple player calls big blind, then checks, folds to any bet past BB
class SimplePlayer(Player):
    def decide(self, round_num, pot, all_day, big_blind, community_cards, player_ct):
        """
        Simple player calls big blind, then checks, folds to any bet past BB
        :param round_num: 0 for pre-flop, 1 for flop, 2 for turn, 3 for river
        :param pot: the current pot
        :param all_day: the current highest bet (including all rounds)
        :param big_blind: the big blind for the game
        :param community_cards: the community cards (list of 0 to 5 cards)
        :param player_ct: number of players in the game
        :return: a tuple of the action ("fold", "check", "call", "raise") and the amount to bet
        """
        to_call = all_day - self.round_bet
        if round_num == 0 and all_day == big_blind and to_call > 0:
            return "call", self.bet(to_call)
        if to_call == 0:
            return "check", 0
        return "fold", self.fold()


class AllInPreFlopPlayer(Player):
    threshold = 0.5
    preflop_stats_repo = None
    in_check_fold = False

    def __init__(self, position, chips=1000, threshold=0.5):
        super().__init__(position, chips)
        self.threshold = threshold
        self.preflop_stats_repo = PreflopStatsRepository()

    def decide(self, round_num, pot, all_day, big_blind, community_cards, player_ct):
        """
        Goes all in preflop if win rate is above threshold, otherwise check/folds
        :param round_num: 0 for pre-flop, 1 for flop, 2 for turn, 3 for river
        :param pot: the current pot
        :param all_day: the current highest bet (including all rounds)
        :param big_blind: the big blind for the game
        :param community_cards: the community cards (list of 0 to 5 cards)
        :param player_ct: number of players in the game
        :return: a tuple of the action ("fold", "check", "call", "raise") and the amount to bet
        """
        to_call = all_day - self.round_bet
        # if player is BB and
        if self.in_check_fold and to_call > 0 and round_num > 0:
            return "fold", self.fold()
        if round_num == 0:
            self.in_check_fold = False
            win_rate = self.preflop_stats_repo.get_win_rate(
                self.hand_of_two.cards[0].rank,
                self.hand_of_two.cards[1].rank,
                self.hand_of_two.cards[0].suit == self.hand_of_two.cards[1].suit,
                player_ct)
            if win_rate['win_rate'] > self.threshold:
                return "raise", self.bet(self.chips)
            else:
                if to_call == 0:
                    self.in_check_fold = True
                    return "check", 0
                return "fold", self.fold()
        # if player is BB and made it past the flop we need to check/fold
        if self.in_check_fold and to_call > 0 and round_num > 0:
            return "fold", self.fold()
        return "check", 0


class LimpPlayer(Player):
    threshold = 0.5
    preflop_stats_repo = None
    is_variable_threshold = False

    def __init__(self, position, chips=1000, threshold=0.5):
        super().__init__(position, chips)
        self.threshold = threshold
        self.preflop_stats_repo = PreflopStatsRepository()
        if type(threshold) is list:
            self.is_variable_threshold = True

    def decide(self, round_num, pot, all_day, big_blind, community_cards, player_ct):
        """
        Calls if win rate is above threshold, otherwise check/folds
        :param round_num: 0 for pre-flop, 1 for flop, 2 for turn, 3 for river
        :param pot: the current pot
        :param all_day: the current highest bet (including all rounds)
        :param big_blind: the big blind for the game
        :param community_cards: the community cards (list of 0 to 5 cards)
        :param player_ct: number of players in the game
        :return: a tuple of the action ("fold", "check", "call", "raise") and the amount to bet
        """
        to_call = all_day - self.round_bet
        if to_call == 0 or self.chips == 0:
            return "check", 0

        rd_threshold = self.threshold if not self.is_variable_threshold else self.threshold[round_num]

        if round_num == 0:
            win_rate = self.preflop_stats_repo.get_win_rate(
                self.hand_of_two.cards[0].rank,
                self.hand_of_two.cards[1].rank,
                self.hand_of_two.cards[0].suit == self.hand_of_two.cards[1].suit,
                player_ct)
            if win_rate['win_rate'] > rd_threshold:
                return "call", self.bet(to_call)
        else:
            stats = get_hand_rank_details(self.hand_of_two.cards, community_cards, player_ct)
            rate = stats['expected_win_rate']
            if rate > rd_threshold:
                return "call", self.bet(to_call)

        return "fold", self.fold()


class KellyMaxProportionPlayer(Player):
    round_proportions = None

    def __init__(self, position, chips=1000, round_proportions=None):
        super().__init__(position, chips)
        if round_proportions is None:
            self.round_proportions = [1, 1, 1, 1]
        else:
            self.round_proportions = round_proportions
        if len(self.round_proportions) != 4:
            raise ValueError("round_proportions must be a list of length 4")

    def decide(self, round_num, pot, all_day, big_blind, community_cards, player_ct):
        """
        decides whether to check/fold/call/raise based on the kelly criterion and round proportion
        bet size is rounded to the nearest multiple of the big blind
        :param round_num: 0 for pre-flop, 1 for flop, 2 for turn, 3 for river
        :param pot: the current pot
        :param all_day: the current highest bet (including all rounds)
        :param big_blind: the big blind for the game
        :param community_cards: the community cards (list of 0 to 5 cards)
        :param player_ct: number of players in the game
        :return: a tuple of the action ("fold", "check", "call", "raise") and the amount to bet
        """
        stats = get_hand_rank_details(self.hand_of_two.cards, community_cards, player_ct)
        desired_bet = self.chips * self.round_proportions[round_num] * stats['ideal_kelly_max']
        to_call = all_day - self.round_bet
        desired_bet_nearest_multiple = round(desired_bet / big_blind) * big_blind
        if desired_bet_nearest_multiple < all_day:
            if to_call > 0:
                return "fold", self.fold()
            else:
                return "check", 0
        elif desired_bet_nearest_multiple > all_day:
            return "raise", self.bet(desired_bet_nearest_multiple - all_day)
        else:
            if to_call == 0:
                return "check", 0
            return "call", self.bet(to_call)
