import os

import pandas as pd
from dotenv import load_dotenv, find_dotenv
import sqlalchemy


class PreflopStatsRepository:
    conn = None

    def __init__(self):
        _ = load_dotenv(find_dotenv())
        self.conn = sqlalchemy.create_engine(os.getenv("DATABASE_CONN_STRING")).connect()

    def get_win_rate(self, card1_rank, card2_rank, suited, player_count):
        data = pd.read_sql(sqlalchemy.sql.text(f"select * from poker.win_rates where player_count = {player_count} and "
                                               f"card_1_rank = '{card1_rank}' and card_2_rank = '{card2_rank}' "
                                               f"and {'' if suited else 'not '}suited"), self.conn)
        return data.iloc[0].to_dict()
