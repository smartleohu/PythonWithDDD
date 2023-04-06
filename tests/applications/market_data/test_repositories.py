from unittest.mock import AsyncMock, MagicMock

import aiohttp
import pytest
from aiohttp import ContentTypeError, ClientResponse

from solutions.applications.market_data.repositories import \
    MarketDataRepository


class TestMarketDataRepository:
    @pytest.mark.asyncio
    async def test_get_market_data_error(self):
        # Create a mock response object with status code 404
        response = AsyncMock(status=404)
        response.json = AsyncMock(return_value={})

        # Create a mock session object that returns the response object
        session = AsyncMock(spec=aiohttp.ClientSession)
        async with self.context_manager_mock() as manager_mock:
            manager_mock.__aenter__.return_value = response
            session.get = AsyncMock(return_value=manager_mock)

            # Call the get_market_data method with the mock session & a symbol
            result = await MarketDataRepository.get_market_data(session,
                                                                "AAPL")

            # Assert that the result is None
            assert result is None

    @pytest.mark.asyncio
    async def test_get_market_data_content_type_error(self):
        # Create a mock response object with content type 'text/html'
        response = MagicMock()
        response.status = 200
        response.json = AsyncMock(
            side_effect=ContentTypeError(response,
                                         (MagicMock(spec=ClientResponse),)))

        # Create a mock session object that returns the response object
        session = AsyncMock(spec=aiohttp.ClientSession)
        async with self.context_manager_mock() as manager_mock:
            manager_mock.__aenter__.return_value = response
            session.get = AsyncMock(return_value=manager_mock)

            # Call the get_market_data method with the mock session & a symbol
            result = await MarketDataRepository.get_market_data(session,
                                                                "AAPL")

            # Assert that the result is None
            assert result is None

    @pytest.mark.asyncio
    async def test_get_market_data_expected_value(self):
        # Create a mock response
        response = MagicMock(status=200)
        response.json = AsyncMock(
            return_value={"symbol": "AAPL", "price": 200.0})

        # Create a mock session
        session = AsyncMock(spec=aiohttp.ClientSession)
        async with self.context_manager_mock() as manager_mock:
            manager_mock.__aenter__.return_value = response
            session.get = AsyncMock(return_value=manager_mock)

            # Call the get_market_data method with the mock session & a symbol
            result = await MarketDataRepository.get_market_data(session,
                                                                "AAPL")

            # Assert that the function returned the expected result
            assert result == {"symbol": "AAPL", "price": 200.0}

    @classmethod
    def context_manager_mock(cls):
        # Create a mock context manager object
        manager_mock = MagicMock()

        # Add an __aenter__ method that returns the object itself
        manager_mock.__aenter__ = AsyncMock(return_value=manager_mock)

        # Add an __aexit__ method that does nothing
        manager_mock.__aexit__ = AsyncMock()

        return manager_mock
