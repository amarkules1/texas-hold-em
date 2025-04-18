from texas_hold_em_utils.card import Card
from texas_hold_em_utils.outs_counter import get_one_card_outs, get_two_card_outs


def test_get_one_card_outs():
    hand1 = [Card().from_str("A", "Hearts"), Card().from_str("A", "Clubs")]
    hand2 = [Card().from_str("2", "Spades"), Card().from_str("7", "Spades")]
    community_cards = [Card().from_str("7", "Clubs"), Card().from_str("6", "Spades"),
                       Card().from_str("9", "Hearts"), Card().from_str("9", "Spades")]

    one_card_outs = get_one_card_outs([hand1, hand2], community_cards)
    assert len(one_card_outs)


def test_get_two_card_outs():
    hand1 = [Card().from_str("A", "Hearts"), Card().from_str("A", "Clubs")]
    hand2 = [Card().from_str("2", "Spades"), Card().from_str("7", "Spades")]
    community_cards = [Card().from_str("7", "Clubs"), Card().from_str("6", "Spades"),
                       Card().from_str("9", "Hearts")]

    two_card_outs = get_two_card_outs([hand1, hand2], community_cards)
    assert isinstance(two_card_outs, list)
    assert len(two_card_outs) == 2
    # Each entry should be a list of (card1, card2) tuples
    for outs in two_card_outs:
        for pair in outs:
            assert isinstance(pair, tuple)
            assert len(pair) == 2
            # Each element should be a Card
            assert all(hasattr(card, 'rank') and hasattr(card, 'suit') for card in pair)
