from texas_hold_em_utils.card import Card
from texas_hold_em_utils.outs_counter import get_one_card_outs, get_two_card_outs, OutsMetrics


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

def test_outsmetrics_to_json_one_card_outs():
    hand1 = [Card().from_str("A", "Hearts"), Card().from_str("A", "Clubs")]
    hand2 = [Card().from_str("2", "Spades"), Card().from_str("7", "Spades")]
    community_cards = [Card().from_str("7", "Clubs"), Card().from_str("6", "Spades"),
                       Card().from_str("9", "Hearts"), Card().from_str("9", "Spades")]
    metrics = OutsMetrics([hand1, hand2], community_cards)
    data = metrics.to_json()
    # Should be a list of lists of card strings
    assert isinstance(data["outs"], list)
    assert all(isinstance(l, list) for l in data["outs"])
    for out_list in data["outs"]:
        for card_str in out_list:
            assert isinstance(card_str, str)
            assert " of " in card_str or card_str == ""  # Empty string possible if no outs

def test_outsmetrics_to_json_two_card_outs():
    hand1 = [Card().from_str("A", "Hearts"), Card().from_str("A", "Clubs")]
    hand2 = [Card().from_str("2", "Spades"), Card().from_str("7", "Spades")]
    community_cards = [Card().from_str("7", "Clubs"), Card().from_str("6", "Spades"),
                       Card().from_str("9", "Hearts")]
    metrics = OutsMetrics([hand1, hand2], community_cards)
    data = metrics.to_json()
    # Should be a list of lists of comma-joined card strings
    assert isinstance(data["outs"], list)
    assert all(isinstance(l, list) for l in data["outs"])
    for out_list in data["outs"]:
        for card_str in out_list:
            assert isinstance(card_str, str)
            if card_str:
                # Should be two cards joined by a comma
                cards = card_str.split(",")
                assert len(cards) == 2
                assert all(" of " in c for c in cards)
