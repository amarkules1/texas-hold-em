from texas_hold_em_utils.preflop_stats_repository import PreflopStatsRepository


def test_get_win_rate():
    repo = PreflopStatsRepository()
    win_rate_info = repo.get_win_rate(0, 1, True, 2)

    assert win_rate_info['player_count'] == 2
