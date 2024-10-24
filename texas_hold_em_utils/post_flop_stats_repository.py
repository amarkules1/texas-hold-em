import os

import pandas as pd
from dotenv import load_dotenv, find_dotenv
import sqlalchemy


class PostflopStatsRepository:
    all_data = None

    def __init__(self):
        """
        Constructor for the PreflopStatsRepository
        otherwise gets the data from the csv file. If you don't know what to set this to, leave it as False.
        """
        self.all_data = pd.read_csv(os.path.dirname(__file__) + "/data/post_flop_win_rate_distribution.csv")

    def get_percentile(self, win_rate, player_count, street):
        """
        Gets the percentile for the given win rate, player count, and street
        """
        count = self.all_data.query(f"player_ct == {player_count} and street == '{street}' and win_rate < {win_rate}").shape[0]
        total = self.all_data.query(f"player_ct == {player_count} and street == '{street}'").shape[0]
        return 100 * (count / total)
