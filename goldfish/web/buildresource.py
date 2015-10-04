import goldfish.web.resource as resource


def _logout_action():
    form = []
    return resource.Action(
        ref='/application/logout', form=form)


def _login_action():
    form = [
        resource.FormField(name='username', value='', type='email', required=True),
        resource.FormField(name='password', value='', type='password', required=True)
    ]
    return resource.Action(
        ref='/application/login', form=form)


def _create_user_action():
    form = [
        resource.FormField(name='first_name', value='', type='name', required=True),
        resource.FormField(name='last_name', value='', type='name', required=True),
        resource.FormField(name='email', value='', type='email', required=True)
    ]
    return resource.Action(
        ref='/user/create', form=form)


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
        actions['logout'] = _logout_action()
        user = user_ref(context, context.user)
        data = resource.ApplicationData(user_ref=user)
    else:
        actions['login'] = _login_action()
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
    actions = {
        'create': _create_user_action()
    }
    embedded = {}

    return resource.Resource(
        ref=ref, cls=cls, data=None, links=links, actions=actions, embedded=embedded)


def user_ref(context, user):
    ref = '/user/%s' % user.id
    cls = 'UserRef'

    return resource.UserRef(
        ref=ref, cls=cls, first_name=user.first_name, last_name=user.last_name)
