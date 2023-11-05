""" Download historical data from Binance Data Dumper using `binance_historical_data` library.
CSV data will be downloaded under `./spot/daily` and `./spot/monthly` folders.
source: https://pypi.org/project/binance-historical-data/

Data format from Binance Data Dumper:
[
    [
        "Open time",  # - Timestamp
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
        "Close time",  # - Timestamp
        "Quote asset volume",
        "Number of trades",
        "Taker buy base asset volume",
        "Taker buy quote asset volume",
        "Ignore",
    ],
    ...
]
"""

import os
import pandas as pd
from binance_historical_data import BinanceDataDumper


data_dumper = BinanceDataDumper(
    path_dir_where_to_dump=".",
    asset_class="spot",  # spot, um, cm
    data_type="klines",  # aggTrades, klines, trades
    data_frequency="15m",
)

# download data to local directory
data_dumper.dump_data(
    tickers=['BTCUSDT'],  # `None` means all tickers
    date_start=None,  # `None` means from the earliest date
    date_end=None,  # `None` means up to the latest date
    is_to_update_existing=True
)

# get all csv paths
csv_directory = "spot/monthly/klines/BTCUSDT/15m"
csv_paths = [os.path.join(csv_directory, csv) for csv in os.listdir(csv_directory)]
csv_paths = sorted(csv_paths)

# read all `csv_paths` into dataframes and concat them together
dfs = list()
for csv_path in csv_paths:
    df = pd.read_csv(csv_path)
    df.columns = ['open_time', 'open_price', 'high_price', 'low_price', 'close_price', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trade', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore']
    dfs.append(df)  

# export to csv
df_all = pd.concat(dfs)
df_all.to_csv("dataset/BTCUSDT_15m_Aug2017-Oct2023.csv", index=False)
