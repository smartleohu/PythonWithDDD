import asyncio
from datetime import datetime

from solutions.applications.portfolios.contexts import PortfolioContext
from solutions.applications.market_data.events import MarketDataFetched
from solutions.applications.portfolios.factories import MarketDataFactory
from solutions.applications.portfolios.repositories import PortfolioRepository
from solutions.applications.risks.contexts import RiskManagementContext
from solutions.domains.services.market_data import MarketDataService
from solutions.utils.loggers import logger


# Contexte global ApplicationContext
class ApplicationContext:
    def __init__(self):
        self.portfolio_repository = PortfolioRepository()
        self.market_data_repository = MarketDataService()
        self.market_data_factory = MarketDataFactory()
        self.market_data_fetched_handler = self.on_market_data_fetched
        self.portfolio_context = PortfolioContext(
            portfolio_repository=self.portfolio_repository,
            market_data_service=self.market_data_repository,
            market_data_factory=self.market_data_factory,
            market_data_fetched_handler=self.market_data_fetched_handler)
        self.risk_management_context = RiskManagementContext(
            portfolio_context=self.portfolio_context)

    @classmethod
    def on_market_data_fetched(cls, event: MarketDataFetched):
        logger.info(
            f"Received event: {event.symbol.name}, {event.price.value}, "
            f"{event.volume.value} on "
            f"{datetime.fromtimestamp(event.timestamp)}")

    async def run(self):
        await self.portfolio_context.fetch_market_data()
        portfolio_risk = \
            self.risk_management_context.calculate_portfolio_risk()
        logger.info(f"Portfolio risk: {portfolio_risk}")


if __name__ == '__main__':
    asyncio.run(ApplicationContext().run())
