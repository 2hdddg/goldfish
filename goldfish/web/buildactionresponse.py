from goldfish.web.action import ActionResponse
import goldfish.web.buildresource as build_resource_for


def logged_in(context):
    application = build_resource_for.application(context)
    events = {
        'changed': [build_resource_for.application_ref(context)],
        'logged_in': [application.data.user_ref]
    }
    embedded = {}
    embedded[application.ref] = application
    response = ActionResponse(events=events, embedded=embedded)
    return response


def created_user(context, user):
    user_resource = build_resource_for.user(context, user)
    events = {
        'created': [build_resource_for.user_ref(context, user)]
    }
    embedded = {}
    embedded[user_resource.ref] = user_resource
    # if context.user same as user, we signed up
    if context.is_authorized and context.user.id == user.id:
        application = build_resource_for.application(context)
        embedded[application.ref] = application
        events['logged_in'] = application.data.user_ref
        events['changed'] = build_resource_for.application_ref(context)
    response = ActionResponse(events=events, embedded=embedded)
    return response
