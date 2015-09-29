from collections import namedtuple


"""
    Resources
    Represents the current state of a 'thing'
    Based on current state and who is asking, the representation also
    contains what actions that can be performed on it and what
    other related resources that can be reached.
"""
Resource = namedtuple('Resource', [
    'ref',
    'cls',
    'data',
    'links',
    'actions',
    'embedded'
])

ApplicationData = namedtuple('ApplicationData', ['user_ref'])
CalendarData = namedtuple('CalendarData', [])
UserData = namedtuple('UserData', [
    'first_name',
    'last_name'
])
UserTemplateData = namedtuple('UserTemplate', [
    'first_name',
    'last_name'
])
UserRef = namedtuple('UserRef', [
    'ref',
    'cls',
    'first_name',
    'last_name'
])
