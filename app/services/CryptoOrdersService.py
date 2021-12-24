from typing import List

from pydantic import parse_obj_as

from app.models.CryptoMarketOrders import CryptoMarketOrders
from app.models.CryptoOrder import CryptoOrder
from app.services.Ftx import Ftx


class CryptoOrdersService:
    ftx = Ftx()

    def get_orders_history(self):
        response = self.ftx.get_orders_from_market()
        orders_history: List[CryptoOrder] = parse_obj_as(List[CryptoOrder], response)
        return orders_history

