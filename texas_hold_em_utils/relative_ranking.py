from texas_hold_em_utils.hands import HandOfFive
from texas_hold_em_utils.deck import Deck


def rank_hand(hand, community_cards):
    """
    *Post Flop*
    Ranks a hand of two cards and 3-5 five community cards relative to all other possible hands, based only on known cards
    Known issue: odds assume no additional community cards. Works best for after the river, does an ok approx before then
    :param hand: a list of 2 cards (Card objects)
    :param community_cards: a list of 3-5 cards (Card objects)
    :return: a tuple of the number of wins, losses, and ties for the given hand
    """
    player_hand = HandOfFive(hand, community_cards)
    deck1 = Deck()
    deck2 = Deck()
    wins = 0
    losses = 0
    ties = 0
    for card1 in deck1.cards:
        if card1 not in hand + community_cards:
            for card2 in deck2.cards:
                if card2 not in hand + community_cards and card2 != card1:
                    other_hand = HandOfFive([card1, card2], community_cards)
                    if player_hand > other_hand:
                        wins += 1
                    elif player_hand < other_hand:
                        losses += 1
                    else:
                        ties += 1
    return wins, losses, ties


def get_hand_stats(hand, community_cards, player_count):
    """
    *Post Flop*
    Provides expected outcome information for a given hand based on the number of players
    Known issue: odds assume no additional community cards. Works best for after the river, does an ok approx before then
    :param hand: 2 cards
    :param community_cards: a list of 3-5 cards
    :param player_count: 2+
    :return: dict with keys: "two_player_effective_win_rate", "percentile", "win_rate"
    """
    wins, losses, ties = rank_hand(hand, community_cards)
    two_player_effective_win_rate = ((2 * wins) + ties) / (
                2 * (wins + losses + ties)) if wins + losses + ties > 0 else 0
    percentile = two_player_effective_win_rate * 100
    # win rate is the chance that the hand beats player_count other hands
    win_rate = two_player_effective_win_rate ** (player_count - 1)
    return {"two_player_effective_win_rate": two_player_effective_win_rate, "percentile": percentile,
            "win_rate": win_rate}
