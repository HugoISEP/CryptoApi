from typing import List

from pydantic import BaseModel

from app.models.CryptoOrder import CryptoOrder


class CryptoMarketOrders(BaseModel):
    market: str
    orders: List[CryptoOrder]
