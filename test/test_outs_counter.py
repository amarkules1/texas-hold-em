from texas_hold_em_utils.card import Card
from texas_hold_em_utils.outs_counter import get_one_card_outs


def test_get_one_card_outs():
    hand1 = [Card().from_str("A", "Hearts"), Card().from_str("A", "Clubs")]
    hand2 = [Card().from_str("2", "Spades"), Card().from_str("7", "Spades")]
    community_cards = [Card().from_str("7", "Clubs"), Card().from_str("6", "Spades"),
                       Card().from_str("9", "Hearts"), Card().from_str("9", "Spades")]

    one_card_outs = get_one_card_outs([hand1, hand2], community_cards)
    assert len(one_card_outs)
