from solutions.applications.market_data.events import MarketDataFetched
from solutions.applications.portfolios.factories import MarketDataFactory
from solutions.applications.portfolios.repositories import PortfolioRepository
from solutions.domains.models.values import Symbol
from solutions.domains.services.market_data import MarketDataService


# Contexte borné PortfolioContext
class PortfolioContext:
    def __init__(self, portfolio_repository: PortfolioRepository,
                 market_data_service: MarketDataService,
                 market_data_factory: MarketDataFactory,
                 market_data_fetched_handler):
        self.portfolio_repository = portfolio_repository
        self.market_data_service = market_data_service
        self.market_data_factory = market_data_factory
        self.portfolio = None
        self.market_data = {}
        self._market_data_fetched_handler = market_data_fetched_handler

    async def fetch_market_data(self):
        self.portfolio = self.portfolio_repository.portfolio
        market_data = \
            await self.market_data_service.get_market_data_for_assets(
                self.portfolio.assets)
        for md in market_data:
            self.market_data[md.symbol.name] = md
            self._market_data_fetched_handler(MarketDataFetched(
                md.symbol, md.price, md.volume))

    def get_market_data(self, symbol: Symbol):
        return self.market_data[symbol.name]

    def calculate_risk(self) -> float:
        return sum(asset.weight.value
                   * self.market_data[asset.symbol.name].price.value
                   / self.market_data[asset.symbol.name].volume.value
                   for asset in self.portfolio.assets) / self.total_weight()

    def total_weight(self):
        return self.portfolio.total_weight()
