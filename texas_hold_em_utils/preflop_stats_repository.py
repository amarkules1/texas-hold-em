import os

import pandas as pd
from dotenv import load_dotenv, find_dotenv
import sqlalchemy


class PreflopStatsRepository:
    conn = None
    all_data = None

    def __init__(self):
        """
        Constructor for the PreflopStatsRepository
        """
        self.all_data = pd.read_csv(os.path.dirname(__file__) + "/data/preflop_win_rates.csv")

    def get_win_rate(self, card1_rank, card2_rank, suited, player_count):
        """
        Gets win rate and related info for the given cards and player count
        :param card1_rank: 0-12, 0 is 2, 12 is Ace
        :param card2_rank: 0-12, 0 is 2, 12 is Ace
        :param suited: True if the cards are the same suite, False otherwise
        :param player_count: number of players in the game
        :return: a dict with the following values: card_1_rank, card_2_rank, suited, win_rate, rank, percentile,
        player_count, sklansky, sklansky_position, modified_sklansky, modified_sklansky_position
        """
        if card1_rank == card2_rank and suited:
            raise ValueError("Cannot have the same card twice")
        data = self.all_data.query(f"player_count == {player_count} and card_1_rank == {card1_rank} and "
                                   f"card_2_rank == {card2_rank} and {'' if suited else 'not '}suited")
        return data.iloc[0].to_dict()
