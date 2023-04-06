from solutions.domains.models.values import Price, Symbol, Volume
from solutions.utils.datetimes import utc_now_tsp


class MarketDataFetched:
    def __init__(self, symbol: Symbol, price: Price, volume: Volume,
                 timestamp: float = utc_now_tsp):
        self.symbol = symbol
        self.price = price
        self.volume = volume
        self.timestamp = timestamp
