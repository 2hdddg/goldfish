from __future__ import absolute_import
from flask import Flask, jsonify, render_template, request, make_response

from goldfish.core.infrastructure import WorkUnit
import goldfish.core.lookup as lookup
import goldfish.core.command as command
import goldfish.web.buildresource as build_resource_for

application = Flask("Goldfish application")


class Context(object):
    def __init__(self, workunit, user=None, userid=None):
        self.workunit = workunit
        if user:
            self.is_authorized = True
            self._user = user
        elif userid:
            self.is_authorized = True
            self._userid = userid
        else:
            self.is_authorized = False

    @property
    def user(self):
        if not self.is_authorized:
            raise "Unauthorized!"

        if not self._user:
            workunit = self.workunit
            self._user = lookup.user(
                workunit, self._userid)

        return self._user


def get_context():
    workunit = WorkUnit()
    context = Context(workunit)
    return context


def _response(context, result):
    if request.is_xhr:
        return jsonify(**result.__dict__)

    application = build_resource_for.application(context, current=result.__dict__)
    return render_template('index.html', application=application.__dict__)


@application.route('/', methods=['GET'])
def index():
    context = get_context()
    with context.workunit:
        application = build_resource_for.application(context)
        if request.is_xhr:
            return jsonify(**application.__dict__)
        return render_template('index.html', application=application.__dict__)


@application.route('/application', methods=['GET'])
def application_index():
    context = get_context()
    with context.workunit:
        result = build_resource_for.application(context)
        return _response(context, result)


@application.route('/application/login', methods=['POST'])
def login():
    body = request.get_json()
    username = body['username']
    password = body['password']

    context = get_context()
    with context.workunit as workunit:
        user = command.try_logon(workunit, username, password)
        if user:
            # Recreate the context with authorized
            # user
            context = Context(workunit, user)

    result = build_resource_for.application(context)
    response = make_response(jsonify(**result.__dict__))

    if user:
        pass
        # build token and set cookie
    else:
        # Set some http status code
        # 401
        response.status_code = 401

    return response


@application.route('/user/template', methods=['GET'])
def user_template():
    context = get_context()
    with context.workunit:
        result = build_resource_for.user_template(context)
        return _response(context, result)


@application.route("/calendar/<int:id>", methods=['GET'])
def calendar_get(id):
    context = get_context()
    with context.workunit as workunit:
        calendar = lookup.calendar(workunit, id)
        result = build_resource_for.calendar(context, calendar)
        return _response(context, result)
