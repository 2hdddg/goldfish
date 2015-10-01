import goldfish.web.resource as resource


def application(context, current=None):
    ref = '/application'
    cls = 'Application'
    links = {}
    actions = {}
    embedded = {
        'current': current
    }
    data = None

    if context.is_authorized:
        actions['logout'] = '/application/logout'
        user = user_ref(context, context.user)
        data = resource.ApplicationData(user_ref=user)
    else:
        actions['login'] = '/application/login'
        links['userTemplate'] = '/user/template'
        data = resource.ApplicationData(user_ref=None)

    return resource.Resource(
        ref=ref, cls=cls, data=data, links=links, actions=actions, embedded=embedded)


def calendar(context, calendar):
    ref = '/calendar/%s' % calendar.id
    cls = 'Calendar'
    links = {}
    actions = {}
    embedded = {}
    data = resource.CalendarData()

    return resource.Resource(
        ref=ref, cls=cls, data=data, links=links, actions=actions, embedded=embedded)


def user(context, user):
    ref = '/user/%s' % user.id
    cls = 'User'
    links = {}
    actions = {}
    embedded = {}
    data = resource.UserData(
        first_name=user.first_name, last_name=user.last_name)

    return resource.Resource(
        ref=ref, cls=cls, data=data, links=links, actions=actions, embedded=embedded)


def user_template(context):
    ref = '/user/template'
    cls = 'UserTemplate'
    links = {}
    actions = {}
    embedded = {}

    data = resource.UserTemplateData(
        first_name='', last_name='')

    return resource.Resource(
        ref=ref, cls=cls, data=data, links=links, actions=actions, embedded=embedded)


def user_ref(context, user):
    ref = '/user/%s' % user.id
    cls = 'UserRef'

    return resource.UserRef(
        ref=ref, cls=cls, first_name=user.first_name, last_name=user.last_name)
