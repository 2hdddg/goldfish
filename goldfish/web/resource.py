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
            create: [{
                ref: '/whatever/create',
                cls: 'xx'
            }]
        },
        embedded: {
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

ResourceRef = namedtuple('ResourceRef', [
    'ref',
    'cls',
    'refcls',
    'data'
])

ApplicationData = namedtuple('ApplicationData', ['user_ref', 'current_url'])

CalendarData = namedtuple('CalendarData', [])

UserData = namedtuple('UserData', [
    'first_name',
    'last_name'
])

UserRefData = namedtuple('UserRefData', [
    'first_name',
    'last_name'
])
