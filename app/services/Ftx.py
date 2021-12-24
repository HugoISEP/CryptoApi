import ftx
from app.configuration.Configuration import Configuration


class Ftx:
    client = None

    def __init__(self):
        config = Configuration()
        self.client = ftx.FtxClient(
            api_key=config.api_key,
            api_secret=config.api_secret,
            subaccount_name=config.subaccount_name
        )

    def get_orders_from_market(self):
        return self.client.get_order_history()
