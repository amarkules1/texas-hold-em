import os

import pandas as pd
from dotenv import load_dotenv, find_dotenv
import sqlalchemy


class PreflopStatsRepository:
    conn = None
    use_database = False
    all_data = None

    def __init__(self, use_database=False):
        self.use_database = use_database
        if use_database:
            _ = load_dotenv(find_dotenv())
            self.conn = sqlalchemy.create_engine(os.getenv("DATABASE_CONN_STRING")).connect()
        else:
            self.all_data = pd.read_csv(os.path.dirname(__file__) + "/data/win_rates.csv")

    def get_win_rate(self, card1_rank, card2_rank, suited, player_count):
        if self.all_data is not None and not self.use_database:
            data = self.all_data.query(f"player_count == {player_count} and card_1_rank == {card1_rank} and "
                                       f"card_2_rank == {card2_rank} and {'' if suited else 'not '}suited")
        else:
            data = pd.read_sql(sqlalchemy.sql.text(f"select * from poker.win_rates where player_count = {player_count} and "
                                                   f"card_1_rank = '{card1_rank}' and card_2_rank = '{card2_rank}' "
                                                   f"and {'' if suited else 'not '}suited"), self.conn)
        return data.iloc[0].to_dict()
