from unittest.mock import Mock

import pytest

from solutions.applications.portfolios.factories import MarketDataFactory
from solutions.applications.portfolios.repositories import PortfolioRepository
from solutions.applications.risks.contexts import PortfolioContext, \
    RiskManagementContext
from solutions.domains.models.aggregates import Portfolio
from solutions.domains.models.entities import Asset, MarketData
from solutions.domains.models.values import Price, Symbol, Volume, Weight
from solutions.domains.services.market_data import MarketDataService


class TestRiskManagementContext:
    @pytest.fixture
    def market_data_service(self):
        return Mock(spec=MarketDataService)

    @pytest.fixture
    def market_data_factory(self):
        return Mock(spec=MarketDataFactory)

    @pytest.fixture
    def portfolio_repository(self):
        return Mock(spec=PortfolioRepository)

    @pytest.fixture
    def portfolio_context(self, portfolio_repository, market_data_service,
                          market_data_factory):
        return PortfolioContext(
            portfolio_repository=portfolio_repository,
            market_data_service=market_data_service,
            market_data_factory=market_data_factory,
            market_data_fetched_handler=None)

    @pytest.fixture
    def risk_management_context(self, portfolio_context):
        return RiskManagementContext(portfolio_context)

    def test_calculate_portfolio_risk(self, risk_management_context):
        aapl = Asset(symbol=Symbol('AAPL'), weight=Weight(0.5))
        googl = Asset(symbol=Symbol('GOOGL'), weight=Weight(0.5))
        risk_management_context.portfolio_context.portfolio = Portfolio(
            assets=[aapl, googl])
        risk_management_context.portfolio_context.market_data = {
            'AAPL': MarketData(symbol=Symbol('AAPL'), price=Price(100.0),
                               volume=Volume(200.0)),
            'GOOGL': MarketData(symbol=Symbol('GOOGL'), price=Price(200.0),
                                volume=Volume(100.0))
        }
        assert risk_management_context.calculate_portfolio_risk() == 1.25
