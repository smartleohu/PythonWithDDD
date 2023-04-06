from unittest.mock import patch, MagicMock

import pytest

from solutions.infrastructures.internal_services.market_data_restx_api import \
    app, MarketData


class TestWebServices:
    @pytest.fixture(scope='module')
    def client(self):
        with app.test_client() as client:
            yield client

    @patch('sqlite3.connect')
    def test_get_market_data_with_data(self, mock_connect):
        mock_cursor = MagicMock()
        mock_data = ('AAPL', 134.5, 100000)
        mock_cursor.fetchone.return_value = mock_data
        mock_connect.return_value.cursor.return_value = mock_cursor

        data = MarketData.get_market_data('AAPL')
        assert data == {'symbol': 'AAPL', 'price': 134.5, 'volume': 100000}

        mock_connect.assert_called_once_with('market_data.db')
        mock_cursor.execute.assert_called_once_with(
            "SELECT * FROM market_data WHERE symbol = 'AAPL' "
            "ORDER BY timestamp DESC LIMIT 1")
        mock_cursor.fetchone.assert_called_once_with()

    @patch('sqlite3.connect')
    def test_get_market_data_without_data(self, mock_connect):
        mock_cursor = MagicMock()
        mock_data = None
        mock_cursor.fetchone.return_value = mock_data
        mock_connect.return_value.cursor.return_value = mock_cursor

        data = MarketData.get_market_data('MSFT')
        assert data == mock_data

        mock_connect.assert_called_once_with('market_data.db')
        mock_cursor.execute.assert_called_once_with(
            "SELECT * FROM market_data WHERE symbol = 'MSFT' "
            "ORDER BY timestamp DESC LIMIT 1")
        mock_cursor.fetchone.assert_called_once_with()

    def test_get(self, client, monkeypatch):
        mock_data = {'symbol': 'AAPL', 'price': 134.5, 'volume': 100000}
        mock_get_market_data = MagicMock(return_value=mock_data)

        monkeypatch.setattr(MarketData, 'get_market_data',
                            mock_get_market_data)

        response = client.get('/internal/marketdata/AAPL')
        assert response.status_code == 200
        assert response.json == mock_data

        mock_get_market_data.assert_called_once_with('AAPL')

    def test_get_no_data(self, monkeypatch, client):
        mock_get_market_data = MagicMock(return_value=None)

        monkeypatch.setattr(MarketData, 'get_market_data',
                            mock_get_market_data)

        response = client.get('/internal/marketdata/MSFT')
        assert response.status_code == 404
        assert response.json == {
            'message': 'Aucune donnée pour le symbole MSFT. '
                       'You have requested this URI [/internal/'
                       'marketdata/MSFT] but did you mean /'
                       'internal/marketdata/<string:symbol> ?'}

        mock_get_market_data.assert_called_once_with('MSFT')
