from __future__ import absolute_import

from .entity import User, Calendar


class Command(object):
    def __init__(self, db, query):
        self._db = db
        self._query = query

    @property
    def user(self):
        return UserCommand(self._db, self._query)

    @property
    def calendar(self):
        return CalendarCommand(self._db, self._query)


class UserCommand(object):
    def __init__(self, db, query):
        self._db = db
        self._query = query

    def create(self, first_name, last_name, email, password):
        id = self._db.next_id()
        user = User(
            id=id, first_name=first_name, last_name=last_name,
            email=email, hashedpassword=password)
        self._db.users[id] = user

        return user

    def try_logon(self, username, password):
        user = self._query.user.by_email(username)
        if user and user.hashedpassword == password:
            return user

        return None


class CalendarCommand(object):
    def __init__(self, db, query):
        self._db = db
        self._query = query

    def create(self, owner, name):
        id = self._db.next_id()
        calendar = Calendar(id=id, owner=owner, name=name)

        self._db.calendars[id] = calendar

        return calendar
