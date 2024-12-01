from texas_hold_em_utils.card import Card


def test_greater_than():
    card1 = Card().from_ints(0, 0)
    card2 = Card().from_ints(1, 0)
    assert card2.is_higher_than(card1)


def test_less_than():
    card1 = Card().from_ints(0, 0)
    card2 = Card().from_ints(1, 0)
    assert card1.is_lower_than(card2)


def test_equal():
    card1 = Card().from_ints(0, 0)
    card2 = Card().from_ints(0, 0)
    assert not card1.is_higher_than(card2)
    assert not card1.is_lower_than(card2)


def test_same_suit():
    card1 = Card().from_ints(0, 0)
    card2 = Card().from_ints(1, 0)
    assert card1.is_same_suit(card2)


def test_different_suit():
    card1 = Card().from_ints(0, 0)
    card2 = Card().from_ints(0, 1)
    assert not card1.is_same_suit(card2)


def test_from_str():
    actual = Card().from_str("2", 's')

    assert actual.rank == 0
    assert actual.suit == 3


def test_from_str_ten():
    actual = Card().from_str("T", 'd')

    assert actual.rank == 8
    assert actual.suit == 1

