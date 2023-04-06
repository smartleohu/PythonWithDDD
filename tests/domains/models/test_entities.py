from solutions.domains.models.entities import MarketData, Asset
from solutions.domains.models.values import Price, Symbol, Volume, Weight


class TestAsset:
    def test_init(self):
        symbol = Symbol("AAPL")
        weight = Weight(0.5)
        asset = Asset(symbol=symbol, weight=weight)
        assert asset.symbol == symbol
        assert asset.weight == weight

    def test_equality(self):
        symbol = Symbol("AAPL")
        weight = Weight(0.5)
        asset = Asset(symbol=symbol, weight=weight)
        asset2 = Asset(symbol=symbol, weight=weight)
        assert asset != asset2


class TestMarketData:
    def test_init(self):
        symbol = Symbol('AAPL')
        price = Price(100.0)
        volume = Volume(100.0)
        md = MarketData(symbol=symbol, price=price, volume=volume)
        assert md.symbol == symbol
        assert md.price == price
        assert md.volume == volume

    def test_equality(self):
        symbol = Symbol('AAPL')
        price = Price(100.0)
        volume = Volume(100.0)
        md = MarketData(symbol=symbol, price=price, volume=volume)
        md2 = MarketData(symbol=symbol, price=price, volume=volume)
        assert md != md2
