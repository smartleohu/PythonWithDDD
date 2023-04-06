import pytest

from solutions.applications.globals.contexts import ApplicationContext
from solutions.applications.portfolios.factories import MarketDataFactory
from solutions.applications.portfolios.repositories import PortfolioRepository
from solutions.applications.risks.contexts import PortfolioContext, \
    RiskManagementContext
from solutions.domains.services.market_data import MarketDataService


class TestApplicationContext:
    @pytest.fixture
    def application_context(self):
        return ApplicationContext()

    def test_portfolio_repository(self, application_context):
        assert isinstance(application_context.portfolio_repository,
                          PortfolioRepository)

    def test_market_data_repository(self, application_context):
        assert isinstance(application_context.market_data_repository,
                          MarketDataService)

    def test_market_data_factory(self, application_context):
        assert isinstance(application_context.market_data_factory,
                          MarketDataFactory)

    def test_market_data_fetched_handler(self, application_context):
        assert callable(application_context.market_data_fetched_handler)

    def test_portfolio_context(self, application_context):
        assert isinstance(application_context.portfolio_context,
                          PortfolioContext)

    def test_risk_management_context(self, application_context):
        assert isinstance(application_context.risk_management_context,
                          RiskManagementContext)
