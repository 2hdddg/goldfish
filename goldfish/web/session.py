from flask import request

from goldfish.core.infrastructure import WorkUnit
from goldfish.web.context import Context


def _get_user_id():
    userid = request.cookies.get('userid')
    if userid:
        return int(userid)
    else:
        return None


def get_context():
    workunit = WorkUnit()
    context = Context(workunit, userid=_get_user_id())
    return context


def reset(response):
    response.set_cookie('userid', '', expires=0)


def set(user, response):
    response.set_cookie('userid', str(user.id))
