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
