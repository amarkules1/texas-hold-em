from texas_hold_em_utils.deck import Deck
from texas_hold_em_utils.hands import HandOfFive


def get_one_card_outs(hands, community_cards=None):
    outs = [[] for i in range(len(hands))]
    if community_cards is None or len(community_cards) < 4:
        return outs
    deck = Deck()
    for hand in hands:
        for card in hand:
            deck.remove(card)

    for card in community_cards:
        deck.remove(card)

    for card in deck.cards:
        final_hands = []
        winner = None
        winner_index = 0
        is_split = False
        for i in range(len(hands)):
            hand = HandOfFive(hands[i], community_cards + [card])
            final_hands.append(hand)
            if winner is None or hand > winner:
                winner = hand
                winner_index = i
                is_split = False
            elif hand == winner and i != winner_index:
                is_split = True

        if not is_split:
            outs[winner_index].append(card)

    return outs

def get_two_card_outs(hands, community_cards=None):
    """
    Returns, for each player, the list of (card1, card2) pairs such that if both are drawn as the next two community cards, that player wins outright (not a split).
    """
    from itertools import combinations
    outs = [[] for _ in range(len(hands))]
    if community_cards is None or len(community_cards) < 3:
        # Need at least 3 community cards to add two more
        return outs
    deck = Deck()
    for hand in hands:
        for card in hand:
            deck.remove(card)
    for card in community_cards:
        deck.remove(card)

    # For each pair of remaining cards, simulate adding both to the board
    for card1, card2 in combinations(deck.cards, 2):
        final_hands = []
        winner = None
        winner_index = 0
        is_split = False
        for i in range(len(hands)):
            hand = HandOfFive(hands[i], community_cards + [card1, card2])
            final_hands.append(hand)
            if winner is None or hand > winner:
                winner = hand
                winner_index = i
                is_split = False
            elif hand == winner and i != winner_index:
                is_split = True
        if not is_split:
            outs[winner_index].append((card1, card2))
    return outs

class OutsMetrics:
    hands = []
    community_cards = None
    outs = []
    remaining_card_combinations = 0
    win_percentages = []

    def __init__(self, hands, community_cards):
        self.hands = hands
        self.community_cards = community_cards
        remaining_deck = Deck()
        for hand in self.hands:
            for card in hand:
                remaining_deck.remove(card)
        for card in self.community_cards:
            remaining_deck.remove(card)
        if len(community_cards) == 4:
            self.remaining_card_combinations = len(remaining_deck.cards)
            self.outs = get_one_card_outs(self.hands, self.community_cards)
            self.win_percentages = [len(out) / self.remaining_card_combinations for out in self.outs]
        elif len(community_cards) == 3:
            self.remaining_card_combinations = len(remaining_deck.cards) * (len(remaining_deck.cards) - 1)
        else:
            raise ValueError(f"Invalid number of community cards {len(community_cards)}")
