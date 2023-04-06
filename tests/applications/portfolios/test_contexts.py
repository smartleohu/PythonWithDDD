from unittest.mock import Mock

import pytest

from solutions.applications.market_data.events import MarketDataFetched
from solutions.applications.portfolios.factories import MarketDataFactory
from solutions.applications.portfolios.repositories import PortfolioRepository
from solutions.applications.risks.contexts import PortfolioContext
from solutions.domains.models.aggregates import Portfolio
from solutions.domains.models.entities import Asset, MarketData
from solutions.domains.models.values import Price, Symbol, Volume, Weight
from solutions.domains.services.market_data import MarketDataService


class TestPortfolioContext:
    @pytest.fixture
    def portfolio_repository(self):
        return PortfolioRepository()

    @pytest.fixture
    def market_data_service(self):
        return Mock(spec=MarketDataService)

    @pytest.fixture
    def market_data_factory(self):
        return Mock(spec=MarketDataFactory)

    @pytest.fixture
    def market_data_fetched_handler(self):
        return Mock(spec=MarketDataFetched)

    @pytest.fixture
    def portfolio_context(self, portfolio_repository, market_data_service,
                          market_data_factory, market_data_fetched_handler):
        return PortfolioContext(
            portfolio_repository=portfolio_repository,
            market_data_service=market_data_service,
            market_data_factory=market_data_factory,
            market_data_fetched_handler=market_data_fetched_handler
        )

    @pytest.mark.asyncio
    async def test_fetch_market_data(self, portfolio_context,
                                     market_data_service,
                                     market_data_fetched_handler):
        # Create mock market data responses
        aapl_market_data = Mock(spec=MarketData)
        aapl_market_data.symbol = Symbol("AAPL")
        aapl_market_data.price = Price(200.0)
        aapl_market_data.volume = Volume(500.0)
        googl_market_data = Mock(spec=MarketData)
        googl_market_data.symbol = Symbol("GOOGL")
        googl_market_data.price = Price(300.0)
        googl_market_data.volume = Volume(600.0)

        # Set up mock market data service to return the mock market data
        # responses
        market_data_service.get_market_data_for_assets.return_value = [
            aapl_market_data,
            googl_market_data,
        ]

        # Call the fetch_market_data method to test
        await portfolio_context.fetch_market_data()

        # Check that the market data was fetched and stored correctly
        assert portfolio_context.get_market_data(
            Symbol("AAPL")) == aapl_market_data
        assert portfolio_context.get_market_data(
            Symbol("GOOGL")) == googl_market_data
        assert len(portfolio_context.market_data) == 2
        assert market_data_fetched_handler.call_count == 2

    def test_get_market_data(self, portfolio_context):
        portfolio_context.market_data = {
            'AAPL': MarketData(symbol=Symbol('AAPL'), price=Price(130.0),
                               volume=Volume(1000)),
            'GOOGL': MarketData(symbol=Symbol('GOOGL'), price=Price(2500.0),
                                volume=Volume(500))
        }
        assert portfolio_context.get_market_data(Symbol('AAPL')) == \
               portfolio_context.market_data['AAPL']
        assert portfolio_context.get_market_data(Symbol('GOOGL')) == \
               portfolio_context.market_data['GOOGL']

    def test_calculate_risk(self, portfolio_context):
        portfolio_context.portfolio = Portfolio(assets=[
            Asset(symbol=Symbol('AAPL'), weight=Weight(0.5)),
            Asset(symbol=Symbol('GOOGL'), weight=Weight(0.5))
        ])
        portfolio_context.market_data = {
            'AAPL': MarketData(symbol=Symbol('AAPL'), price=Price(130.0),
                               volume=Volume(1000)),
            'GOOGL': MarketData(symbol=Symbol('GOOGL'), price=Price(2500.0),
                                volume=Volume(500))
        }
        assert portfolio_context.calculate_risk() == pytest.approx(2.565,
                                                                   rel=1e-4)

    def test_total_weight(self, portfolio_context):
        portfolio_context.portfolio = Portfolio(assets=[
            Asset(symbol=Symbol('AAPL'), weight=Weight(0.5)),
            Asset(symbol=Symbol('GOOGL'), weight=Weight(0.5))
        ])
        assert portfolio_context.total_weight() == 1.0
