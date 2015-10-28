from __future__ import absolute_import


def get_user_by_email(workunit, email):
    for _, user in workunit.db.users.iteritems():
        if user.email == email:
            return user

    return None


def get_user_calendars(workunit, userid):
    for _, calendar in workunit.db.calendars.iteritems():
        if calendar.owner == userid:
            yield calendar
