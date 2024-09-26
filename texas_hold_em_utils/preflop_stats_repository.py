import os

import pandas as pd
from dotenv import load_dotenv, find_dotenv
import sqlalchemy


class PreflopStatsRepository:
    conn = None
    use_database = False
    all_data = None

    def __init__(self, use_database=False):
        """
        Constructor for the PreflopStatsRepository
        :param use_database: Default False. gets the data from the database if True and DATABASE_CONN_STRING env variable is set,
        otherwise gets the data from the csv file. If you don't know what to set this to, leave it as False.
        """
        self.use_database = use_database
        if use_database and os.getenv("DATABASE_CONN_STRING"):
            _ = load_dotenv(find_dotenv())
            self.conn = sqlalchemy.create_engine(os.getenv("DATABASE_CONN_STRING")).connect()
        else:
            self.all_data = pd.read_csv(os.path.dirname(__file__) + "/data/win_rates.csv")

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
        if self.all_data is not None and not self.use_database:
            data = self.all_data.query(f"player_count == {player_count} and card_1_rank == {card1_rank} and "
                                       f"card_2_rank == {card2_rank} and {'' if suited else 'not '}suited")
        else:
            data = pd.read_sql(sqlalchemy.sql.text(f"select * from poker.win_rates where player_count = {player_count} and "
                                                   f"card_1_rank = '{card1_rank}' and card_2_rank = '{card2_rank}' "
                                                   f"and {'' if suited else 'not '}suited"), self.conn)
        return data.iloc[0].to_dict()
