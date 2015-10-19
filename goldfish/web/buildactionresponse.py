from goldfish.web.action import ActionResponse
import goldfish.web.buildresource as build_resource_for
import goldfish.web.buildrepresentation as build_representation_for


def logged_in(context):
    application = build_resource_for.application(context)
    application_repr = build_representation_for.application(context)
    user_repr = application.data.user_repr
    user_resource = build_resource_for.user(context, context.user)

    events = {
        'logged_in': [user_repr, application_repr]
    }
    embedded = {}
    embedded[user_resource.ref] = user_resource
    embedded[application.ref] = application
    response = ActionResponse(events=events, embedded=embedded)

    return response


def logged_out(context):
    application = build_resource_for.application(context)
    application_repr = build_representation_for.application(context)
    events = {
        'logged_out': [application_repr]
    }
    embedded = {}
    embedded[application.ref] = application
    response = ActionResponse(events=events, embedded=embedded)

    return response


def created_user(context, user):
    user_resource = build_resource_for.user(context, user)
    user_repr = build_representation_for.user(context, user)
    events = {
        'created': [user_repr]
    }
    embedded = {}
    embedded[user_resource.ref] = user_resource

    # if context.user same as user, we signed up
    if context.is_authorized and context.user.id == user.id:
        application = build_resource_for.application(context)
        application_repr = build_representation_for.application(context)
        embedded[application.ref] = application
        events['logged_in'] = [user_repr, application_repr]
    response = ActionResponse(events=events, embedded=embedded)

    return response
