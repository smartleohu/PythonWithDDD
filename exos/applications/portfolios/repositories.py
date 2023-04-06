from exos.domains.models.aggregates import Portfolio
from exos.domains.models.entities import Asset
from exos.domains.models.values import Symbol, Weight
from exos.utils.loggers import logger


class PortfolioRepository:
    def __init__(self, db_connector=None):
        self._db_connector = db_connector
        self._portfolio = self.get()

    @property
    def portfolio(self):
         # to do

    @property
    def db_connector(self):
         # to do

    def get(self):
        logger.info("DB Connection for Portfolio fetch")
        logger.debug(self.db_connector or "Mock Portfolio from DB")
        return Portfolio(assets=[
            Asset(symbol=Symbol('AAPL'), weight=Weight(0.5)),
            Asset(symbol=Symbol('GOOGL'), weight=Weight(0.5))])

    def find(self, *args, **kwargs):
        ...

    def add(self, *args, **kwargs):
        ...

    def remove(self, *args, **kwargs):
        ...

    def save(self, *args, **kwargs):
        ...
