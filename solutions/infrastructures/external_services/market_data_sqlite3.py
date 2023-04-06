import random
import sqlite3
import threading
import time

lock = threading.Lock()

market_data_list = [
    {'symbol': 'AAPL', 'price': 150.0, 'volume': 1000000},
    {'symbol': 'GOOGL', 'price': 2500.0, 'volume': 500000},
    {'symbol': 'AAPL', 'price': 155.0, 'volume': 1200000},
    {'symbol': 'GOOGL', 'price': 2525.0, 'volume': 550000},
    {'symbol': 'AAPL', 'price': 157.0, 'volume': 1500000},
    {'symbol': 'GOOGL', 'price': 2550.0, 'volume': 600000},
]


def create_market_data():
    with lock:
        conn = sqlite3.connect('market_data.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS market_data (
                symbol TEXT,
                price REAL,
                volume INTEGER,
                timestamp BIGINT 
            )
        ''')
        conn.commit()
        conn.close()


def update_market_data(event: threading.Event, waiting_time: float = 60.0):
    create_market_data()
    conn = sqlite3.connect('market_data.db')
    c = conn.cursor()
    while True:
        for data in market_data_list:
            c.execute(f"INSERT INTO market_data VALUES "
                      f"('{data['symbol']}', {data['price']}, "
                      f"{data['volume']}, (strftime('%s', 'now') * 1000))")
            conn.commit()
            time.sleep(random.uniform(0.1, 1))
        print(f"update in {waiting_time} seconds...")
        event.wait(waiting_time)


if __name__ == '__main__':
    t_event = threading.Event()
    t = threading.Thread(target=update_market_data, args=(t_event, 60))
    t.start()
    t.join()
