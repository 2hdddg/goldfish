from __future__ import absolute_import

from .representation import Representation, UserReprData, CalendarReprData


def application(context):
    return Representation(ref='/application', cls="Representation", refcls="Application", data=None)


def user(context, user):
    ref = '/user/%s' % user.id
    data = UserReprData(first_name=user.first_name, last_name=user.last_name)

    return Representation(
        ref=ref, cls="Representation", refcls="User", data=data)


def calendar(context, calendar):
    ref = '/calendar/%s' % calendar.id
    data = CalendarReprData(name='xyz')

    return Representation(
        ref=ref, cls="Representation", refcls="Calendar", data=data)
