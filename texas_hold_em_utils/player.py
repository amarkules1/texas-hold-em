from texas_hold_em_utils.hands import HandOfTwo


class Player:

    hand_of_two = None
    hand_of_five = None
    chips = 0
    round_bet = 0
    in_round = True
    position = -1

    def __init__(self, position, chips=1000):
        self.position = position
        self.hand_of_two = HandOfTwo([])
        self.chips = chips
        self.round_bet = 0
        self.in_round = True

    def bet(self, amount):
        if amount > self.chips:
            amount = self.chips
        self.chips -= amount
        self.round_bet += amount
        return amount

    def fold(self):
        self.in_round = False
        return 0

    def decide(self, round_num, pot, all_day, big_blind, community_cards):
        pass


# Simple player calls big blind, then checks, folds to any bet past BB
class SimplePlayer(Player):
    def decide(self, round_num, pot, all_day, big_blind, community_cards):
        to_call = all_day - self.round_bet
        if round_num == 0 and all_day == big_blind and to_call > 0:
            return "call", self.bet(to_call)
        if to_call == 0:
            return "check", 0
        return "fold", self.fold()
