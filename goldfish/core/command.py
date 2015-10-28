from __future__ import absolute_import

from .entity import User, Calendar
from . import query


def create_user(workunit, first_name, last_name, email, password):
    id = workunit.db.next_id()
    user = User(
        id=id, first_name=first_name, last_name=last_name,
        email=email, hashedpassword=password)
    workunit.db.users[id] = user

    return user


def try_logon(workunit, username, password, get_user_by_email=query.get_user_by_email):
    user = get_user_by_email(workunit, username)
    if user and user.hashedpassword == password:
        return user

    return None


def create_calendar(workunit, owner):
    id = workunit.db.next_id()
    calendar = Calendar(id=id, owner=owner)

    workunit.db.calendars[id] = calendar

    return calendar
