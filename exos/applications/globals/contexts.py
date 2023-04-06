import asyncio
from datetime import datetime

from exos.applications.portfolios.contexts import PortfolioContext
from exos.applications.market_data.events import MarketDataFetched
from exos.applications.portfolios.factories import MarketDataFactory
from exos.applications.portfolios.repositories import PortfolioRepository
from exos.applications.risks.contexts import RiskManagementContext
from exos.domains.services.market_data import MarketDataService
from exos.utils.loggers import logger


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
        # to do


if __name__ == '__main__':
    asyncio.run(ApplicationContext().run())
