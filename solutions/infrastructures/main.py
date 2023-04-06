import threading

from solutions.infrastructures.external_services.market_data_sqlite3 import \
    update_market_data
from solutions.infrastructures.internal_services.market_data_restx_api import \
    app

if __name__ == '__main__':
    t_event = threading.Event()
    t_extern = threading.Thread(target=update_market_data, args=(t_event, 60))
    t_extern.start()
    t_intern = threading.Thread(target=app.run, kwargs={'debug': False})
    t_intern.start()

    t_extern.join()
    t_intern.join()
