import datetime

from solutions.utils.datetimes import monotonic_time, utc_now


def test_utc_now():
    assert isinstance(utc_now, datetime.datetime), \
        "utc_now should be a datetime object"
    assert utc_now.tzinfo == datetime.timezone.utc, \
        "utc_now should be timezone-aware and set to UTC"


def test_monotonic_time():
    assert isinstance(monotonic_time, float), \
        "monotonic_time should be a float"
