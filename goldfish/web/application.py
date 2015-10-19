from __future__ import absolute_import
from flask import Flask, jsonify, render_template, request, make_response

import goldfish.core.lookup as lookup
import goldfish.core.command as command
import goldfish.core.query as query

import goldfish.web.buildresource as build_resource_for
import goldfish.web.buildactionresponse as build_action_response_for
from goldfish.web.context import Context
from goldfish.web.dictalizer import namedtuple_to_dict
import goldfish.web.session as session

application = Flask("Goldfish application")


def _response(context, result):
    if request.is_xhr:
        result_as_dict = namedtuple_to_dict(result)
        return jsonify(result_as_dict)

    application = build_resource_for.application(context, current=result)
    application_as_dict = namedtuple_to_dict(application)
    return render_template('index.html', application=application_as_dict)


def _default_page(context):
    if context.is_authorized:
        calendars = query.get_user_calendars(context.workunit, context.userid)
        return build_resource_for.user_calendars(context, calendars, context.user)
    else:
        return build_resource_for.popular_calendars(context)


@application.route('/', methods=['GET'])
def index():
    context = session.get_context()
    with context.workunit:
        current = _default_page(context)
        application = build_resource_for.application(context, current=current)
        application_as_dict = namedtuple_to_dict(application)
        if request.is_xhr:
            return jsonify(application_as_dict)
        return render_template('index.html', application=application_as_dict)


@application.route('/application', methods=['GET'])
def application_index():
    context = session.get_context()
    with context.workunit:
        result = build_resource_for.application(context)
        return _response(context, result)


@application.route('/application/login', methods=['POST'])
def login():
    body = request.get_json()
    username = body['username']
    password = body['password']

    context = session.get_context()
    with context.workunit as workunit:
        user = command.try_logon(workunit, username, password)
        if user:
            # Recreate the context with authorized user
            context = Context(workunit, user)

            result = build_action_response_for.logged_in(context)
            result = namedtuple_to_dict(result)
            response = make_response(jsonify(result))

            session.set(user, response)
        else:
            response = make_response()
            response.status_code = 401

    return response


@application.route('/application/logout', methods=['POST'])
def logout():
    context = session.get_context()
    with context.workunit as workunit:
        # Recreate the context as uauthorized
        context = Context(workunit)
        result = build_action_response_for.logged_out(context)
        result = namedtuple_to_dict(result)
        response = make_response(jsonify(result))
        session.reset(response)

    return response


@application.route('/user/template', methods=['GET'])
def user_template():
    context = session.get_context()
    with context.workunit:
        result = build_resource_for.user_template(context)
        return _response(context, result)


@application.route('/user/create', methods=['POST'])
def user_create():
    body = request.get_json()
    first_name = body['first_name']
    last_name = body['last_name']
    logged_in = False

    context = session.get_context()
    with context.workunit as workunit:
        user = command.create_user(
            workunit, first_name, last_name, '', '')
        if not context.is_authorized:
            # Login user, assume sign up
            # Recreate the context with created user
            context = Context(workunit, user)
            logged_in = True

        result = build_action_response_for.created_user(context, user)
        result = namedtuple_to_dict(result)
        response = make_response(jsonify(result))

        if logged_in:
            session.set(user, response)

        return response


@application.route('/user/<int:userid>/calendars', methods=['GET'])
def user_calendars_get(userid):
    context = session.get_context()
    with context.workunit as workunit:
        calendars = query.get_user_calendars(workunit, userid)
        result = build_resource_for.user_calendars(context, calendars, context.user)
        return _response(context, result)


@application.route("/calendar/<int:id>", methods=['GET'])
def calendar_get(id):
    context = session.get_context()
    with context.workunit as workunit:
        calendar = lookup.calendar(workunit, id)
        result = build_resource_for.calendar(context, calendar)
        return _response(context, result)
