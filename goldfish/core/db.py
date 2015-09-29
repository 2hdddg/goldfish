users = {}
calendars = {}

_id = 0


def next_id():
    global _id
    _id = _id + 1
    return _id
