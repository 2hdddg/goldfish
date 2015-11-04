from __future__ import absolute_import

from flask import Flask

from . import endpoints

application = Flask("Goldfish application")


def _endpoint(rule, endpoint, methods=['GET']):
    application.add_url_rule(rule, endpoint.__name__, endpoint, methods=methods)


_endpoint('/', endpoints.get_application_html)
_endpoint('/application', endpoints.get_application)
_endpoint('/application/login', endpoints.login, methods=['POST'])
_endpoint('/application/logout', endpoints.logout, methods=['POST'])
_endpoint('/user/template', endpoints.get_user_template)
_endpoint('/user/create', endpoints.create_user, methods=['POST'])
_endpoint('/user/<int:userid>/calendars', endpoints.get_user_calendars)
_endpoint("/calendar/<int:id>", endpoints.get_calendar)
_endpoint("/calendar/template", endpoints.get_calendar_template)
