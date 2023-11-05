"""
Doc: https://binance-docs.github.io/apidocs/spot/en
Github: https://github.com/binance/binance-connector-python

Pypi: https://pypi.org/project/python-binance
Github: https://github.com/sammchardy/python-binance
"""

import pandas as pd
import pendulum
from typing import Dict, Optional
from binance import Client


class BinanceClient(Client):
    def __init__(self,
                 api_key: Optional[str] = None, api_secret: Optional[str] = None,
                 requests_params: Dict[str, str] = None, testnet: bool = False
                 ):
        super(BinanceClient, self).__init__(api_key=api_key, api_secret=api_secret, requests_params=requests_params, testnet=testnet)
        self.balances = self.get_balances()

    def get_balances(self):
        """
        get balance information for the account
        return: [{'asset': 'BNB', 'free': '1000.00000000', 'locked': '0.00000000'}, {...}, ... ]
        """
        info = self.get_account()
        balances = [coin for coin in info['balances'] if float(coin['free']) > 0 or float(coin['locked']) > 0]
        return balances

    def get_all_coins(self, unit: str = 'USDT'):
        """get all coin symbols with `unit` as a base unit"""
        exchange_info = self.get_exchange_info()
        symbols = [info['symbol'] for info in exchange_info['symbols'] if info['symbol'].endswith(unit)]
        return symbols

    def reformat_klines(self, symbol, interval, start_time: int = None, end_time: int = None, limit: int = None):
        """create pd.DataFrame and change data type of columns"""
        # get klines information
        if start_time and end_time:
            klines_info = self.get_klines(symbol=symbol, interval=interval, startTime=start_time, endTime=end_time)
        elif limit:
            klines_info = self.get_klines(symbol=symbol, interval=interval, limit=limit)
        else:
            return pd.DataFrame()
        
        include_columns = [0, 1, 2, 3, 4, 5, 6, 8]

        df = pd.DataFrame(klines_info)
        df = df[include_columns]

        for col in [0, 6]:
            df[col] = df[col].astype('str').str.slice(stop=10).astype('int')
        for col in [1, 2, 3, 4, 5]:
            df[col] = df[col].astype('float')

        df.columns = ['open_time', 'open_price', 'high_price', 'low_price', 'close_price', 'volume', 'close_time', 'number_of_trade']
        
        df['datetime'] = df['open_time'].map(lambda x: pendulum.from_timestamp(x, tz='Asia/Bangkok'))
        df.set_index('datetime', inplace=True)
        df.index = df.index.tz_convert('Asia/Bangkok')
        
        return df


if __name__ == '__main__':
    # TODO: config credential in `../.env` before execute
    import os
    from dotenv import load_dotenv

    # take environment variables from `./..env`
    load_dotenv(dotenv_path="../.env")    

    BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
    BINANCE_API_SECRET = os.getenv('BINANCE_API_SECRET')
    BINANCE_ENABLE_TESTNET = os.getenv('BINANCE_ENABLE_TESTNET')

    binance_client = BinanceClient(api_key=BINANCE_API_KEY, api_secret=BINANCE_API_SECRET, testnet=BINANCE_ENABLE_TESTNET)

    # get account's balances
    balances = binance_client.get_balances()

    # get all coin in the system
    coins = binance_client.get_all_coins()
    print('coin amount: ', len(coins))

    # get current BTC coin data
    df_info = binance_client.reformat_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE, limit=int(24*60/15))
    print(df_info.head())
