from __future__ import absolute_import

from flask import Flask

from . import endpoints

application = Flask("Goldfish application")


def _endpoint(rule, endpoint, methods=['GET']):
    application.add_url_rule(rule, endpoint.__name__, endpoint, methods=methods)


_endpoint('/', endpoints.index)
_endpoint('/application', endpoints.application_index)
_endpoint('/application/login', endpoints.login, methods=['POST'])
_endpoint('/application/logout', endpoints.logout, methods=['POST'])
_endpoint('/user/template', endpoints.user_template)
_endpoint('/user/create', endpoints.user_create, methods=['POST'])
_endpoint('/user/<int:userid>/calendars', endpoints.user_calendars_get)
_endpoint("/calendar/<int:id>", endpoints.calendar_get)
_endpoint("/calendar/template", endpoints.calendar_template)
