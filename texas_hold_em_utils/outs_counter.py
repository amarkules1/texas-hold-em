from texas_hold_em_utils import card
from texas_hold_em_utils.deck import Deck
from texas_hold_em_utils.hands import HandOfFive


def get_one_card_outs(hands, community_cards=None):
    """
    Calculate the one-card outs for each player given their hands and the current community cards.

    An "out" is a card that, if drawn as the next community card, allows a player to win outright (not a split).
    Only valid if there are at least 4 community cards.

    Args:
        hands (List[List[Card]]): List of player hands, each a list of Card objects.
        community_cards (List[Card]): List of community Card objects. Must have at least 4 cards.

    Returns:
        List[List[Card]]: For each player, a list of Card objects that are their outs.
    """
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
    Calculate the two-card outs for each player given their hands and the current community cards.

    An "out" is a tuple of two cards such that, if both are drawn as the next two community cards, the player wins outright (not a split).
    Only valid if there are at least 3 community cards.

    Args:
        hands (List[List[Card]]): List of player hands, each a list of Card objects.
        community_cards (List[Card]): List of community Card objects. Must have at least 3 cards.

    Returns:
        List[List[Tuple[Card, Card]]]: For each player, a list of (Card, Card) tuples that are their outs.
    """
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
    """
    Stores and computes metrics related to poker outs, given players' hands and community cards.

    Depending on the number of community cards, calculates one-card or two-card outs, remaining combinations, and win percentages.
    """
    def __init__(self, hands, community_cards):
        """
        Initialize OutsMetrics, computing outs and win percentages for the given hands and community cards.

        Args:
            hands (List[List[Card]]): List of player hands, each a list of Card objects.
            community_cards (List[Card]): List of community Card objects (length must be 3 or 4).

        Raises:
            ValueError: If the number of community cards is not 3 or 4.
        """
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
            self.remaining_card_combinations = len(remaining_deck.cards) * (len(remaining_deck.cards) - 1) / 2 # divide by 2 because order doesn't matter
            self.outs = get_two_card_outs(self.hands, self.community_cards)
            self.win_percentages = [len(out) / self.remaining_card_combinations for out in self.outs]
        else:
            raise ValueError(f"Invalid number of community cards {len(community_cards)}")

    def to_json(self):
        """
        Serialize the OutsMetrics object to a JSON-serializable dictionary.

        The 'outs' field will always be a list of lists of strings:
        - For one-card outs: each string is a single card (e.g., 'A of Hearts').
        - For two-card outs: each string is two cards joined by a comma (e.g., 'A of Hearts,K of Spades').

        Returns:
            dict: Dictionary representation of the OutsMetrics suitable for JSON serialization.
        """
        return {
            "hands": [[str(card) for card in hand] for hand in self.hands],
            "community_cards": [str(card) for card in self.community_cards],
            "outs": [
                [
                    str(card) if not isinstance(card, tuple)
                    else ",".join(str(c) for c in card)
                    for card in out_list
                ]
                for out_list in self.outs
            ],
            "win_percentages": self.win_percentages
        }