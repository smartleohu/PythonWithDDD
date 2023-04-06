from solutions.domains.models.values import Price, Symbol, Volume, Weight


class TestSymbol:
    def test_init(self):
        symbol = Symbol('AAPL')
        assert symbol.name == 'AAPL'

    def test_equality(self):
        symbol1 = Symbol('AAPL')
        symbol2 = Symbol('AAPL')
        symbol3 = Symbol('GOOGL')
        assert symbol1 == symbol2
        assert symbol1 != symbol3


class TestPrice:
    def test_init(self):
        price = Price(100.0)
        assert price.value == 100.0

    def test_equality(self):
        price1 = Price(100.0)
        price2 = Price(100.0)
        price3 = Price(200.0)
        assert price1 == price2
        assert price1 != price3


class TestVolume:
    def test_init(self):
        volume = Volume(100.0)
        assert volume.value == 100.0

    def test_equality(self):
        volume1 = Volume(100.0)
        volume2 = Volume(100.0)
        volume3 = Volume(200.0)
        assert volume1 == volume2
        assert volume1 != volume3


class TestWeight:
    def test_init(self):
        weight = Weight(0.5)
        assert weight.value == 0.5

    def test_equality(self):
        weight1 = Weight(0.5)
        weight2 = Weight(0.5)
        weight3 = Weight(0.7)
        assert weight1 == weight2
        assert weight1 != weight3
