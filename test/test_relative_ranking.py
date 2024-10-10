import pytest

from texas_hold_em_utils.card import Card
from texas_hold_em_utils.preflop_stats_repository import PreflopStatsRepository
from texas_hold_em_utils.relative_ranking import get_hand_rank_details, rank_hand_post_flop, rank_hand_post_turn, \
    rank_hand_post_river


def test_get_hand_rank_details_missing_hand_card():
    hand = [Card().from_ints(0, 0)]
    # should throw exception
    with pytest.raises(ValueError):
        get_hand_rank_details(hand)

def test_get_hand_rank_details_too_many_hand_cards():
    hand = [Card().from_ints(0, 0), Card().from_ints(0, 1), Card().from_ints(0, 2)]
    # should throw exception
    with pytest.raises(ValueError):
        get_hand_rank_details(hand)

def test_get_hand_rank_details_too_many_community_cards():
    hand = [Card().from_ints(0, 0), Card().from_ints(0, 1)]
    community_cards = [Card().from_ints(0, 2),
                       Card().from_ints(0, 3),
                       Card().from_ints(3, 3),
                       Card().from_ints(3, 2),
                       Card().from_ints(3, 1),
                       Card().from_ints(7, 1)]
    # should throw exception
    with pytest.raises(ValueError):
        get_hand_rank_details(hand, community_cards)

def test_get_hand_rank_details_preflop_2_player():
    hand = [Card().from_ints(0, 0), Card().from_ints(0, 1)]
    community_cards = []

    rank_details = get_hand_rank_details(hand, community_cards)

    assert rank_details["expected_win_rate"] == PreflopStatsRepository().get_win_rate(0, 0, False, 2)['win_rate']
    assert rank_details["expected_win_rate"] == rank_details["expected_2_player_win_rate"]
    assert rank_details["percentile"] > 0.0
    assert rank_details["percentile"] < 100.0


def test_get_hand_rank_details_preflop_3_player():
    hand = [Card().from_ints(0, 0), Card().from_ints(0, 1)]
    community_cards = []

    rank_details = get_hand_rank_details(hand, community_cards, player_count=3)

    assert rank_details["expected_win_rate"] == PreflopStatsRepository().get_win_rate(0, 0, False, 3)['win_rate']
    assert rank_details["expected_win_rate"] < rank_details["expected_2_player_win_rate"]
    assert rank_details["percentile"] > 0.0
    assert rank_details["percentile"] < 100.0


def test_get_hand_rank_details_postflop_2_player():
    hand = [Card().from_ints(0, 0), Card().from_ints(0, 1)]
    community_cards = [
        Card().from_ints(3, 2),
        Card().from_ints(3, 1),
        Card().from_ints(7, 1)
    ]

    rank_details = get_hand_rank_details(hand, community_cards, player_count=2)

    # allow a 15% tollerance to avoid random failure due to sample variability
    assert rank_details["expected_win_rate"] * 1.15 > rank_details["expected_2_player_win_rate"]
    assert rank_details["expected_win_rate"] * 0.85 < rank_details["expected_2_player_win_rate"]
    assert rank_details["percentile"] > 0.0
    assert rank_details["percentile"] < 100.0


def test_get_hand_rank_details_postflop_3_player():
    hand = [Card().from_ints(0, 0), Card().from_ints(0, 1)]
    community_cards = [
        Card().from_ints(3, 2),
        Card().from_ints(3, 1),
        Card().from_ints(7, 1)
    ]

    rank_details = get_hand_rank_details(hand, community_cards, player_count=3)

    # allow a 20% tollerance to avoid random failure due to sample variability
    assert rank_details["expected_win_rate"] * 1.2 > rank_hand_post_flop(hand, community_cards, n_other_players=2)
    assert rank_details["expected_win_rate"] * 0.8 < rank_hand_post_flop(hand, community_cards, n_other_players=2)
    assert rank_details["expected_win_rate"] < rank_details["expected_2_player_win_rate"]
    assert rank_details["percentile"] > 0.0
    assert rank_details["percentile"] < 100.0


def test_get_hand_rank_details_postturn_2_player():
    hand = [Card().from_ints(0, 0), Card().from_ints(0, 1)]
    community_cards = [
        Card().from_ints(3, 2),
        Card().from_ints(3, 1),
        Card().from_ints(7, 1),
        Card().from_ints(8, 1)
    ]

    rank_details = get_hand_rank_details(hand, community_cards, player_count=2)

    # allow a 15% tollerance to avoid random failure due to sample variability
    assert rank_details["expected_win_rate"] * 1.15 > rank_details["expected_2_player_win_rate"]
    assert rank_details["expected_win_rate"] * 0.85 < rank_details["expected_2_player_win_rate"]
    assert rank_details["percentile"] > 0.0
    assert rank_details["percentile"] < 100.0


def test_get_hand_rank_details_postturn_3_player():
    hand = [Card().from_ints(0, 0), Card().from_ints(0, 1)]
    community_cards = [
        Card().from_ints(3, 2),
        Card().from_ints(3, 1),
        Card().from_ints(7, 1),
        Card().from_ints(8, 1)
    ]

    rank_details = get_hand_rank_details(hand, community_cards, player_count=3)

    # allow a 15% tollerance to avoid random failure due to sample variability
    assert rank_details["expected_win_rate"] * 1.15 > rank_hand_post_turn(hand, community_cards, n_other_players=2)
    assert rank_details["expected_win_rate"] * 0.85 < rank_hand_post_turn(hand, community_cards, n_other_players=2)
    assert rank_details["expected_win_rate"] < rank_details["expected_2_player_win_rate"]
    assert rank_details["percentile"] > 0.0
    assert rank_details["percentile"] < 100.0


def test_get_hand_rank_details_postriver_2_player():
    hand = [Card().from_ints(0, 0), Card().from_ints(0, 1)]
    community_cards = [
        Card().from_ints(3, 2),
        Card().from_ints(3, 1),
        Card().from_ints(7, 1),
        Card().from_ints(8, 1),
        Card().from_ints(9, 1)
    ]

    rank_details = get_hand_rank_details(hand, community_cards, player_count=2)

    # allow a 15% tollerance to avoid random failure due to sample variability
    assert rank_details["expected_win_rate"] == rank_details["expected_2_player_win_rate"]
    assert rank_details["percentile"] > 0.0
    assert rank_details["percentile"] < 100.0


def test_get_hand_rank_details_postriver_3_player():
    hand = [Card().from_ints(0, 0), Card().from_ints(0, 1)]
    community_cards = [
        Card().from_ints(3, 2),
        Card().from_ints(3, 1),
        Card().from_ints(7, 1),
        Card().from_ints(8, 1),
        Card().from_ints(9, 1)
    ]

    rank_details = get_hand_rank_details(hand, community_cards, player_count=3)

    # allow a 15% tollerance to avoid random failure due to sample variability
    assert rank_details["expected_win_rate"] == (rank_hand_post_river(hand, community_cards) ** 2)
    assert rank_details["expected_win_rate"] < rank_details["expected_2_player_win_rate"]
    assert rank_details["percentile"] > 0.0
    assert rank_details["percentile"] < 100.0
