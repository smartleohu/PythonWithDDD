import uuid


def get_id():
    while True:
        yield uuid.uuid4()
