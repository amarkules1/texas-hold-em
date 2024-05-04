from texas_hold_em.deck import Deck


def test_new_draw():
    deck = Deck()
    card = deck.draw()
    assert card.rank == 12
    assert card.suit == 3
    assert len(deck.cards) == 51


def test_all_cards_present():
    deck = Deck()
    for suit in [3, 2, 1, 0]:
        for rank in [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:
            card = deck.draw()
            assert card.rank == rank
            assert card.suit == suit
    assert len(deck.cards) == 0


def test_shuffle():
    deck = Deck()
    deck.shuffle()
    assert len(deck.cards) == 52
    card = deck.draw()
    assert len(deck.cards) == 51
    for card2 in deck.cards:
        assert not (card.rank == card2.rank and card.suit == card2.suit)
