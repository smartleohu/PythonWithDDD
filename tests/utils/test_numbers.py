from solutions.utils.numbers import get_id


def test_get_id():
    gen = get_id()
    uuid1 = next(gen)
    uuid2 = next(gen)
    assert uuid1 != uuid2, "Generated UUIDs should be different"
