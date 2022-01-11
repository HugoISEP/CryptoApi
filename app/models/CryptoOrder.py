from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CryptoOrder(BaseModel):
    id: str
    clientId: Optional[str]
    market: str
    side: str
    price: Optional[float]
    size: float
    status: str
    filledSize: float
    remainingSize: float
    reduceOnly: bool
    liquidation: bool
    avgFillPrice: Optional[float]
    postOnly: bool
    ioc: bool
    createdAt: datetime
    future: Optional[str]
