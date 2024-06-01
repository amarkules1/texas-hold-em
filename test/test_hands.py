from texas_hold_em.card import Card
from texas_hold_em.hands import HandOfTwo, HandOfFive


def test_compare_hands_same_rank():
    community_cards = [
        Card().from_str("A", "Hearts"),
        Card().from_str("A", "Spades"),
        Card().from_str("4", "Clubs"),
        Card().from_str("6", "Diamonds"),
        Card().from_str("9", "Hearts")
    ]
    # 2 pair
    hand1 = HandOfFive([
        Card().from_str("K", "Hearts"),
        Card().from_str("K", "Spades")
    ], community_cards)
    # 2 pair
    hand2 = HandOfFive([
        Card().from_str("Q", "Hearts"),
        Card().from_str("Q", "Spades")
    ], community_cards)

    assert hand1 > hand2


def test_compare_hands_diff_rank():
    community_cards = [
        Card().from_str("A", "Hearts"),
        Card().from_str("A", "Spades"),
        Card().from_str("4", "Clubs"),
        Card().from_str("6", "Diamonds"),
        Card().from_str("9", "Hearts")
    ]
    # 2 pair
    hand1 = HandOfFive([
        Card().from_str("K", "Hearts"),
        Card().from_str("K", "Spades")
    ], community_cards)
    # full house
    hand2 = HandOfFive([
        Card().from_str("A", "Clubs"),
        Card().from_str("9", "Clubs")
    ], community_cards)

    assert hand1 < hand2
