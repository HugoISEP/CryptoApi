from typing import Optional, List

import ftx
from pydantic import parse_obj_as

from app.configuration.Configuration import Configuration
from app.models.CryptoOrder import CryptoOrder


class Ftx:
    _client = None

    def __init__(self):
        config = Configuration()
        self.client = ftx.FtxClient(
            api_key=config.api_key,
            api_secret=config.api_secret,
            subaccount_name=config.subaccount_name
        )

    def get_orders_history(self, market: Optional[str],
                           side: Optional[str],
                           order_type: Optional[str],
                           start_time: Optional[float],
                           end_time: Optional[float]) -> List[CryptoOrder]:
        result = self.client.get_order_history(market, side, order_type, start_time, end_time)
        return parse_obj_as(List[CryptoOrder], result)

    def get_orders_from_market(self):
        return self.client.get_order_history()
