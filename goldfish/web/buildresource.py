from __future__ import absolute_import

from .resource import Resource, ApplicationData, UserData, CalendarData, PopularCalendarsData, UserCalendarsData
from .action import Action, FormField
from . import buildrepresentation as build_representation_for


def _logout_action():
    form = []
    return Action(
        ref='/logout', form=form)


def _login_action():
    form = [
        FormField(name='username', value='', type='email', required=True),
        FormField(name='password', value='', type='password', required=True)
    ]
    return Action(
        ref='/login', form=form)


def _create_user_action():
    form = [
        FormField(name='first_name', value='', type='name', required=True),
        FormField(name='last_name', value='', type='name', required=True),
        FormField(name='email', value='', type='email', required=True)
    ]
    return Action(
        ref='/user/create', form=form)


def _create_calendar_action():
    form = [
        FormField(name='name', value='', type='name', required=True),
    ]
    return Action(
        ref='/calendar/create', form=form)


def _link_to_user_calendars(user):
    return '/user/' + str(user.id) + "/calendars"


def _link_to_popular_calendars():
    return '/calendars/popular'


def application(context, current=None):
    ref = '/application'
    cls = 'Application'
    links = {}
    actions = {}
    embedded = {}
    data = None

    if current:
        links['current'] = current.ref
        embedded[current.ref] = current

    if context.is_authorized:
        user = context.user
        actions['logout'] = _logout_action()
        links['default'] = _link_to_user_calendars(user)
        user = build_representation_for.user(context, user)
        data = ApplicationData(user_repr=user)
    else:
        actions['login'] = _login_action()
        links['userTemplate'] = '/user/template'
        links['default'] = _link_to_popular_calendars()
        data = ApplicationData(user_repr=None)

    return Resource(
        ref=ref, cls=cls, data=data, links=links, actions=actions, embedded=embedded)


def popular_calendars(context):
    ref = _link_to_popular_calendars()
    cls = 'GlobalCalendars'
    links = {}
    actions = {}
    embedded = {}
    data = PopularCalendarsData()

    return Resource(
        ref=ref, cls=cls, data=data, links=links, actions=actions, embedded=embedded)


def user_calendars(context, calendars, user):
    ref = _link_to_user_calendars(user)
    cls = 'UserCalendars'
    links = {}
    actions = {}
    embedded = {}
    calendars_repr = [
        build_representation_for.calendar(context, c) for c in calendars]
    data = UserCalendarsData(list=calendars_repr)

    user_same_as_logged_in = user.id == context.user.id

    if user_same_as_logged_in:
        links['calendarTemplate'] = '/calendar/template'

    return Resource(
        ref=ref, cls=cls, data=data, links=links, actions=actions, embedded=embedded)


def calendar(context, calendar):
    ref = '/calendar/%s' % calendar.id
    cls = 'Calendar'
    links = {}
    actions = {}
    embedded = {}
    data = CalendarData(name=calendar.name)

    return Resource(
        ref=ref, cls=cls, data=data, links=links, actions=actions, embedded=embedded)


def calendar_template(context):
    ref = '/calendar/template'
    cls = 'CalendarTemplate'
    links = {}
    actions = {
        'create': _create_calendar_action()
    }
    embedded = {}

    return Resource(
        ref=ref, cls=cls, data=None, links=links, actions=actions, embedded=embedded)


def user(context, user):
    ref = '/user/%s' % user.id
    cls = 'User'
    links = {}
    actions = {}
    embedded = {}
    data = UserData(
        first_name=user.first_name, last_name=user.last_name)

    user_same_as_logged_in = context.is_authorized and user.id == context.user.id

    if user_same_as_logged_in:
        links['calendars'] = _link_to_user_calendars(user)

    return Resource(
        ref=ref, cls=cls, data=data, links=links, actions=actions, embedded=embedded)


def user_template(context):
    ref = '/user/template'
    cls = 'UserTemplate'
    links = {}
    actions = {
        'create': _create_user_action()
    }
    embedded = {}

    return Resource(
        ref=ref, cls=cls, data=None, links=links, actions=actions, embedded=embedded)
