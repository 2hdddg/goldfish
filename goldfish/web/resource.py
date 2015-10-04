from collections import namedtuple


"""
    Resources
    Represents the current state of a 'thing'
    Based on current state and who is asking, the representation also
    contains what actions that can be performed on it and what
    other related resources that can be reached.

    Example:

    {
        ref: '/url/to/load/myself',
        cls: 'ResourceClassName',
        data: {

        },
        links: {
            next: 'url/to/load/more/data',
        },
        actions:
            create: {
                ref: '/whatever/create',
                form: {
                    first_name: {
                        value: '',
                        type: number/email/text/password/specific
                    },
                    password: {
                    }
                }
            }
        },
        embedded: {
            // Named entry
            'current': {
                // a resource as well
            },
            'url/to/something/refered/to/in/link/or/data': {
                // a resource as well
            }
        }
    }
"""

Resource = namedtuple('Resource', [
    'ref',
    'cls',
    'data',
    'links',
    'actions',
    'embedded'
])

Action = namedtuple('Action', [
    'ref',
    'form'
])

FormField = namedtuple('FormField', [
    'name',
    'value',
    'type',
    'required'
])

ApplicationData = namedtuple('ApplicationData', ['user_ref'])

CalendarData = namedtuple('CalendarData', [])

UserData = namedtuple('UserData', [
    'first_name',
    'last_name'
])

UserRef = namedtuple('UserRef', [
    'ref',
    'cls',
    'first_name',
    'last_name'
])
