from __future__ import absolute_import


class Query(object):
    def __init__(self, db):
        self._db = db

    @property
    def user(self):
        return UserQuery(self._db)

    @property
    def calendar(self):
        return CalendarQuery(self._db)


class UserQuery(object):
    def __init__(self, db):
        self._db = db

    def by_email(self, email):
        for _, user in self._db.users.iteritems():
            if user.email == email:
                return user

        return None


class CalendarQuery(object):
    def __init__(self, db):
        self._db = db

    def by_owner(self, userid):
        for _, calendar in self._db.calendars.iteritems():
            if calendar.owner.id == userid:
                yield calendar
