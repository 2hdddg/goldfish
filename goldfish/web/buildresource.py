from goldfish.web.resource import *
from goldfish.web.action import Action, FormField


def _logout_action():
    form = []
    return Action(
        ref='/application/logout', form=form)


def _login_action():
    form = [
        FormField(name='username', value='', type='email', required=True),
        FormField(name='password', value='', type='password', required=True)
    ]
    return Action(
        ref='/application/login', form=form)


def _create_user_action():
    form = [
        FormField(name='first_name', value='', type='name', required=True),
        FormField(name='last_name', value='', type='name', required=True),
        FormField(name='email', value='', type='email', required=True)
    ]
    return Action(
        ref='/user/create', form=form)


def application(context, current=None):
    ref = '/application'
    cls = 'Application'
    links = {}
    actions = {}
    embedded = {}
    data = None
    current_url = current.ref if current else None

    if context.is_authorized:
        actions['logout'] = _logout_action()
        user = user_ref(context, context.user)
        data = ApplicationData(user_ref=user, current_url=current_url)
    else:
        actions['login'] = _login_action()
        links['userTemplate'] = '/user/template'
        data = ApplicationData(user_ref=None, current_url=current_url)

    if current:
        embedded[current.ref] = current

    return Resource(
        ref=ref, cls=cls, data=data, links=links, actions=actions, embedded=embedded)


def popular_calendars(context):
    ref = '/calendars/popular'
    cls = 'GlobalCalendars'
    links = {}
    actions = {}
    embedded = {}
    data = PopularCalendarsData()

    return Resource(
        ref=ref, cls=cls, data=data, links=links, actions=actions, embedded=embedded)


def user_calendars(context):
    ref = '/user/' + context.user.id + "/calendars"
    cls = 'UserCalendars'
    links = {}
    actions = {}
    embedded = {}
    data = UserCalendarsData()

    return Resource(
        ref=ref, cls=cls, data=data, links=links, actions=actions, embedded=embedded)


def application_ref(context):
    return ResourceRef(ref='/application', cls="Ref", refcls="Application", data=None)


def calendar(context, calendar):
    ref = '/calendar/%s' % calendar.id
    cls = 'Calendar'
    links = {}
    actions = {}
    embedded = {}
    data = CalendarData()

    return Resource(
        ref=ref, cls=cls, data=data, links=links, actions=actions, embedded=embedded)


def user(context, user):
    ref = '/user/%s' % user.id
    cls = 'User'
    links = {}
    actions = {}
    embedded = {}
    data = UserData(
        first_name=user.first_name, last_name=user.last_name)

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


def user_ref(context, user):
    ref = '/user/%s' % user.id
    data = UserRefData(first_name=user.first_name, last_name=user.last_name)

    return ResourceRef(
        ref=ref, cls="Ref", refcls="User", data=data)
