from texas_hold_em_utils.card import Card
from texas_hold_em_utils.relative_ranking import rank_hand


def test_rank_hand_best_possible_4_of_kind():
    hand = [Card().from_ints(0, 0), Card().from_ints(0, 1)]
    community_cards = [Card().from_ints(0, 2), Card().from_ints(0, 3), Card().from_ints(3, 3)]
    wins, losses, ties = rank_hand(hand, community_cards)
    assert losses == 0
    assert ties == 0
    assert wins == 2162 # just trusting the program here

def test_rank_hand_community_cards_best():
    hand = [Card().from_ints(0, 0), Card().from_ints(0, 1)]
    community_cards = [Card().from_ints(5, 2), Card().from_ints(5, 3), Card().from_ints(5, 1), Card().from_ints(7, 1), Card().from_ints(7, 0)]
    wins, losses, ties = rank_hand(hand, community_cards)
    assert losses == 318
    assert ties == 1662
    assert wins == 0
