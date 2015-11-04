from __future__ import absolute_import

from flask import jsonify, render_template, request, make_response

from .dictalizer import namedtuple_to_dict
from .context import Context
from . import session
from . import buildresource as build_resource_for
from . import buildactionresponse as build_action_response_for


def _response(context, result):
    if request.is_xhr:
        result_as_dict = namedtuple_to_dict(result)
        return jsonify(result_as_dict)

    application = build_resource_for.application(context, current=result)
    application_as_dict = namedtuple_to_dict(application)
    return render_template('index.html', application=application_as_dict)


def _default_page(context):
    if context.is_authorized:
        workunit = context.workunit
        calendars = workunit.query.calendar.by_owner(context.userid)
        return build_resource_for.user_calendars(context, calendars, context.user)
    else:
        return build_resource_for.popular_calendars(context)


def get_application_html():
    context = session.get_context()
    with context.workunit:
        current = _default_page(context)
        application = build_resource_for.application(context, current=current)
        application_as_dict = namedtuple_to_dict(application)
        if request.is_xhr:
            return jsonify(application_as_dict)
        return render_template('index.html', application=application_as_dict)


def get_application():
    context = session.get_context()
    with context.workunit:
        result = build_resource_for.application(context)
        return _response(context, result)


def login():
    body = request.get_json()
    username = body['username']
    password = body['password']

    context = session.get_context()
    with context.workunit as workunit:
        user = workunit.command.user.try_logon(username, password)
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


def get_user_template():
    context = session.get_context()
    with context.workunit:
        result = build_resource_for.user_template(context)
        return _response(context, result)


def create_user():
    body = request.get_json()
    first_name = body['first_name']
    last_name = body['last_name']
    logged_in = False

    context = session.get_context()
    with context.workunit as workunit:
        user = workunit.command.user.create(
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


def get_user(id):
    context = session.get_context()
    with context.workunit as workunit:
        user = workunit.lookup.user(id)
        result = build_resource_for.user(context, user)
        return _response(context, result)


def get_user_calendars(userid):
    context = session.get_context()
    with context.workunit as workunit:
        calendars = workunit.query.calendar.by_owner(userid)
        result = build_resource_for.user_calendars(context, calendars, context.user)
        return _response(context, result)


def get_calendar(id):
    context = session.get_context()
    with context.workunit as workunit:
        calendar = workunit.lookup.calendar(id)
        result = build_resource_for.calendar(context, calendar)
        return _response(context, result)


def get_calendar_template():
    context = session.get_context()
    with context.workunit:
        result = build_resource_for.calendar_template(context)
        return _response(context, result)
