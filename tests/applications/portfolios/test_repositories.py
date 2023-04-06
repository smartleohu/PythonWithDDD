from unittest.mock import Mock

from solutions.applications.portfolios.repositories import PortfolioRepository
from solutions.domains.models.aggregates import Portfolio
from solutions.domains.models.values import Symbol, Weight


class TestPortfolioRepository:
    def test_init(self):
        portfolio_repository = PortfolioRepository()
        assert len(portfolio_repository.portfolio.assets) == 2

    def test_get(self, monkeypatch):
        # Mock the db_connector to return a dummy value
        mock_db_connector = Mock(return_value='dummy value')
        monkeypatch.setattr(PortfolioRepository, "db_connector",
                            mock_db_connector)

        # Create the repository instance
        repo = PortfolioRepository()

        # Call the get method and check that it returns the expected portfolio
        portfolio = repo.get()
        assert isinstance(portfolio, Portfolio)
        assert len(portfolio.assets) == 2
        assert portfolio.assets[0].symbol == Symbol('AAPL')
        assert portfolio.assets[0].weight == Weight(0.5)
        assert portfolio.assets[1].symbol == Symbol('GOOGL')
        assert portfolio.assets[1].weight == Weight(0.5)
