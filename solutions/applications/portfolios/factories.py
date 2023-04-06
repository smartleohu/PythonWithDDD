from solutions.domains.models.entities import MarketData
from solutions.domains.models.values import Price, Symbol, Volume


class MarketDataFactory:
    @classmethod
    def create_market_data(cls, symbol: str, price: float, volume: float):
        return MarketData(symbol=Symbol(symbol), price=Price(price),
                          volume=Volume(volume))
