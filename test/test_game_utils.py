from src.texas_hold_em_utils.card import Card
from src.texas_hold_em_utils.game_utils import get_card_counts, find_royal_flush, find_straight_flush, find_four_of_a_kind, \
    find_full_house, find_flush, find_straight, find_three_of_a_kind, find_two_pair, find_single_pair, find_high_card


def test_get_card_counts_all_diff():
    hand = [Card().from_str("2", "Hearts"), Card().from_str("A", "Spades")]
    community_cards = [Card().from_str("J", "Clubs"), Card().from_str("5", "Diamonds"), Card().from_str("10", "Hearts"),
                       Card().from_str("7", "Spades"), Card().from_str("8", "Clubs")]

    assert get_card_counts(hand, community_cards) == [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1]


def test_get_card_counts_2_pair():
    hand = [Card().from_str("2", "Hearts"), Card().from_str("J", "Spades")]
    community_cards = [Card().from_str("J", "Clubs"), Card().from_str("5", "Diamonds"), Card().from_str("10", "Hearts"),
                       Card().from_str("7", "Spades"), Card().from_str("2", "Clubs")]

    assert get_card_counts(hand, community_cards) == [2, 0, 0, 1, 0, 1, 0, 0, 1, 2, 0, 0, 0]


def test_get_card_counts_3_of_a_kind():
    hand = [Card().from_str("2", "Hearts"), Card().from_str("J", "Spades")]
    community_cards = [Card().from_str("J", "Clubs"), Card().from_str("5", "Diamonds"), Card().from_str("10", "Hearts"),
                       Card().from_str("J", "Spades"), Card().from_str("2", "Clubs")]

    assert get_card_counts(hand, community_cards) == [2, 0, 0, 1, 0, 0, 0, 0, 1, 3, 0, 0, 0]


def test_find_royal_flush_true():
    hand = [Card().from_str("10", "Hearts"),
            Card().from_str("J", "Hearts")]
    community_cards = [Card().from_str("Q", "Hearts"),
                       Card().from_str("K", "Hearts"),
                       Card().from_str("A", "Hearts"),
                       Card().from_str("9", "Hearts"),
                       Card().from_str("3", "Spades")]

    assert find_royal_flush(hand, community_cards) == [Card().from_str("A", "Hearts"),
                                                       Card().from_str("K", "Hearts"),
                                                       Card().from_str("Q", "Hearts"),
                                                       Card().from_str("J", "Hearts"),
                                                       Card().from_str("10", "Hearts")]


def test_find_royal_flush_mismatched_suite():
    hand = [Card().from_str("10", "Hearts"),
            Card().from_str("J", "Hearts")]
    community_cards = [Card().from_str("Q", "Hearts"),
                       Card().from_str("K", "Spades"),
                       Card().from_str("A", "Hearts"),
                       Card().from_str("9", "Hearts"),
                       Card().from_str("3", "Spades")]

    assert not find_royal_flush(hand, community_cards)


def test_find_royal_flush_missing_facecard():
    hand = [Card().from_str("4", "Hearts"),
            Card().from_str("J", "Hearts")]
    community_cards = [Card().from_str("Q", "Hearts"),
                       Card().from_str("K", "Hearts"),
                       Card().from_str("A", "Hearts"),
                       Card().from_str("9", "Hearts"),
                       Card().from_str("3", "Spades")]

    assert not find_royal_flush(hand, community_cards)


def test_find_straight_flush():
    hand = [Card().from_str("4", "Hearts"),
            Card().from_str("5", "Hearts")]
    community_cards = [Card().from_str("6", "Hearts"),
                       Card().from_str("K", "Spades"),
                       Card().from_str("A", "Hearts"),
                       Card().from_str("2", "Hearts"),
                       Card().from_str("3", "Hearts")]

    assert find_straight_flush(hand, community_cards) == [Card().from_str("6", "Hearts"),
                                                          Card().from_str("5", "Hearts"),
                                                          Card().from_str("4", "Hearts"),
                                                          Card().from_str("3", "Hearts"),
                                                          Card().from_str("2", "Hearts")]


def test_find_straight_flush_missing_card():
    hand = [Card().from_str("4", "Hearts"),
            Card().from_str("9", "Hearts")]
    community_cards = [Card().from_str("6", "Hearts"),
                       Card().from_str("K", "Spades"),
                       Card().from_str("A", "Hearts"),
                       Card().from_str("2", "Hearts"),
                       Card().from_str("3", "Hearts")]

    assert not find_straight_flush(hand, community_cards)


def test_find_straight_flush_wrong_suite():
    hand = [Card().from_str("4", "Diamonds"),
            Card().from_str("5", "Hearts")]
    community_cards = [Card().from_str("6", "Hearts"),
                       Card().from_str("K", "Spades"),
                       Card().from_str("A", "Hearts"),
                       Card().from_str("2", "Hearts"),
                       Card().from_str("3", "Hearts")]

    assert not find_straight_flush(hand, community_cards)


def test_find_four_of_a_kind():
    hand = [Card().from_str("4", "Hearts"),
            Card().from_str("4", "Spades")]
    community_cards = [Card().from_str("4", "Clubs"),
                       Card().from_str("4", "Diamonds"),
                       Card().from_str("3", "Hearts"),
                       Card().from_str("2", "Hearts"),
                       Card().from_str("3", "Spades")]

    assert find_four_of_a_kind(hand, community_cards) == [Card().from_str("4", "Hearts"),
                                                          Card().from_str("4", "Diamonds"),
                                                          Card().from_str("4", "Clubs"),
                                                          Card().from_str("4", "Spades"),
                                                          Card().from_str("3", "Hearts")]


def test_find_four_of_a_kind_not_found():
    hand = [Card().from_str("4", "Hearts"),
            Card().from_str("6", "Spades")]
    community_cards = [Card().from_str("4", "Clubs"),
                       Card().from_str("4", "Diamonds"),
                       Card().from_str("3", "Hearts"),
                       Card().from_str("2", "Hearts"),
                       Card().from_str("3", "Spades")]

    assert not find_four_of_a_kind(hand, community_cards)


def test_find_full_house():
    hand = [Card().from_str("4", "Hearts"),
            Card().from_str("4", "Spades")]
    community_cards = [Card().from_str("4", "Clubs"),
                       Card().from_str("3", "Diamonds"),
                       Card().from_str("3", "Hearts"),
                       Card().from_str("2", "Hearts"),
                       Card().from_str("6", "Spades")]

    assert find_full_house(hand, community_cards) == [Card().from_str("4", "Hearts"),
                                                      Card().from_str("4", "Spades"),
                                                      Card().from_str("4", "Clubs"),
                                                      Card().from_str("3", "Diamonds"),
                                                      Card().from_str("3", "Hearts")]


def test_find_full_house_no_pair():
    hand = [Card().from_str("4", "Hearts"),
            Card().from_str("4", "Spades")]
    community_cards = [Card().from_str("4", "Clubs"),
                       Card().from_str("7", "Diamonds"),
                       Card().from_str("8", "Hearts"),
                       Card().from_str("2", "Hearts"),
                       Card().from_str("6", "Spades")]

    assert not find_full_house(hand, community_cards)


def test_find_flush():
    hand = [Card().from_str("4", "Hearts"),
            Card().from_str("9", "Hearts")]
    community_cards = [Card().from_str("6", "Hearts"),
                       Card().from_str("K", "Spades"),
                       Card().from_str("A", "Hearts"),
                       Card().from_str("2", "Hearts"),
                       Card().from_str("3", "Hearts")]

    assert find_flush(hand, community_cards) == [Card().from_str("A", "Hearts"),
                                                 Card().from_str("9", "Hearts"),
                                                 Card().from_str("6", "Hearts"),
                                                 Card().from_str("4", "Hearts"),
                                                 Card().from_str("3", "Hearts")]


def test_find_flush_no_flush():
    hand = [Card().from_str("4", "Hearts"),
            Card().from_str("9", "Spades")]
    community_cards = [Card().from_str("6", "Hearts"),
                       Card().from_str("K", "Spades"),
                       Card().from_str("A", "Hearts"),
                       Card().from_str("2", "Hearts"),
                       Card().from_str("3", "Spades")]

    assert not find_flush(hand, community_cards)


def test_find_full_house_no_three_of_a_kind():
    hand = [Card().from_str("4", "Hearts"),
            Card().from_str("4", "Spades")]
    community_cards = [Card().from_str("5", "Clubs"),
                       Card().from_str("2", "Diamonds"),
                       Card().from_str("3", "Hearts"),
                       Card().from_str("2", "Hearts"),
                       Card().from_str("6", "Spades")]

    assert not find_full_house(hand, community_cards)


def test_find_straight():
    hand = [Card().from_str("2", "Hearts"),
            Card().from_str("5", "Spades")]
    community_cards = [Card().from_str("6", "Hearts"),
                       Card().from_str("7", "Spades"),
                       Card().from_str("8", "Hearts"),
                       Card().from_str("9", "Spades"),
                       Card().from_str("J", "Hearts")]

    assert find_straight(hand, community_cards) == [Card().from_str("9", "Spades"),
                                                    Card().from_str("8", "Hearts"),
                                                    Card().from_str("7", "Spades"),
                                                    Card().from_str("6", "Hearts"),
                                                    Card().from_str("5", "Spades")]


def test_find_straight_no_straight():
    hand = [Card().from_str("2", "Hearts"),
            Card().from_str("5", "Spades")]
    community_cards = [Card().from_str("Q", "Hearts"),
                       Card().from_str("7", "Spades"),
                       Card().from_str("8", "Hearts"),
                       Card().from_str("9", "Spades"),
                       Card().from_str("J", "Hearts")]

    assert not find_straight(hand, community_cards)


def test_find_three_of_a_kind():
    hand = [Card().from_str("5", "Hearts"),
            Card().from_str("5", "Spades")]
    community_cards = [Card().from_str("6", "Hearts"),
                       Card().from_str("7", "Spades"),
                       Card().from_str("5", "Clubs"),
                       Card().from_str("9", "Spades"),
                       Card().from_str("J", "Hearts")]

    assert find_three_of_a_kind(hand, community_cards) == [Card().from_str("5", "Hearts"),
                                                           Card().from_str("5", "Spades"),
                                                           Card().from_str("5", "Clubs"),
                                                           Card().from_str("J", "Hearts"),
                                                           Card().from_str("9", "Spades")]


def test_find_three_of_a_kind_no_three_of_a_kind():
    hand = [Card().from_str("5", "Hearts"),
            Card().from_str("5", "Spades")]
    community_cards = [Card().from_str("6", "Hearts"),
                       Card().from_str("7", "Spades"),
                       Card().from_str("8", "Clubs"),
                       Card().from_str("9", "Spades"),
                       Card().from_str("J", "Hearts")]

    assert not find_three_of_a_kind(hand, community_cards)


def test_find_two_pair():
    hand = [Card().from_str("A", "Hearts"),
            Card().from_str("2", "Spades")]
    community_cards = [Card().from_str("6", "Hearts"),
                       Card().from_str("A", "Spades"),
                       Card().from_str("2", "Clubs"),
                       Card().from_str("9", "Spades"),
                       Card().from_str("J", "Hearts")]

    assert find_two_pair(hand, community_cards) == [Card().from_str("A", "Hearts"),
                                                    Card().from_str("A", "Spades"),
                                                    Card().from_str("2", "Spades"),
                                                    Card().from_str("2", "Clubs"),
                                                    Card().from_str("J", "Hearts")]


def test_find_two_pair_no_two_pair():
    hand = [Card().from_str("A", "Hearts"),
            Card().from_str("2", "Spades")]
    community_cards = [Card().from_str("6", "Hearts"),
                       Card().from_str("A", "Spades"),
                       Card().from_str("3", "Clubs"),
                       Card().from_str("9", "Spades"),
                       Card().from_str("J", "Hearts")]

    assert not find_two_pair(hand, community_cards)


def test_find_single_pair():
    hand = [Card().from_str("A", "Hearts"),
            Card().from_str("2", "Spades")]
    community_cards = [Card().from_str("6", "Hearts"),
                       Card().from_str("A", "Spades"),
                       Card().from_str("3", "Clubs"),
                       Card().from_str("9", "Spades"),
                       Card().from_str("J", "Hearts")]

    assert find_single_pair(hand, community_cards) == [Card().from_str("A", "Hearts"),
                                                       Card().from_str("A", "Spades"),
                                                       Card().from_str("J", "Hearts"),
                                                       Card().from_str("9", "Spades"),
                                                       Card().from_str("6", "Hearts")]


def test_find_single_pair_no_pair():
    hand = [Card().from_str("A", "Hearts"),
            Card().from_str("2", "Spades")]
    community_cards = [Card().from_str("6", "Hearts"),
                       Card().from_str("3", "Spades"),
                       Card().from_str("4", "Clubs"),
                       Card().from_str("9", "Spades"),
                       Card().from_str("J", "Hearts")]

    assert not find_single_pair(hand, community_cards)


def test_find_high_card_hand():
    hand = [Card().from_str("A", "Hearts"),
            Card().from_str("2", "Spades")]
    community_cards = [Card().from_str("6", "Hearts"),
                       Card().from_str("3", "Spades"),
                       Card().from_str("4", "Clubs"),
                       Card().from_str("9", "Spades"),
                       Card().from_str("J", "Hearts")]

    assert find_high_card(hand, community_cards) == [Card().from_str("A", "Hearts"),
                                                     Card().from_str("J", "Hearts"),
                                                     Card().from_str("9", "Spades"),
                                                     Card().from_str("6", "Hearts"),
                                                     Card().from_str("4", "Clubs")]
