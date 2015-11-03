from __future__ import absolute_import

from .exceptions import NotFound


class Lookup(object):
    def __init__(self, db):
        self._db = db

    def user(self, id):
        try:
            return self._db.users[id]
        except KeyError:
            raise NotFound()

    def calendar(self, id):
        return self._db.calendars[id]
