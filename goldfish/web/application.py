from __future__ import absolute_import
from flask import Flask, jsonify, render_template, request, make_response

from goldfish.core.infrastructure import WorkUnit
import goldfish.core.lookup as lookup
import goldfish.core.command as command
import goldfish.web.buildresource as build_resource_for
import goldfish.web.buildactionresponse as build_action_response_for

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


def _dict_containing_namedtuples_to_dict(d):
    for k, v in d.iteritems():
        if isinstance(v, tuple):
            d[k] = _namedtuple_to_dict(v)
        elif isinstance(v, dict):
            d[k] = _dict_containing_namedtuples_to_dict(v)
        elif isinstance(v, list):
            d[k] = _list_containing_named_tuples_to_list(v)
    return d


def _list_containing_named_tuples_to_list(l):
    for i, x in enumerate(l):
        if isinstance(x, tuple):
            l[i] = _namedtuple_to_dict(x)
        elif isinstance(x, dict):
            l[i] = _dict_containing_namedtuples_to_dict(x)
        elif isinstance(x, list):
            l[i] = _list_containing_named_tuples_to_list(x)
    return l


def _namedtuple_to_dict(nt):
    d = nt._asdict()
    return _dict_containing_namedtuples_to_dict(d)


def _response(context, result):
    if request.is_xhr:
        result_as_dict = _namedtuple_to_dict(result)
        return jsonify(result_as_dict)

    application = build_resource_for.application(context, current=result)
    application_as_dict = _namedtuple_to_dict(application)
    return render_template('index.html', application=application_as_dict)


@application.route('/', methods=['GET'])
def index():
    context = get_context()
    with context.workunit:
        application = build_resource_for.application(context)
        application_as_dict = _namedtuple_to_dict(application)
        if request.is_xhr:
            return jsonify(application_as_dict)
        return render_template('index.html', application=application_as_dict)


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

            # build token and set cookie

            result = build_action_response_for.logged_in(context)
            result = _namedtuple_to_dict(result)
            response = make_response(jsonify(result))
        else:
            response = make_response()
            response.status_code = 401

    return response


@application.route('/user/template', methods=['GET'])
def user_template():
    context = get_context()
    with context.workunit:
        result = build_resource_for.user_template(context)
        return _response(context, result)


@application.route('/user/create', methods=['POST'])
def user_create():
    body = request.get_json()
    first_name = body['first_name']
    last_name = body['last_name']

    context = get_context()
    with context.workunit as workunit:
        user = command.create_user(
            workunit, first_name, last_name, '', '')
        if not context.is_authorized:
            # Login user, assume sign up
            # Recreate the context with created user
            context = Context(workunit, user)

            # build token and set cookie

        result = build_action_response_for.created_user(context, user)
    result_as_dict = _namedtuple_to_dict(result)
    return make_response(jsonify(result_as_dict))


@application.route("/calendar/<int:id>", methods=['GET'])
def calendar_get(id):
    context = get_context()
    with context.workunit as workunit:
        calendar = lookup.calendar(workunit, id)
        result = build_resource_for.calendar(context, calendar)
        return _response(context, result)
