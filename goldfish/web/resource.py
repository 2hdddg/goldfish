from __future__ import absolute_import

from collections import namedtuple


"""
    The current state of a 'thing'
    Based on current state and who is asking, the representation also
    contains what actions that can be performed on it and what
    other related resources that can be reached.
    The data can contain simple properties, references to
    resources or representations of resources

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


ApplicationData = namedtuple('ApplicationData', ['user_repr', 'current_link'])

CalendarData = namedtuple('CalendarData', [])

UserData = namedtuple('UserData', [
    'first_name',
    'last_name'
])


PopularCalendarsData = namedtuple('PopularCalendarsData', [])

UserCalendarsData = namedtuple('UserCalendarsData', [
    'list'
])
