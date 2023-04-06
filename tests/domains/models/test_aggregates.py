from solutions.domains.models.aggregates import Portfolio
from solutions.domains.models.entities import Asset
from solutions.domains.models.values import Symbol, Weight


class TestPortfolio:
    def test_total_weight(self):
        symbol1 = Symbol("AAPL")
        symbol2 = Symbol("GOOGL")
        weight1 = Weight(0.5)
        weight2 = Weight(0.3)
        assets = [Asset(symbol=symbol1, weight=weight1),
                  Asset(symbol=symbol2, weight=weight2)]
        portfolio = Portfolio(assets=assets)
        assert portfolio.total_weight() == weight1.value + weight2.value
