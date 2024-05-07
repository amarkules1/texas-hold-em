from texas_hold_em.card import Card
from texas_hold_em.sklansky import sklansky_rank


def test_sklansky_9_q_7_suited():
    rank_1 = "Q"
    suit_1 = "Spades"
    rank_2 = "7"
    suit_2 = "Spades"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 9


def test_sklansky_9_10_6_suited():
    rank_1 = "10"
    suit_1 = "Spades"
    rank_2 = "6"
    suit_2 = "Spades"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 9


def test_sklansky_9_9_5_suited():
    rank_1 = "9"
    suit_1 = "Spades"
    rank_2 = "5"
    suit_2 = "Spades"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 9


def test_sklansky_9_8_4_suited():
    rank_1 = "8"
    suit_1 = "Spades"
    rank_2 = "4"
    suit_2 = "Spades"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 9


def test_sklansky_9_6_3_suited():
    rank_1 = "3"
    suit_1 = "Spades"
    rank_2 = "6"
    suit_2 = "Spades"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 9


def test_sklansky_9_5_2_suited():
    rank_1 = "5"
    suit_1 = "Spades"
    rank_2 = "2"
    suit_2 = "Spades"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 9


def test_sklansky_9_q_8_off():
    rank_1 = "Q"
    suit_1 = "Spades"
    rank_2 = "8"
    suit_2 = "Diamonds"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 9


def test_sklansky_9_6_4_off():
    rank_1 = "6"
    suit_1 = "Spades"
    rank_2 = "4"
    suit_2 = "Diamonds"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 9


def test_sklansky_9_3_4_off():
    rank_1 = "3"
    suit_1 = "Spades"
    rank_2 = "4"
    suit_2 = "Diamonds"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 9


def test_sklansky_9_3_2_off():
    rank_1 = "3"
    suit_1 = "Spades"
    rank_2 = "2"
    suit_2 = "Diamonds"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 9


def test_sklansky_8_9_a_off():
    rank_1 = "9"
    suit_1 = "Diamonds"
    rank_2 = "A"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 8


def test_sklansky_8_9_k_off():
    rank_1 = "9"
    suit_1 = "Diamonds"
    rank_2 = "K"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 8


def test_sklansky_8_9_q_off():
    rank_1 = "9"
    suit_1 = "Diamonds"
    rank_2 = "Q"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 8


def test_sklansky_8_8_j_off():
    rank_1 = "8"
    suit_1 = "Diamonds"
    rank_2 = "J"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 8


def test_sklansky_8_8_10_off():
    rank_1 = "8"
    suit_1 = "Diamonds"
    rank_2 = "10"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 8


def test_sklansky_8_8_7_off():
    rank_1 = "8"
    suit_1 = "Diamonds"
    rank_2 = "7"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 8


def test_sklansky_8_6_7_off():
    rank_1 = "6"
    suit_1 = "Diamonds"
    rank_2 = "7"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 8


def test_sklansky_8_6_5_off():
    rank_1 = "6"
    suit_1 = "Diamonds"
    rank_2 = "5"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 8


def test_sklansky_8_4_5_off():
    rank_1 = "4"
    suit_1 = "Diamonds"
    rank_2 = "5"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 8


def test_sklansky_8_j_7_suited():
    rank_1 = "J"
    suit_1 = "Diamonds"
    rank_2 = "7"
    suit_2 = "Diamonds"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 8


def test_sklansky_8_9_6_suited():
    rank_1 = "9"
    suit_1 = "Diamonds"
    rank_2 = "6"
    suit_2 = "Diamonds"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 8


def test_sklansky_8_8_5_suited():
    rank_1 = "8"
    suit_1 = "Diamonds"
    rank_2 = "5"
    suit_2 = "Diamonds"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 8


def test_sklansky_8_2_4_suited():
    rank_1 = "2"
    suit_1 = "Diamonds"
    rank_2 = "4"
    suit_2 = "Diamonds"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 8


def test_sklansky_8_3_2_suited():
    rank_1 = "3"
    suit_1 = "Diamonds"
    rank_2 = "2"
    suit_2 = "Diamonds"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 8


def test_sklansky_7_k_low_suited():
    rank_1 = "4"
    suit_1 = "Clubs"
    rank_2 = "K"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 7


def test_sklansky_7_q_8_suited():
    rank_1 = "Q"
    suit_1 = "Clubs"
    rank_2 = "8"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 7


def test_sklansky_7_10_7_suited():
    rank_1 = "10"
    suit_1 = "Clubs"
    rank_2 = "7"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 7


def test_sklansky_7_6_5_suited():
    rank_1 = "6"
    suit_1 = "Clubs"
    rank_2 = "5"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 7


def test_sklansky_7_6_4_suited():
    rank_1 = "6"
    suit_1 = "Clubs"
    rank_2 = "5"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 7


def test_sklansky_7_5_3_suited():
    rank_1 = "3"
    suit_1 = "Clubs"
    rank_2 = "5"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 7


def test_sklansky_7_4_3_suited():
    rank_1 = "4"
    suit_1 = "Clubs"
    rank_2 = "3"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 7


def test_sklansky_7_4s():
    rank_1 = "4"
    suit_1 = "Clubs"
    rank_2 = "4"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 7


def test_sklansky_7_3s():
    rank_1 = "3"
    suit_1 = "Clubs"
    rank_2 = "3"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 7


def test_sklansky_7_2s():
    rank_1 = "2"
    suit_1 = "Clubs"
    rank_2 = "2"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 7


def test_sklansky_7_9_j_off():
    rank_1 = "9"
    suit_1 = "Clubs"
    rank_2 = "J"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 7


def test_sklansky_7_9_10_off():
    rank_1 = "9"
    suit_1 = "Clubs"
    rank_2 = "10"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 7


def test_sklansky_7_9_8_off():
    rank_1 = "9"
    suit_1 = "Clubs"
    rank_2 = "8"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 7


def test_sklansky_6_10_a_off():
    rank_1 = "10"
    suit_1 = "Clubs"
    rank_2 = "A"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 6


def test_sklansky_6_10_k_off():
    rank_1 = "10"
    suit_1 = "Clubs"
    rank_2 = "K"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 6


def test_sklansky_6_10_q_off():
    rank_1 = "10"
    suit_1 = "Clubs"
    rank_2 = "Q"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 6


def test_sklansky_6_6s():
    rank_1 = "6"
    suit_1 = "Clubs"
    rank_2 = "6"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 6


def test_sklansky_6_5s():
    rank_1 = "6"
    suit_1 = "Clubs"
    rank_2 = "6"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 6


def test_sklansky_6_k_9_suited():
    rank_1 = "K"
    suit_1 = "Clubs"
    rank_2 = "9"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 6


def test_sklansky_6_j_8_suited():
    rank_1 = "J"
    suit_1 = "Clubs"
    rank_2 = "8"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 6


def test_sklansky_6_6_8_suited():
    rank_1 = "6"
    suit_1 = "Clubs"
    rank_2 = "8"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 6


def test_sklansky_6_4_5_suited():
    rank_1 = "4"
    suit_1 = "Clubs"
    rank_2 = "5"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 6


def test_sklansky_5_ace_low_suited():
    rank_1 = "A"
    suit_1 = "Clubs"
    rank_2 = "9"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 5


def test_sklansky_5_q_9_suited():
    rank_1 = "Q"
    suit_1 = "Clubs"
    rank_2 = "9"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 5


def test_sklansky_5_7_8_suited():
    rank_1 = "7"
    suit_1 = "Clubs"
    rank_2 = "8"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 5


def test_sklansky_5_7_9_suited():
    rank_1 = "7"
    suit_1 = "Clubs"
    rank_2 = "9"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 5


def test_sklansky_5_7_6_suited():
    rank_1 = "7"
    suit_1 = "Clubs"
    rank_2 = "6"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 5


def test_sklansky_5_7s():
    rank_1 = "7"
    suit_1 = "Clubs"
    rank_2 = "7"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 5


def test_sklansky_5_j_k_off():
    rank_1 = "J"
    suit_1 = "Clubs"
    rank_2 = "K"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 5


def test_sklansky_5_j_q_off():
    rank_1 = "J"
    suit_1 = "Clubs"
    rank_2 = "K"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 5


def test_sklansky_5_j_10_off():
    rank_1 = "J"
    suit_1 = "Clubs"
    rank_2 = "10"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 5


def test_sklansky_4_a_j_off():
    rank_1 = "J"
    suit_1 = "Clubs"
    rank_2 = "A"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 4


def test_sklansky_4_q_k_off():
    rank_1 = "Q"
    suit_1 = "Clubs"
    rank_2 = "K"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 4


def test_sklansky_4_8s():
    rank_1 = "8"
    suit_1 = "Clubs"
    rank_2 = "8"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 4


def test_sklansky_4_10_k_suited():
    rank_1 = "10"
    suit_1 = "Clubs"
    rank_2 = "K"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 4


def test_sklansky_4_10_q_suited():
    rank_1 = "10"
    suit_1 = "Clubs"
    rank_2 = "Q"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 4


def test_sklansky_4_9_j_suited():
    rank_1 = "9"
    suit_1 = "Clubs"
    rank_2 = "J"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 4


def test_sklansky_4_9_10_suited():
    rank_1 = "9"
    suit_1 = "Clubs"
    rank_2 = "10"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 4


def test_sklansky_4_9_8_suited():
    rank_1 = "9"
    suit_1 = "Clubs"
    rank_2 = "8"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 4


def test_sklansky_3_a_10_suited():
    rank_1 = "A"
    suit_1 = "Hearts"
    rank_2 = "10"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 3


def test_sklansky_3_k_j_suited():
    rank_1 = "K"
    suit_1 = "Hearts"
    rank_2 = "J"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 3


def test_sklansky_3_q_j_suited():
    rank_1 = "Q"
    suit_1 = "Hearts"
    rank_2 = "J"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 3


def test_sklansky_3_q_a_off():
    rank_1 = "Q"
    suit_1 = "Hearts"
    rank_2 = "A"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 3


def test_sklansky_3_10_a_suited():
    rank_1 = "10"
    suit_1 = "Clubs"
    rank_2 = "A"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 3


def test_sklansky_3_10_j_suited():
    rank_1 = "10"
    suit_1 = "Clubs"
    rank_2 = "J"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 3


def test_sklansky_3_9s():
    rank_1 = "9"
    suit_1 = "Hearts"
    rank_2 = "9"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 3


def test_sklansky_2_ace_king_off():
    rank_1 = "K"
    suit_1 = "Hearts"
    rank_2 = "A"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 2


def test_sklansky_2_q_k_suited():
    rank_1 = "K"
    suit_1 = "Clubs"
    rank_2 = "Q"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 2


def test_sklansky_2_q_a_suited():
    rank_1 = "A"
    suit_1 = "Clubs"
    rank_2 = "Q"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 2


def test_sklansky_2_j_a_suited():
    rank_1 = "A"
    suit_1 = "Clubs"
    rank_2 = "J"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 2


def test_sklansky_2_tens():
    rank_1 = "10"
    suit_1 = "Clubs"
    rank_2 = "10"
    suit_2 = "Hearts"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 2


def test_sklansky_1_high_pair():
    rank_1 = "J"
    suit_1 = "Hearts"
    rank_2 = "J"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 1


def test_sklansky_1_ace_king_suited():
    rank_1 = "A"
    suit_1 = "Clubs"
    rank_2 = "K"
    suit_2 = "Clubs"
    card1 = Card().from_str(rank_1, suit_1)
    card2 = Card().from_str(rank_2, suit_2)

    val = sklansky_rank(card1, card2)
    assert val == 1
