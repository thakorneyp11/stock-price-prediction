import os
from dotenv import load_dotenv

from utils.binance_client import BinanceClient


load_dotenv()  # take environment variables from `.env`

BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
BINANCE_API_SECRET = os.getenv('BINANCE_API_SECRET')
BINANCE_ENABLE_TESTNET = os.getenv('BINANCE_ENABLE_TESTNET')

binance_client = BinanceClient(api_key=BINANCE_API_KEY, api_secret=BINANCE_API_SECRET, testnet=BINANCE_ENABLE_TESTNET)

# get current BTC coin data
df_info = binance_client.reformat_klines(symbol='BTCUSDT', interval=binance_client.KLINE_INTERVAL_15MINUTE, limit=int(24*60/15))
print(df_info)
