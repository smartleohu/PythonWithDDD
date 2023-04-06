import datetime
import time

utc_now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
utc_now_tsp: int = int(utc_now.timestamp())

monotonic_time = time.monotonic()

if __name__ == '__main__':
    print(
        f"Monotonic UTC now: {utc_now.isoformat()} or {utc_now_tsp} "
        f"({monotonic_time:.3f} seconds since epoch)")
