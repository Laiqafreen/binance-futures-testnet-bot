import os
import time
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        # 🔥 Auto sync with Binance server time
        self._sync_time()

    def _sync_time(self):
        server_time = self.client.get_server_time()
        self.client.timestamp_offset = server_time['serverTime'] - int(time.time() * 1000)

    def create_order(self, order_data):
        return self.client.futures_create_order(**order_data)