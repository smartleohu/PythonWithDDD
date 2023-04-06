import pytest

from solutions.applications.market_data.repositories import \
    MarketDataRepository
from solutions.domains.models.entities import MarketData, Asset
from solutions.domains.services.market_data import MarketDataService
from solutions.domains.models.values import Price, Symbol, Volume, Weight


class TestMarketDataService:

    @pytest.mark.asyncio
    async def test_get_market_data_for_assets(self, monkeypatch):
        # Define a list of Asset objects
        assets = [
            Asset(symbol=Symbol("AAPL"), weight=Weight(0.5)),
            Asset(symbol=Symbol("GOOGL"), weight=Weight(0.5))
        ]

        # Define a list of MarketData objects to be returned by the mock
        market_data_list = [
            MarketData(symbol=Symbol("AAPL"), price=Price(120),
                       volume=Volume(11000)),
            MarketData(symbol=Symbol("GOOGL"), price=Price(250),
                       volume=Volume(22000))
        ]

        # Define a mock for the get_market_data method
        async def mock_get_market_data(session, sym_name):
            print(session, sym_name)
            for market_data in market_data_list:
                if market_data.symbol.name == sym_name:
                    return market_data

        monkeypatch.setattr(MarketDataRepository, 'get_market_data',
                            mock_get_market_data)
        # Create an instance of MarketDataService
        market_data_service = MarketDataService()

        # Call the get_market_data_for_assets method and get the result
        result = await market_data_service.get_market_data_for_assets(assets)

        # Check that the result is a list of MarketData objects
        assert isinstance(result, list)
        assert all(isinstance(item, MarketData) for item in result)

        # Check that the result contains the expected MarketData objects
        for asset in assets:
            symbol_name = asset.symbol.name
            expected_market_data = next(
                md for md in market_data_list if md.symbol.name == symbol_name)
            actual_market_data = next(
                md for md in result if md.symbol.name == symbol_name)
            assert actual_market_data == expected_market_data


