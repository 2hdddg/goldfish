from __future__ import absolute_import

from .exceptions import NotFound


def user(workunit, id):
    try:
        return workunit.db.users[id]
    except KeyError:
        raise NotFound()


def calendar(workunit, id):
    return workunit.db.calendars[id]
