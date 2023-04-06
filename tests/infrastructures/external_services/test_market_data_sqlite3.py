from unittest.mock import Mock

import pytest

from solutions.infrastructures.external_services import \
    market_data_sqlite3 as bases


@pytest.fixture(scope='function')
def mock_sqlite3(monkeypatch):
    conn_mock = Mock()
    cursor_mock = Mock()
    conn_mock.cursor.return_value = cursor_mock
    monkeypatch.setattr('sqlite3.connect', lambda x: conn_mock)
    return conn_mock


def test_create_market_data(mock_sqlite3):
    bases.create_market_data()

    mock_sqlite3.cursor.assert_called_once_with()
    mock_sqlite3.cursor().execute.assert_called_once_with('''
            CREATE TABLE IF NOT EXISTS market_data (
                symbol TEXT,
                price REAL,
                volume INTEGER,
                timestamp BIGINT 
            )
        ''')
    mock_sqlite3.commit.assert_called_once_with()
    mock_sqlite3.close.assert_called_once_with()


def test_update_market_data(monkeypatch):
    def mock_create_market_data():
        pass

    def mock_sleep(seconds):
        print(seconds)

    monkeypatch.setattr(bases, 'create_market_data', mock_create_market_data)
    monkeypatch.setattr(bases.time, 'sleep', mock_sleep)

    event = bases.threading.Event()

    def mock_update_market_data(m_event, waiting_time=0):
        for data in bases.market_data_list:
            print(m_event, waiting_time, data)

    monkeypatch.setattr(bases, 'update_market_data', mock_update_market_data)

    test_thread = bases.threading.Thread(target=bases.update_market_data,
                                         args=(event,))
    test_thread.start()
    bases.time.sleep(0.1)
    event.set()
    test_thread.join()
