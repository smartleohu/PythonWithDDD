import aiohttp

from solutions.applications.portfolios.factories import MarketDataFactory


class MarketDataRepository:
    @classmethod
    async def get_market_data(cls, session, symbol):
        url = f"http://localhost:5000/marketdata/{symbol}"
        async with session.get(url) as response:
            if response.status != 200:
                print(response)
                # Handle error response here
                return
            try:
                response_json = await response.json()
            except aiohttp.ContentTypeError:
                print(response_json)
                # Handle unexpected response here
                return
            return MarketDataFactory.create_market_data(
                symbol=symbol,
                price=response_json['price'],
                volume=response_json['volume'])
