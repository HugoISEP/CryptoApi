from fastapi import FastAPI

from app.configuration.Configuration import Configuration
from app.services.CryptoOrdersService import CryptoOrdersService
from app.services.TradingBotService import TradingBotService

app = FastAPI(debug=True)


@app.get("/status")
def get_status():
    return "alive"


@app.get("/ordersHistory")
def get_orders_history():
    orders_service = CryptoOrdersService()
    print(orders_service.get_orders_history())
    return "alive"


@app.get("/bot/{id}/status")
def get_status():
    conf = Configuration()
    bot_service = TradingBotService(conf.bot_base_url)
    return bot_service.get_status()
