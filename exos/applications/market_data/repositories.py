import aiohttp

from exos.applications.portfolios.factories import MarketDataFactory


class MarketDataRepository:
    @classmethod
    async def get_market_data(cls, session, symbol):
        # to do
            return MarketDataFactory.create_market_data(
                symbol=symbol,
                price=response_json['price'],
                volume=response_json['volume'])
