import asyncio

import aiohttp as aiohttp

from solutions.applications.market_data.repositories import \
    MarketDataRepository


class MarketDataService:
    @classmethod
    async def get_market_data_for_assets(cls, assets):
        async with aiohttp.ClientSession(trust_env=True) as session:
            tasks = [
                asyncio.create_task(
                    MarketDataRepository.get_market_data(
                        session, asset.symbol.name)) for
                asset in assets]
            return await asyncio.gather(*tasks)
