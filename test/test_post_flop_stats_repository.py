
import pytest
from texas_hold_em_utils.post_flop_stats_repository import PostflopStatsRepository

@pytest.fixture
def repo():
    return PostflopStatsRepository()
def test_get_percentile_flop_3_players(repo):
    percentile = repo.get_percentile(0.4806666666666667, 3, 'flop')
    assert isinstance(percentile, float)
    assert 0 <= percentile <= 1

def test_get_percentile_turn_4_players(repo):
    percentile = repo.get_percentile(0.5, 4, 'turn')
    assert isinstance(percentile, float)
    assert 0 <= percentile <= 1

def test_get_percentile_edge_cases(repo):
    # Test with minimum win rate
    min_percentile = repo.get_percentile(0.0, 3, 'flop')
    assert isinstance(min_percentile, float)
    assert min_percentile == 0.0

    # Test with maximum win rate
    max_percentile = repo.get_percentile(1.0, 3, 'flop')
    assert isinstance(max_percentile, float)
    assert max_percentile > 0.999

def test_get_percentile_different_player_counts(repo):
    for player_count in [3, 4, 5, 6]:
        percentile = repo.get_percentile(0.5, player_count, 'flop')
        assert isinstance(percentile, float)
        assert 0 <= percentile <= 1

def test_get_percentile_all_streets(repo):
    for street in ['flop', 'turn', 'river']:
        percentile = repo.get_percentile(0.5, 3, street)
        assert isinstance(percentile, float)
        assert 0 <= percentile <= 1
