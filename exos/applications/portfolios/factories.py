from exos.domains.models.entities import MarketData
from exos.domains.models.values import Price, Symbol, Volume


class MarketDataFactory:
    @classmethod
    def create_market_data(cls, symbol: str, price: float, volume: float):
         # to do
