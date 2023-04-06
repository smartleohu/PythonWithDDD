import asyncio

import aiohttp as aiohttp

from exos.applications.market_data.repositories import \
    MarketDataRepository


class MarketDataService:
    @classmethod
    async def get_market_data_for_assets(cls, assets):
        # to do
