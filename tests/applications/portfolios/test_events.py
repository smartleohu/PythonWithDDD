from solutions.applications.market_data.events import MarketDataFetched
from solutions.domains.models.values import Price, Symbol, Volume


class TestMarketDataFetched:
    def test_market_data_fetched(self):
        symbol = Symbol('AAPL')
        price = Price(100)
        volume = Volume(1000)
        event = MarketDataFetched(symbol, price, volume)
        assert event.symbol == symbol
        assert event.price == price
        assert event.volume == volume
