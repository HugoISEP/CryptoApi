from typing import List, Optional

from fastapi import FastAPI

from app.configuration.Configuration import Configuration
from app.models.CryptoOrder import CryptoOrder
from app.models.FtxBalance import FtxBalance
from app.services.Ftx import Ftx
from app.services.TradingBotService import TradingBotService

app = FastAPI(debug=True)


@app.get("/status")
def get_status() -> str:
    return "alive"


@app.get("/bot/{id}/status")
def get_bot_status() -> str:
    conf = Configuration()
    bot_service = TradingBotService(conf.bot_base_url)
    return bot_service.get_status()


@app.get("/bot/{id}/balances")
def get_bot_balances() -> List[FtxBalance]:
    conf = Configuration()
    bot_service = TradingBotService(conf.bot_base_url)
    return bot_service.get_balances()


@app.get("/bot/{id}/markets")
def get_bot_status() -> List[str]:
    conf = Configuration()
    trading_bot_service = TradingBotService(conf.bot_base_url)
    return trading_bot_service.get_markets()


@app.get("/bot/{id}/ordersHistory")
def get_bot_orders_history(market: Optional[str] = None,
                           side: Optional[str] = None,
                           order_type: Optional[str] = None,
                           start_time: Optional[float] = None,
                           end_time: Optional[float] = None) -> List[CryptoOrder]:
    ftx = Ftx()
    result = ftx.get_orders_history(market, side, order_type, start_time, end_time)
    return result
