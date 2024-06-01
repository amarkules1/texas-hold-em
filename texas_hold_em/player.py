from texas_hold_em.hands import HandOfTwo, HandOfFive


class Player:

    hand_of_two = None
    hand_of_five = None
    chips = 0
    round_bet = 0
    in_round = True
    position = -1

    def __init__(self, position):
        self.position = position
        self.hand_of_two = HandOfTwo([])
        self.chips = 1000
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
        return self.round_bet


