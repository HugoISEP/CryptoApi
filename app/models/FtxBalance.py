from pydantic import BaseModel


class FtxBalance(BaseModel):
    coin: str
    total = float
    free: float
    availableWithoutBorrow: float
    usdValue: float
    spotBorrow: float
