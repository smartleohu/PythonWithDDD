from exos.applications.market_data.events import MarketDataFetched
from exos.applications.portfolios.factories import MarketDataFactory
from exos.applications.portfolios.repositories import PortfolioRepository
from exos.domains.models.values import Symbol
from exos.domains.services.market_data import MarketDataService


# Contexte borné PortfolioContext
class PortfolioContext:
    def __init__(self, portfolio_repository: PortfolioRepository,
                 market_data_service: MarketDataService,
                 market_data_factory: MarketDataFactory,
                 market_data_fetched_handler):
          # to do

    async def fetch_market_data(self):
        # to do
        for md in market_data:
            self.market_data[md.symbol.name] = md
            self._market_data_fetched_handler(MarketDataFetched(
                md.symbol, md.price, md.volume))

    def get_market_data(self, symbol: Symbol):
         # to do

    def calculate_risk(self) -> float:
        return sum(asset.weight.value
                   * self.market_data[asset.symbol.name].price.value
                   / self.market_data[asset.symbol.name].volume.value
                   for asset in self.portfolio.assets) / self.total_weight()

    def total_weight(self):
        return self.portfolio.total_weight()
