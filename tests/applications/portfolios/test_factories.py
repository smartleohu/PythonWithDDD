from solutions.applications.portfolios.factories import MarketDataFactory


class TestMarketDataFactory:
    def test_create_market_data(self):
        symbol = "AAPL"
        price = 100.0
        volume = 200.0
        market_data = MarketDataFactory.create_market_data(
            symbol=symbol, price=price, volume=volume)
        assert market_data.symbol.name == symbol
        assert market_data.price.value == price
        assert market_data.volume.value == volume
