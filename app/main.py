from typing import List, Optional

from fastapi.openapi.utils import get_openapi
from starlette.responses import JSONResponse

from app.configuration.Configuration import Configuration
from app.models.CryptoOrder import CryptoOrder
from app.models.FtxBalance import FtxBalance
from app.models.Notification import Notification
from app.security.ApiKeyAuthentication import get_api_key
from app.services.Ftx import Ftx
from app.services.NotificationService import NotificationService
from app.services.TradingBotService import TradingBotService
from fastapi import Depends, FastAPI
from fastapi.security.api_key import APIKey


app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


@app.get("/openapi.json", tags=["documentation"])
async def get_open_api_endpoint(api_key: APIKey = Depends(get_api_key)):
    response = JSONResponse(
        get_openapi(title="FastAPI security test", version="1", routes=app.routes)
    )
    return response


@app.get("/status")
async def get_status(api_key: APIKey = Depends(get_api_key)) -> str:
    return "alive"


@app.get("/bot/{id}/status")
async def get_bot_status(api_key: APIKey = Depends(get_api_key)) -> str:
    conf = Configuration()
    bot_service = TradingBotService(conf.bot_base_url)
    return bot_service.get_status()


@app.get("/bot/{id}/balances")
async def get_bot_balances(api_key: APIKey = Depends(get_api_key)) -> List[FtxBalance]:
    conf = Configuration()
    bot_service = TradingBotService(conf.bot_base_url)
    return bot_service.get_balances()


@app.get("/bot/{id}/markets")
async def get_bot_status(api_key: APIKey = Depends(get_api_key)) -> List[str]:
    conf = Configuration()
    trading_bot_service = TradingBotService(conf.bot_base_url)
    return trading_bot_service.get_markets()


@app.get("/bot/{id}/ordersHistory")
async def get_bot_orders_history(api_key: APIKey = Depends(get_api_key),
                                 market: Optional[str] = None,
                                 side: Optional[str] = None,
                                 order_type: Optional[str] = None,
                                 start_time: Optional[float] = None,
                                 end_time: Optional[float] = None) -> List[CryptoOrder]:
    ftx = Ftx()
    result = ftx.get_orders_history(market, side, order_type, start_time, end_time)
    return result


@app.post("/notification")
async def notification(notif: Notification, api_key: APIKey = Depends(get_api_key)):
    service = NotificationService()
    return service.send_notification(notif)

